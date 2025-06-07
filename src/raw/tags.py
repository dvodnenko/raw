import click

from .data import rewrite_data, get_tags


@click.command('tags')
@click.option('--new')
def tag(
    new: str
):

    mytags: list = get_tags()
    mytags = mytags if mytags else []

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
            exit(1)
    else:
        if mytags == []:
            click.echo('you do not have tags yet')
            click.echo('type "raw tags --new <NAME>" to add a new tag')
            exit(1)
        for tag in mytags:
            click.echo(f'* {tag}')
