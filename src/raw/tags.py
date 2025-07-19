import click

from .data import Data


@click.command("tags")
@click.option("--new", default="")
@click.pass_context
def tag(
    ctx: click.Context,
    new: str
):

    if new == "":
        new = []
    else:
        new = new.split(",")

    raw_directory = ctx.obj["raw_directory"]
    data = Data(raw_directory)
    mytags = data.tags

    if new:
        for newtag in new:
            if newtag in mytags:
                click.echo(f"🦇 Tag '{newtag}' already exists")
            else:
                data.tags = [*data.tags, newtag]
                click.echo(f"🦇 New tag - {newtag}")
    else:
        if mytags == []:
            click.echo("🦇 Your tag list is empty right now")
            exit(1)
        for tag in mytags:
            click.echo(f"* {tag}")
