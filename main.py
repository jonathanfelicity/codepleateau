from email.policy import default
from pydoc import cli
import click
import colorama


from scripts import shell


@click.command()
def start():
    click.echo(shell.egg())


if __name__ == '__main__':
    start()