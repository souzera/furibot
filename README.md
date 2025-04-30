# Furibot

## Guia de instalacao


[ RECOMENDADO ] Primeiramente, crie e ative um ambiente virtual python utilizando o comando a seguir, lembre-se de considerar os diferentes cenarios relacionados principalmente a qual seu sistema operacional

```bash
python -m venv .venv
source .venv/bin/activate
```

A seguir, com o ambiente virtual criado e ativado, instale as dependencias do projeto, listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` e adicione as chaves necessarias para a execucao do projeto, a seguir o template do arquivo, listando todos os tokens.

*.env.example*

```env
BOT_TOKEN="########"
GEMINI_KEY="#######"
```

*Como consigo o `BOT_TOKEN`?*

Para gerar "BOT_TOKEN", no app do telegram solicitamos a criacao de um bot atraves do [BOT_FATHER](https://t.me/BotFather)

*Como consigo a `GEMINI_KEY`?*

A chave do gemini pode ser solicitada pelo link fornecido pela documentacao do agente, para gerar acesse a [documentacao](https://ai.google.dev/gemini-api/docs?hl=pt-br)

*Posso utilizar outro agente de IA?*

O projeto foi inicialmente construido utilizando o **GEMINI**, mas pode facilmente ser adaptadado para outros agentes com poucas mudancas.