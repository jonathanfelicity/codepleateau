from app.shell import egg


import click
import colorama


@click.command()
def run():
    click.echo(egg())



if __name__ == '__main__':
    run()