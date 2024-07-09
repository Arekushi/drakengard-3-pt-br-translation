import typer
from config import settings

from .make_translation_folder import make_translation_folder_command
from .make_result_folder import make_result_folder_command
from .translate import translate_command
from .update_xxx_files import update_xxx_command


app = typer.Typer(
    help=settings.TYPER.BUILDER.help
)

app.command('make-translation-folder', help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help)(make_translation_folder_command)
app.command('make-result-folder', help=settings.TYPER.MAKE_RESULT_FOLDER.help)(make_result_folder_command)
app.command('translate', help=settings.TYPER.TRANSLATE.help)(translate_command)
app.command('update-xxx', help=settings.TYPER.UPDATE_XXX.help)(update_xxx_command)
