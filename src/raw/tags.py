import click

from .data import rewrite_data, get_tags


@click.command('tags')
@click.option('--new')
def tag(
    new: str | None
):

    mytags: list = get_tags()

    if new:
        if new in mytags:
            click.echo(f'tag {new} already exists')
            exit(1)
        else:
            new_data = {
                'tags': [*mytags, new]
            }

            rewrite_data(new_data)
            click.echo(f'new tag - {new}')
    else:
        for tag in mytags:
                click.echo(f'* {tag}')
