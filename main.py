import sys
import typer
import nest_asyncio
import src.commands.manager.manager as manager


def main():
    app = typer.Typer()
    app.add_typer(manager.app, name='manager')
    
    if not getattr(sys, 'frozen', False):
        import src.commands.builder.builder as builder
        app.add_typer(builder.app, name='builder')

    nest_asyncio.apply()
    app()


if __name__ == '__main__':
    main()
