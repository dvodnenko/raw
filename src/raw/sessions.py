from datetime import datetime

import click

from .data import rewrite_data, get_tags, get_active_session, get_sessions

@click.command()
@click.argument('tags', nargs=-1)
def b(tags: tuple):

    active_session = get_active_session()

    if active_session:
        click.echo('you already started a session')
        exit(1)

    if tags == ():
        click.echo('you should provide at least one tag to begin a session')
        exit(1)
    
    mytags = get_tags()
    sessions = get_sessions()

    for tag in tags:
        if tag not in mytags:
            click.echo(f'tag {tag} does not exist yet')
            exit(1)

    start_time = datetime.now()

    new_data = {
        'tags': [*mytags],
        'active_session': {
            'tags': [*tags],
            'start time': f'{start_time}'
        },
        'sessions': [*sessions]
    }

    rewrite_data(new_data)

    click.echo('session started')


@click.command()
def f():

    active_session = get_active_session()

    if not active_session:
        click.echo('you did not start a session yet')
        exit(1)

    mytags = get_tags()
    mysessions = get_sessions()

    print(len(mysessions))

    start_time = datetime.fromisoformat(active_session['start time'])
    end_time = datetime.now()
    timedelta = (end_time - start_time).seconds
    hours = timedelta // 3600
    timedelta -= hours*3600
    minutes = timedelta // 60
    timedelta -= minutes * 60
    seconds = timedelta

    total_time = {
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

    new_session = {
        'tags': [*(active_session.get('tags'))],
        'start time': f'{start_time}',
        'end time': f'{end_time}',
        'total time': total_time
    }

    new_data = {
        'tags': [*mytags],
        'active_session': {},
        'sessions': [*mysessions, new_session]
    }

    rewrite_data(new_data=new_data)

    click.echo('session finished')
    click.echo('')

