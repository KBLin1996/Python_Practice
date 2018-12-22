<<<<<<< HEAD
#Reference: https://click.palletsprojects.com/en/5.x/

=======
>>>>>>> 6c0f2ac9e9987c681b3f2f51731e1b7cfea08da5
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')

def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
