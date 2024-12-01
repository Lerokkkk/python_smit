from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.entites.log import LogEntity


@dataclass
class BaseAsyncLoggerService(ABC):

    @abstractmethod
    async def send_logs(self, log: LogEntity):
        ...
