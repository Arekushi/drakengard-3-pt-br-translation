import os
import typer
import asyncio

from rich import print
from rich.console import Console

from config import settings, ROOT_DIR
from src.helpers.path_helper import get_all_files, has_file, has_folder
from src.translator_engine import TranslatorEngine


console = Console()
app = typer.Typer(
    help=settings.TYPER.TRANSLATE.help
)


@app.command(
    'translate',
    help=settings.TYPER.TRANSLATE.help
)
def translate_command():
    console.rule(settings.CLI.TRANSLATE.rule)
    chat_gpt_translate()


def chat_gpt_translate():
    from src.translator_engine import ChatGPTTranslator
    from src.chat_gpt import G4FWrapper
    
    translator = ChatGPTTranslator(G4FWrapper())
    asyncio.run(translate(translator))


async def translate(translator: TranslatorEngine):
    files = get_files_to_translate()
    await translator.translate_multiple_files(files)


def get_files_to_translate():
    files = []

    for path in settings.TRANSLATION.PATHS.to_translate:
        full_path = f'{ROOT_DIR}\\texts\\{path}'

        if has_file(full_path):
            files.append(full_path)
        elif has_folder(full_path):
            files.extend(get_all_files(full_path))
        else:
            print(
                settings.CLI.TRANSLATE.file_failed.replace('<file>', full_path)
            )
    if (list(settings.TRANSLATION.FILES.to_translate)):
        return list(
            filter(lambda file: os.path.basename(file) in list(settings.TRANSLATION.FILES.to_translate), files)
        )

    return list(
        filter(lambda file: os.path.basename(file) not in list(settings.TRANSLATION.FILES.to_not_translate), files)
    )
