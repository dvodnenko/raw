from importlib.metadata import version

import click

from .tags import tag


@click.command('version')
def show_version():
    v = version('raw')

    click.echo(f'raw {v}')


@click.group()
def raw():
    ...


raw.add_command(tag)
raw.add_command(show_version)
