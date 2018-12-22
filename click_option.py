# Reference: https://click.palletsprojects.com/en/5.x/options/

import sys
import click
import codecs # For using 'rot-13'


# 1. Click Boolean Flags

@click.command()
# Boolean flags are options that can be enabled or disabled. This can be accomplished by defining two flags in one go separated by a slash (/) for enabling or disabling the option.
@click.option('--shout/--no-shout', default=False) # False means the latter option (True/False)

def boolean(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!'
    click.echo(rv)


# 2. Click Choice

# To notice user to type correct options (If not, pop an error message and tell user to type correct options)
@click.command()
@click.option('--gender', type=click.Choice(['man', 'woman'])) # Options

def choose(gender):
    click.echo('gender: %s' % gender)


# 3. Feature Switches

@click.command()
# Note that by providing the flag_value parameter, Click will implicitly set is_flag=True.
@click.option('--upper', 'transformation', flag_value='upper', default=True)
@click.option('--lower', 'transformation', flag_value='lower')

def switch(transformation):
    click.echo(getattr(sys.platform, transformation)())


# 4. Counting

@click.command()
@click.option('-c', '--verbose', count=True) # count=True means it's initialized to 0
                                             # -cccc -> Verbosity: 4
def counting(verbose):
    click.echo('Verbosity: %s' % verbose)


# 5. Choice Options

@click.command()
# Sometimes, you want to have a parameter be a choice of a list[] of values. In that case you can use Choice type. It can be instantiated with a list of valid values.
@click.option('--type', type=click.Choice(['a', 'b', 'c']))

def choice(type):
    click.echo(click.style('%s is your choice !' % type, fg='red'))


# 6. Prompt

@click.command()
# In some cases, you want parameters that can be provided from the command line, but if not provided, ask for user input instead.
@click.option('--name', prompt=True) # prompt=True -> name:  or  prompt is availible to give a string, Ex: prompt='What's your name?'

def hello(name):
    click.echo('Hello %s!' % name)


# 7. Password Prompts

@click.command()
# Click also supports hidden prompts and asking for confirmation.
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True) # Can be replaced by @click.password_option()

def pwd(password):
    convert = codecs.getencoder("rot-13") # Reference: https://www.wefearchange.org/2012/01/python-3-porting-fun-redux.html
    click.echo('Encrypting password to %s' % convert(password)[0])


# 8. Range Options

@click.command()
@click.option('--count', type=click.IntRange(0, 20, clamp=True)) # An optional clamping mode where a value that falls outside of the range will be clamped. Ex: range of 0~5 return 5 for the value 10, return 0 for the value -1
@click.option('--digit', type=click.IntRange(0, 10)) # The default mode (non-clamping mode) where a value that falls outside of the range will cause an error

def range_repeat(count, digit):
    click.echo(str(digit) * count)


if __name__ == '__main__':
    # boolean()
    choose()
    # switch()
    # counting()
    # choice()
    # hello()
    # pwd()
    # range_repeat()
