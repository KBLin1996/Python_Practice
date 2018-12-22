import click

# The most basic option is a simple string argument of one value. If no type is provided, the type of the default value is used, and if no default value is provided, the type is assumed to be STRING.

@click.command()
@click.argument('filename') # The string that user types will be stored at a string variable called 'filename'

def argu(filename):
    click.echo('string variable "filename" has been stored as: %s' % filename)


# Variadic Arguments (Variadic == Changeable)

@click.command()
# The second most common version is variadic arguments where a specific (or unlimited) number of arguments is accepted. This can be controlled with the nargs parameter. If it is set to -1, then an unlimited number of arguments is accepted.
@click.argument('src', nargs=-1) # nargs=-1 means 'src' can have multiple strings
@click.argument('dst', nargs=1) # nargs=1 means 'dst' has only one string

def changeable_variable(src, dst):
    for fn in src:
        click.echo('move %s to folder %s' % (fn, dst))

# Example:
# $ python click_argument.py foo.txt bar.txt log.txt my_folder
#   move foo.txt to folder my_folder
#   move bar.txt to folder my_folder
#   move log.txt to folder my_folder


if __name__ == '__main__':
    argu()
    # changeable_variable()
