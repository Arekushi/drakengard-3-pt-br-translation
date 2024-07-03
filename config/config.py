from pathlib import Path
from dynaconf import Dynaconf


settings = Dynaconf(
    settings_files=[
        './toml/settings.toml',
        './toml/cli.toml',
        './toml/typer.toml',
    ],
    load_dotenv=True,
    envvar_prefix=False
)

ROOT_DIR = Path(__file__).parent.parent
