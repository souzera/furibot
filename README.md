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
PANDASCORE_KEY=#######
```

*Como consigo o `BOT_TOKEN`?*

Para gerar "BOT_TOKEN", no app do telegram solicitamos a criacao de um bot atraves do [BOT_FATHER](https://t.me/BotFather)

*Como consigo a `GEMINI_KEY`?*

A chave do gemini pode ser solicitada pelo link fornecido pela documentacao do agente, para gerar acesse a [documentacao](https://ai.google.dev/gemini-api/docs?hl=pt-br)

*Como consigo o `PANDASCORE_KEY`?*

Crie uma conta em https://developers.pandascore.co/, gere sua chave de API no DASHBOARD.

*Posso utilizar outro agente de IA?*

O projeto foi inicialmente construido utilizando o **GEMINI**, mas pode facilmente ser adaptadado para outros agentes com poucas mudancas.

## 🤖 Comandos

Entrando em contato com [@a_furibot](https://t.me/@a_furibot), os comandos a seguir podem ser utilizados:

1. **/start** - iniciar a interação com o bot
2. **/ai** "texto" - interagir com agente de IA
3. **/next** - responde com a proxima partida da FURIA
4. **/last** - responde com a ultima partida da FURIA
5. **/ranking** - exibe o ranking atual da FURIA na HLTV e a quantidade de pontos
6. **/roster** - exibe a formação atua da equipe de CS

🛠️ Futuras implementações (ideias)

- /vs [time] → histórico de confrontos com outro time
- /stats → estatísticas detalhadas da FURIA ou de jogadores
- /mapas → mapa mais jogado e melhor winrate
- /alerts → receber alertas automáticos de partidas
- adicionar alertas para divulgações para os streamers
- expanções para outras modalidades
- integração com clipes ou vídeos de highlights

👨‍💻 Contribuindo

Pull Requests são bem-vindos! Se quiser sugerir melhorias, relatórios de bugs ou novas ideias, abra uma issue ou fale comigo.