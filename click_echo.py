import click

# click.echo() v.s print() -> 1. echo() has no return value, print has return value (1)
#                             2. echo() can be called consecutively but print() can't
#                                Ex: echo('a')('b')('c')
#                             3. echo() is slightly faster than print()
#                             4. echo() does not exist in python (but click.echo does)

variable = 100
click.echo('The value of variable is: %d' % variable) # Using '%' before the variable you want to echo(print)

# It will emit a trailing newline by default, which can be suppressed by passing nl=False
click.echo('Newline = False  ', nl=False)

# click_secho() == click.echo(click.style())
click.secho('Hello World!', fg='green') #fg = foreground
click.secho('Some more text', bg='blue', fg='white') # bg = background
click.secho('ATTENTION', blink=True, bold=True)


@click.command() # Make a function to be an input command window

# In some situations, you might want to show long texts on the terminal and let a user scroll through it. This can be achieved by using the echo_via_pager() function which works similarly to the echo() function, but always writes to stdout and, if possible, through a pager.
def scroll():
    click.echo_via_pager('\n'.join('Line %d' % idx for idx in range(200)))

#if __name__ == '__main__':
#   scroll()
