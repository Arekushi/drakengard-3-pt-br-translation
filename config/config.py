from pathlib import Path
from dynaconf import Dynaconf


settings = Dynaconf(
    settings_files=[
        './toml/cli.toml',
        './toml/typer.toml',
        './toml/llm.toml',
        './toml/settings.toml',
        './toml/.secrets.toml',
    ],
    load_dotenv=True,
    envvar_prefix=False
)

ROOT_DIR = Path(__file__).parent.parent
