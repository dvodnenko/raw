import click

from .data import Data, Tag


@click.command('tags')
@click.option('--new', default='')
@click.pass_context
def tag(
    ctx: click.Context,
    new: str
):

    if new == '':
        new = []
    else:
        new = new.split(',')

    raw_directory = ctx.obj['raw_directory']
    data = Data(raw_directory)
    mytags = []
    for t in data.tags:
        mytags.append(t.title)

    if new:
        for newtag in new:
            if newtag in mytags:
                click.echo(f'🦇 tag {newtag} already exists')
            else:
                newtag_instance = Tag(title=newtag)
                data.tags = [*data.tags, newtag_instance]
                click.echo(f'🦇 new tag - {newtag}')
    else:
        if mytags == []:
            click.echo('🦇 your tag list is empty right now')
            exit(1)
        for tag in mytags:
            click.echo(f'* {tag}')
