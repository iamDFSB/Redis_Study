from dataclasses import dataclass
from typing import Callable

from interfaces import DatabaseServiceInterface

class FuncOptions:
    def __init__(self, data_source_setup: DatabaseServiceInterface):
        self.__get_operation: Callable = data_source_setup.get_value_by_key_operation
        self.__add_operation: Callable = data_source_setup.create_key_value_operation
        self.__update_operation: Callable = data_source_setup.update_value_operation

    def get_operations(self):
        return {
            "add": self.__add_operation,
            "get": self.__get_operation,
            "update": self.__update_operation
        }


@dataclass
class Command:
    command_name: str
    command_help: str


@dataclass
class Argument(Command):
    command_type: object

