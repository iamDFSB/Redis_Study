from typing import List
from abc import ABC, abstractmethod
from argparse import ArgumentParser, _SubParsersAction
from models import FuncOptions, Argument, Command
from interfaces import DatabaseServiceInterface


class SubParser:
    def __init__(self, parser: ArgumentParser, data_source_setup: DatabaseServiceInterface) -> None:
        self.__parser = parser
        self.__data_source_setup = data_source_setup
        self.__subparser: _SubParsersAction = None
        self.__command_parser: ArgumentParser = None

    def create_subparser(self, dest: str, required: bool, help_text: str):
        self.__subparser = self.__parser.add_subparsers(dest=dest, required=required, help=help_text)

    def __create_command_parser(self, command: Command) -> None:
        self.__command_parser = self.__subparser.add_parser(
            command.command_name,
            help=command.command_help
        )

    def __create_command_argument(self, command: Argument) -> None:
        self.__command_parser.add_argument(
            command.command_name,
            help=command.command_help,
            type=command.command_type
        )

    def __bind_function_as_set_defaults(self, command_name: str):
        functions = FuncOptions(self.__data_source_setup).get_operations()
        self.__command_parser.set_defaults(func=functions.get(command_name))


    def build_commands(self, command_parser: Command, list_of_arguments: List[Argument]):
             
        self.__create_command_parser(command_parser)

        for command in list_of_arguments:
            self.__create_command_argument(command)

        self.__bind_function_as_set_defaults(command_parser.command_name)



class TerminalCommandInterface(ABC):
    @staticmethod
    @abstractmethod
    def build(subparser: SubParser) -> None: pass



class AddCommand(TerminalCommandInterface):
    @staticmethod
    def build(subparser: SubParser) -> None:
        # Create the add subparser
        add_operation_command = Command(command_name="add", command_help="Persist key-value data in Redis and DB")
        add_operation_arguments = [
            Argument(command_name="key", command_help="Set the key name", command_type=str),
            Argument(command_name="value", command_help="Set the key value", command_type=str),
        ]
    
        subparser.build_commands(
            command_parser=add_operation_command, 
            list_of_arguments=add_operation_arguments
        )



class GetCommand(TerminalCommandInterface):
    @staticmethod
    def build(subparser: SubParser) -> None:
        # Create the get subparser 
        get_operation_command = Command(command_name="get", command_help="Get the value data from Redis/DB")
        get_operation_arguments = [
            Argument(command_name="key", command_help="The key to be searched in Redis/DB", command_type=str),
        ]

        subparser.build_commands(
            command_parser=get_operation_command, 
            list_of_arguments=get_operation_arguments
        )


class UpdateCommand(TerminalCommandInterface):
    @staticmethod
    def build(subparser: SubParser) -> None:
        update_operation_command = Command(command_name="update", command_help="Change the key value to another")
        update_operation_arguments = [
            Argument(command_name="key", command_help="Set the key name", command_type=str),
            Argument(command_name="value", command_help="Set the new value for the key", command_type=str),
        ]

        subparser.build_commands(
            command_parser=update_operation_command, 
            list_of_arguments=update_operation_arguments
        )