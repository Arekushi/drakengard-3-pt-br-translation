<h1 align="center">
  Drakengard 3 - Tradução para PT-BR
</h1>

<p align="center">
  <a href="#" target="blank">
    <img src="https://64.media.tumblr.com/8e6d5f2b00a4f243dc972f8fca58aa22/tumblr_plk41yKKf01vak9iio1_500.jpg" width="200" alt="Emil" />
  </a>
</p>

<p align="center">
  Aplicação para instalar e criar traduções para o Drakengard 3 (BLUS31197)
  <br>
  English version of this README.md <a href="https://github.com/Arekushi/drakengard-3-pt-br-translation/blob/master/README.en.md">here</a>
</p>

<br>

# Sobre o projeto...
Projeto de tradução para PT-BR do exclusivo de PS3, Drakengard 3! Esse RPG incrível nunca recebeu suporte oficial ao PT-BR, o que afastou muitos jogadores. Agora, com essa tradução, mais pessoas poderão aproveitar essa obra-prima.

A tradução foi feita a partir dos textos em inglês, usando o ChatGPT como ferramenta principal. Depois, revisamos tudo para garantir qualidade e fidelidade — e, na maioria dos casos, os textos já estavam bastante satisfatórios.

O ChatGPT foi essencial para concluir essa tradução em tempo recorde, algo impossível com serviços como Google Tradutor ou Bing, que ainda deixam a desejar na precisão.

Essa aplicação também pode ser usada para traduzir o jogo para outros idiomas, bastando ajustar os parâmetros. Só não esqueça de revisar os textos! 🌍

Esse projeto não pretende substituir trabalhos de tradução manual, que, embora mais demorados, costumam ter ainda mais atenção aos detalhes.

Ah, e se quiser jogar Drakengard 3 hoje, ele roda muito bem via o emulador [RPCS3][rpcs3]. Ressaltamos que **não apoiamos a pirataria** — jogue apenas se tiver uma cópia legítima do jogo. 🎮

E se puder apoiar, um ☕ via PIX `0dd32e9d-8b78-4978-ad8a-797cbd7380d1` é sempre bem-vindo! ☕🎉

<br><br>

## Como ajudar na tradução?
Olhe a pasta `texts` e olhe os arquivos da pasta `translation` (onde está a tradução)
Faça sua alteração e faça um **pull request**, seja claro porquê você decidiu tais alterações e com base isso será aprovado ou não.

Se quiser conversar mais sobre, podem me chamar no meu servidor do Discord ou em algumas das minhas redes sociais abaixo:
<p align="center">
    <a
        style="all: unset;"
        target="_blank"
        href="https://discord.gg/MBHfdRsEwd">
        <img style="padding: 10px" title="Yokoverso PT-BR - Mods" alt="Yokoverso PT-BR - Mods" width="40px" src="https://i.imgur.com/WuqAV26.png">
    </a>
    <a
        style="all: unset;"
        target="_blank"
        href="https://steamcommunity.com/id/arekushii">
        <img style="padding: 10px" title="Steam" alt="Steam" width="40px" src="https://i.imgur.com/3qObil8.png">
    </a>
</p>

<br>

## Agradecimentos
🚧 Mais detalhes em breve...


## Como instalar a tradução?
🚧 Mais detalhes em breve...

<br>

# Para desenvolvedores...

## Construído com
- [Python 3.10.9][python]

<br>

## Ferramentas de apoio
Esse projeto só foi possível graças a esses repositórios abaixo:
* Ferramenta para extração e recompactação dos textos - [Drakengard-3-Sqex03DataMessage][sqex]

<br>

## Primeiros passos
Se quiser o projeto para desenvolver, alguns pré-requisitos são necessários.

### Pré-requisitos (Windows)
* Python
  1. Você pode baixar aqui: [Python][python_url]
  2. Aqui tem um tutorial passo-a-passo. [(Tutorial)][python_tutorial_url]
     1. Tutorial com Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
  1. Você pode instalar aqui: [Poetry][poetry_url]

<br>

### Variávels em arquivos `.toml`
Eu guardo bastante informação em arquivos `.toml` dentro do diretório [`config/toml`][configtoml], algumas delas são sobre as mensagens que mando para o ChatGPT para a tradução, se quiser customizar a aplicação, recomendo dar uma olhada lá!

<br>

### Instalação e Uso
1. Clone o repositório.
    ```sh
    git clone https://github.com/Arekushi/drakengard-3-pt-br-translation.git
    ```

2. Instale os pacotes com o `Poetry`
    ```sh
    poetry install
    ```

3. Execute:
    ```sh
    python main.py --help
    ```

4. Prontinho, você já pode desenvolver 🎉

<br>

### Comandos úteis
🚧 Mais detalhes em breve...

<br>

## Contribuidores
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] <div title="Código e Tradução">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/131723671?v=4"><br><sub>Cristian Kirsch</sub></div>][omainha] <div title="Tradução e Revisão">📚</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/174618134?v=4"><br><sub>Paul Paulo HNKBR</sub></div>][paulo] <div title="Tradução e Revisão">📚</div> |
| :---: | :---: | :---: |

<!-- [Build With] -->
[python]: https://www.python.org/downloads/

<!-- [Some links] -->
[python_url]: https://www.python.org/downloads/
[python_tutorial_url]: https://www.digitalocean.com/community/tutorials/install-python-windows-10
[miniconda_tutorial]: https://katiekodes.com/setup-python-windows-miniconda/
[poetry_url]: https://python-poetry.org/docs/#installation
[rpcs3]: https://rpcs3.net/
[sqex]: https://github.com/lehieugch68/Drakengard-3-Sqex03DataMessage
[configtoml]: https://github.com/Arekushi/drakengard-3-pt-br-translation/tree/main/config/toml

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
[omainha]: https://github.com/MainhaLisa
[paulo]: https://github.com/PaulPauloHNKBR
