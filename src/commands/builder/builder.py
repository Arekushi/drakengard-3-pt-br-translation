import typer
from config import settings

from .make_translation_folder import make_translation_folder_command
from .translate import translate_command

app = typer.Typer(
    help=settings.TYPER.BUILDER.help
)

app.command('make-translation-folder', help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help)(make_translation_folder_command)
app.command('translate', help=settings.TYPER.TRANSLATE.help)(translate_command)
