import click

from .tags import tag


@click.group()
def raw():
    ...


raw.add_command(tag)
