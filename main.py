import nest_asyncio


def main():
    import typer
    import src.commands.builder.builder as builder

    app = typer.Typer()
    app.add_typer(builder.app, name='builder')

    nest_asyncio.apply()
    app()


if __name__ == '__main__':
    main()
