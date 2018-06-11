import click


@click.group()
def generate():
    pass


@generate.command()
def server():
    pass


@generate.command()
def client():
    pass


@generate.command()
def types():
    pass

