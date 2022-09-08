import click
import os
import colorama


# from scripts import shell
from app import pen
from app import socail
# from scripts import egg

@click.group()
def cli():
    pass

# @cli.command()
# def crack():
#     """ See secret message for today """
#     click.echo(egg.unlock())

@cli.command()
@click.option('--project', '-p', required=True, help="Project name")
def create(project):
    """ Generate boiler plate code """
    type = click.prompt("Pick project type", type=click.Choice(['java', 'c++', 'web', 'c', 'python']), show_default=False)
    pen.write(project, type)
    

@cli.command()
def connect():
    """ Lookup codeplateau on social media """
    platform = click.prompt('Select ', type=click.Choice(['facebook', 'twitter', 'instagram'], case_sensitive=False))

    if(platform == 'facebook'):
        socail.connect('https://web.facebook.com/hashtag/codeplateau')
    if(platform == 'twitter'):
        socail.connect('https://twitter.com/search?q=%23codeplateau')
    if(platform == 'instagram'):
        socail.connect('https://www.instagram.com/explore/tags/codeplateau/')
        

    

# cli.add_commancld(crack)
cli.add_command(create)
cli.add_command(connect)


if __name__ == '__main__':
    cli()