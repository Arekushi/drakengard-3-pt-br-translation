def main():
    import typer
    import nest_asyncio
    import src.commands.builder.builder as builder
    import src.commands.manager.manager as manager

    app = typer.Typer()
    app.add_typer(manager.app, name='manager')
    app.add_typer(builder.app, name='builder')

    nest_asyncio.apply()
    app()


if __name__ == '__main__':
    main()
