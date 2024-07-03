def main():
    import typer
    import src.commands.builder.builder as builder

    app = typer.Typer()
    app.add_typer(builder.app, name='builder')

    app()


if __name__ == '__main__':
    main()
