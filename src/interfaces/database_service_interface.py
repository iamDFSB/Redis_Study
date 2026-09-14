from abc import ABC, abstractmethod

class DatabaseServiceInterface(ABC):
    @abstractmethod
    def create_key_value_operation(self, args) -> None: pass

    @abstractmethod
    def get_value_by_key_operation(self, args) -> None: pass

    @abstractmethod
    def update_value_operation(self, args) -> None: pass