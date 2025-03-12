<h1 align="center">
  Drakengard 3 - PT-BR Translation
</h1>

<p align="center">
  <a href="#" target="blank">
    <img src="https://64.media.tumblr.com/8e6d5f2b00a4f243dc972f8fca58aa22/tumblr_plk41yKKf01vak9iio1_500.jpg" width="200" alt="Emil" />
  </a>
</p>

<p align="center">
  Application to install and create translations for Drakengard 3 (BLUS31197)
  <br>
  Versão em português deste README.md <a href="https://github.com/Arekushi/drakengard-3-pt-br-translation/blob/master/README.pt.md">aqui</a>
</p>

<br>

# About the project...
Translation project for the PS3-exclusive **Drakengard 3!** This incredible RPG never received official support for Brazilian Portuguese, which kept many players from fully enjoying it. Now, with this translation, more people can experience this masterpiece.

From the same contributors behind the **Brazilian Portuguese translation of [NieR Replicant™ ver.1.22][nier-pt-br]**, the translation was based on the original English texts, using ChatGPT as the main tool. Afterward, we carefully reviewed everything to ensure quality and accuracy — and in most cases, the texts were already quite satisfactory.

ChatGPT was crucial for completing this translation in record time, something impossible with services like Google Translate or Bing, which still struggle with accuracy.

This method can also be used to translate the game into other languages by adjusting the parameters. Just don’t forget to review the texts! 🌍

This project does not intend to replace manual translation efforts, which, although more time-consuming, often have even greater attention to detail.

Oh, and if you want to play Drakengard 3 today, it runs very well via the [RPCS3][rpcs3] emulator. We emphasize that **we do not support piracy** — please only play if you own a legitimate copy of the game. 🎮

<br><br>

## How to help with the translation?
You can review the localized texts in [`texts/translation`][translation] (where the translation is stored). Make your edits/improvements and submit a **pull request**, clearly explaining why you made those changes — they will be reviewed and approved accordingly.

If you’d like to discuss this further, feel free to reach out on my Discord server or through my social media channels below:
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
        <img style="padding: 10px" title="Steam Profile" alt="Steam Profile" width="40px" src="https://i.imgur.com/3qObil8.png">
    </a>
</p>


<br>

## Acknowledgements
🚧 More details soon...

## How to install the translation?
🚧 More details soon...

<br>

# For developers...

## Built with
- [Python 3.10.9][python]

<br>

## Support tools
This project was only possible thanks to the following repositories:
* Tool for text extraction and repacking - [Drakengard-3-Sqex03DataMessage][sqex]

<br>

## Getting started
If you want the project for development, some prerequisites are necessary.

### Prerequisites (Windows)
* Python
  1. You can download here: [Python][python_url]
  2. Here is a step-by-step tutorial. [(Tutorial)][python_tutorial_url]
     1. Tutorial with Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
  1. You can install here: [Poetry][poetry_url]

<br>

### Variables in `.toml` files
I store a lot of information in `.toml` files inside the [`config/toml`][configtoml] directory, including some of the messages I send to ChatGPT for translation. If you’d like to customize the application, I highly recommend checking it out!

<br>

### Installation and Usage
1. Clone the repository.
    ```sh
    git clone https://github.com/Arekushi/drakengard-3-pt-br-translation.git
    ```

2. Install packages with `Poetry`
    ```sh
    poetry install
    ```

3. Run:
    ```sh
    python main.py --help
    ```

4. That's it, you can start developing 🎉

<br>

### Useful commands
🚧 More details soon...

<br>

## Contributors
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] <div title="Code and Translation">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/131723671?v=4"><br><sub>Cristian Kirsch</sub></div>][omainha] <div title="Translation and Review">📚</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/174618134?v=4"><br><sub>Paul Paulo HNKBR</sub></div>][paulo] <div title="Translation and Review">📚</div> |
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
[nier-pt-br]: https://github.com/Arekushi/nier-replicant-pt-br-translation
[translation]: https://github.com/Arekushi/drakengard-3-pt-br-translation/tree/main/texts/translation

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
[omainha]: https://github.com/MainhaLisa
[paulo]: https://github.com/PaulPauloHNKBR
