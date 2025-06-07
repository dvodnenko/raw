import click

from .data import rewrite_data, get_tags, get_sessions, get_active_session


@click.command('tags')
@click.option('--new')
def tag(
    new: str
):

    mytags = get_tags()

    if new:
        if new in mytags:
            click.echo(f'tag {new} already exists')
            exit(1)
        else:
            mysessions = get_sessions()
            active_session = get_active_session()

            new_data = {
                'tags': [*mytags, new],
                'active_session': active_session,
                'sessions': [*mysessions]
            }

            rewrite_data(new_data)
            click.echo(f'new tag - {new}')
            exit(0)
    else:
        if mytags == []:
            click.echo('you do not have tags yet')
            click.echo('type "raw tags --new <NAME>" to add a new tag')
            exit(1)
        for tag in mytags:
            click.echo(f'* {tag}')
