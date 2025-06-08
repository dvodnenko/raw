from importlib.metadata import version

import click

from .tags import tag
from .sessions import begin_session, finish_session, pause_session


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
raw.add_command(begin_session, name='b')
raw.add_command(begin_session, name='s') # s - means "start"
raw.add_command(finish_session, name='f')
raw.add_command(pause_session, name='p')
