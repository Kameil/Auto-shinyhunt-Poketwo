import re, os, asyncio, random, keep_alive, tracemalloc, aiohttp, aiofiles
import discord
from discord.ext import commands
import requests
from PIL import Image, ImageEnhance


catch_id = []



poketwo, pokename, paused, token = '716390085896962058', '0', False, os.environ['token']
unidentified_image = 'original_image.png'


bot = commands.Bot(command_prefix='.', self_bot=True, help_command=None)

async def carregar_catch_ids():
    global catch_id
    print('carregando catch_ids')
    for i in range(101):
        try:
            numero = str(i)
            if numero == '0':
                canal = bot.get_channel(int(os.environ['catch_id']))
                if canal:
                    catch_id.append(str(os.environ['catch_id']))
                else:
                    print('Nao foi possivel obter o canal do secret "catch_id" Verifique o id.')
            else:
                canal = bot.get_channel(int(os.environ[f'catch_id{numero}']))
                if canal:
                    catch_id.append(str(os.environ[f'catch_id{numero}']))
                else:
                    print(f'Nao foi possivel obter o canal do secret "catch_id{numero}" Verifique o id.')
        except KeyError:
            pass
    print(f'{len(catch_id)} Catch_ids Foram carregados.')

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    await carregar_catch_ids()


@bot.event
async def on_message(message):
    global pokename
    global buscar_unidentified_image
    pokename = int(pokename)
    if message.author.id == 874910942490677270 and str(message.channel.id) in catch_id and not paused:
        if len(message.embeds) > 0:
            embed = message.embeds[0]
            if embed.image:
                pokename += 1
                image_url = embed.image.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as response:
                        if response.status == 200:
                            async with aiofiles.open('original_image.png', mode='wb') as file:
                                await file.write(await response.read())
                        else:
                            raise
                await buscar_unidentified_image(message.channel)
    if not message.author.bot and str(message.channel.id) in catch_id:
        await bot.process_commands(message)


async def buscar_unidentified_image(channel):
    global unidentified_image
    if unidentified_image is not None:
        directory = 'data/image'
        identified_words = []
        unidentified_filename = os.path.basename(unidentified_image)
        for filename in os.listdir(directory):
            if filename.endswith('.png'):
                filepath = os.path.join(directory, filename)
                if compare_images(unidentified_image, filepath):
                    identified_word = os.path.splitext(filename)[0]
                    identified_words.append(identified_word)
                    os.rename(filepath, os.path.join(directory, f'{identified_word}.png'))
        if identified_words:
            identified_words_str = ', '.join(identified_words)
            await asyncio.sleep(1)
            await channel.typing()
            pegar = random.randint(3,6)
            await asyncio.sleep(pegar)
            await channel.send(f'<@716390085896962058> c {identified_words_str}')
            print('peguei um sh ai')
    else:
        raise RuntimeError('Nao a imagem para buscar')

def compare_images(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    return image1 == image2

@bot.command()
async def start(ctx):
    global paused
    if paused:
        paused = False
        await ctx.send('Bot started.')
    else:
        await ctx.send('Bot is already runninhg.')

@bot.command()
async def stop(ctx):
    global paused
    if not paused:
        paused = True
        await ctx.send('Bot stopped.')
    else:
        await ctx.send('Bot is already stopped.')
if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.run(token) 
