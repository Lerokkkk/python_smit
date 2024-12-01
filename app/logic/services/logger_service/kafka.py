import json

from aiokafka import AIOKafkaProducer
from domain.entites.log import LogEntity
from logic.services.logger_service.base import BaseAsyncLoggerService


class KafkaLoggingService(BaseAsyncLoggerService):
    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def send_logs(self, log: LogEntity):
        message = {
            'user_id': log.user_id,
            'action': log.action,
            'timestamp': log.timestamp.isoformat()
        }
        serialized_message = json.dumps(message).encode("utf-8")

        try:
            await self.producer.send(topic='my-topic', value=serialized_message)
        except Exception as e:
            raise e
