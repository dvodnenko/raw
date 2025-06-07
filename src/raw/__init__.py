from importlib.metadata import version

import click

from .tags import tag
from .sessions import b, f


@click.command('version')
def show_version():
    v = version('raw')

    click.echo(f'raw {v}')


@click.group()
def raw():
    ...


## commands ##

# std 
raw.add_command(show_version)

# tags
raw.add_command(tag)

# sessions
raw.add_command(b, name='b')
raw.add_command(b, name='s')
raw.add_command(f)
