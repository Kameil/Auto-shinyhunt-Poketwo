# Auto shiny Hunt Poketwo 🎟
- https://replit.com/@Raquison/Auto-shinyhunt-Poketwo#main.py

## Como usar?
- Primeiro Voce deve Criar o secret **"token"**
  
[![token secret](https://media.discordapp.net/attachments/1128720966575464488/1157394734155825222/Screenshot_28.png?ex=65187357&is=651721d7&hm=6cceb52023bb3448cef0a850f95a7d4cfed7b981ef434c499d02f5f9d55dcd14&= "token secret")](https://media.discordapp.net/attachments/1128720966575464488/1157394734155825222/Screenshot_28.png?ex=65187357&is=651721d7&hm=6cceb52023bb3448cef0a850f95a7d4cfed7b981ef434c499d02f5f9d55dcd14&= "token secret")


- Agora Voce pode comecar a criar os chats em que o bot ira pegar o sh, o limite maximo de chats e 100. Voce deve criar os secrets **catch_id{numero}** o **{numero}** pode ser de um a 100 aqui vai um exemplo de **"catch_id"**
  
[![catch_ids](https://media.discordapp.net/attachments/1128720966575464488/1157395931226964151/Screenshot_29.png?ex=65187475&is=651722f5&hm=cf5c36a21ac404abbebaf6956d8f543a6df0dd5740eedb5eb2b6ca1a7be2b48b&= "catch_ids")](https://media.discordapp.net/attachments/1128720966575464488/1157395931226964151/Screenshot_29.png?ex=65187475&is=651722f5&hm=cf5c36a21ac404abbebaf6956d8f543a6df0dd5740eedb5eb2b6ca1a7be2b48b&=// "catch_ids")


- Colocar a imagem do shinyHunt na pasta **"data/image"** 
**Atençao: Nunca enviar imagens repetidas! e o nome da imagem tem que ser o nome do pokemon**

[![diretorio](https://media.discordapp.net/attachments/1128720966575464488/1157398116891373608/Screenshot_31.png?ex=6518767e&is=651724fe&hm=f69247b02a3de32e10be178f2f8b2e80855ab46fc9ff7a4074249568cd264d44&= "diretorio")](https://media.discordapp.net/attachments/1128720966575464488/1157398116891373608/Screenshot_31.png?ex=6518767e&is=651724fe&hm=f69247b02a3de32e10be178f2f8b2e80855ab46fc9ff7a4074249568cd264d44&= "diretorio")


- ultimo passo ligar [**ctrl + enter** ou clique no botao **run**]

[![run](https://media.discordapp.net/attachments/1128720966575464488/1157396500146556958/Screenshot_30.png?ex=651874fd&is=6517237d&hm=42ab2e29b4b4fbc31b0c00acd313aeebd83bbba0fb88d479769f8c70969bd472&= "run")](https://media.discordapp.net/attachments/1128720966575464488/1157396500146556958/Screenshot_30.png?ex=651874fd&is=6517237d&hm=42ab2e29b4b4fbc31b0c00acd313aeebd83bbba0fb88d479769f8c70969bd472&= "run")

## Erros comuns
#### discord.LoginFailure

![improper token](https://media.discordapp.net/attachments/1128720966575464488/1157403387571216384/Screenshot_32.png?ex=65187b67&is=651729e7&hm=bdebd0250553c806c2dcadc566b6d43feb8546c6edd143e33a00aa42b64ea44a&= "improper token")

- Esse erro acontece quando o token que voce colocou no secret **token** esta invalido.


#### Intents

![missing intents](https://media.discordapp.net/attachments/1128720966575464488/1157462172851507271/Screenshot_35.png?ex=6518b226&is=651760a6&hm=ba6d37febb6a8754c246bd8bb030f16ddaa509d462e0ba6264ff4e25a96acc69&= "missing intents")

- Esse erro acontece quando a biblioteca discord.py se sobrepoe a discord.py-self para resolver e so executar o comando: **pip uninstall discord.py-self && pip install discord.py-self==2.0.0**


## Como o bot identifica o pokemon?
#### o Bot utiliza as bibliotecas os e pillow para identificar se uma imagem e igual a outra utilizando a seguinte logica:
- Primeiro ele faz o download da imagem
- ele pega uma lista de todos os arquivos da pasta "data/image"
- filtra todos os arquivos com a extençao .png
- vai em cada arquivo da pasta "data/image" verificando se ele e igual a imagem que ele fez o download
- e se for ele ira remover o .png e ira enviar @poketwo c {nome_da_imagem_identificada}
- se ele nao encontrar nenhuma imagem igual ele nao ira fazer nada
