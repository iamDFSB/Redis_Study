import sys
from typing import List
from pathlib import Path
from argparse import ArgumentParser

ABS_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(ABS_PATH))

from repositories import DatabaseRepository, RedisRepository, RedisConnectionHandle
from interfaces import DatabaseServiceInterface
from services.database_service import DatabaseService
from utils import SubParser, AddCommand, GetCommand, UpdateCommand, TerminalCommandInterface



class TerminalSetup:
    def __init__(self, database_service: DatabaseServiceInterface, commands: List[TerminalCommandInterface]) -> None:
        self.__database_service = database_service
        self.__commands = commands
        self.__parser = ArgumentParser()

    def __create_arguments(self):
        subparser = SubParser(parser=self.__parser, data_source_setup=self.__database_service)
        subparser.create_subparser(dest="command", required=True, help_text="Sub-commands")

        for command in self.__commands:
            command.build(subparser)

    def run(self):
        self.__create_arguments()
        args = self.__parser.parse_args()
        args.func(args)


if __name__ == "__main__":
    redis_conn = RedisConnectionHandle().connect()
    redis_repo = RedisRepository(redis_conn)
    db_repo = DatabaseRepository()
    data_source_setup = DatabaseService(
        redis_repo=redis_repo,
        db_repo=db_repo
    )
    commands = [
        AddCommand,
        GetCommand,
        UpdateCommand
    ]

    TerminalSetup(data_source_setup, commands).run()
