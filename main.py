from email.policy import default
from sqlite3 import connect
import click
import os
import colorama


# from scripts import shell
from scripts import pen
from scripts import socail
from scripts import egg

@click.group()
def cli():
    pass

@cli.command()
def crack():
    """ See secret message for today """
    click.echo(egg.unlock())

@cli.command()
@click.argument('project')
def create():
    """ Generate boiler plate code """
    pass

@cli.command()
# @click.argument('platform')
@click.option('--platform', type=click.Choice(['facebook', 'twitter', 'instagram'], case_sensitive=False))
def connect(platform):
    """ Lookup codeplateau on social media """
    if(platform == 'facebook'):
        socail.connect('https://web.facebook.com/hashtag/codeplateau')
    if(platform == 'twitter'):
        socail.connect('https://twitter.com/search?q=%23codeplateau')
    if(platform == 'instagram'):
        socail.connect('https://www.instagram.com/explore/tags/codeplateau/')
        

    

cli.add_command(crack)
cli.add_command(create)
cli.add_command(connect)


if __name__ == '__main__':
    cli()