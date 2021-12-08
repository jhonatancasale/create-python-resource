#!/usr/bin/env python3
"""
    A lazy way to create a virtualenv and a folder

    Example usage
        {{ script }} create --resource <book|course> --provider <[oreilly|lynda|udemy]> --name <name>
        {{ script }} create --resource <project> --name <name>
"""


from os import environ
from subprocess import run

import click


def plural(singular: str) -> str:
    plural_map = {
        'book': 'books',
        'course': 'courses'
    }

    return plural_map[singular]


class Command:
    def __init__(self, command: str):
        self.__command = command

    def __str__(self):
        return f"Command({self.command}!r)"

    @property
    def command(self):
        return self.__command

    def run(self):
        run(self.command, shell=True, check=True)


@click.group()
def parse_cli():
    pass

@parse_cli.command(name='create')
@click.option("--resource", required=True, help='The resource that will be created')
@click.option("--name", required=True, help='The name of the resource')
@click.option("--provider", required=False, help='One out from [oreilly, lynda, udemy]')
def create_resource(name, resource, provider):
    venvs_workspace = f'{environ["WORKSPACE"]}/virtualenvs'
    python_playground = f'{environ["PYTHON_PLAYGROUND"]}'

    print(venvs_workspace)
    print(python_playground)
    print('method create', name, resource, provider)

    command = Command(f"mkdir -p {python_playground}/{plural(resource)}/{provider}/{name}")
    command.run()

    command = Command(f"virtualenv --python=python3 {venvs_workspace}/{plural(resource)}/{provider}/{name}")
    command.run()

def main() -> None:
    parse_cli()


if __name__ == "__main__":
    main()
