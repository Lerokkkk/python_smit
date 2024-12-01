from functools import lru_cache
from punq import Container, Scope
from aiokafka import AIOKafkaProducer


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    def init_kafka_producer():
        return AIOKafkaProducer(
            bootstrap_servers="kafka:29092",
            max_batch_size=512,
            linger_ms=100

        )

    container.register(AIOKafkaProducer, factory=init_kafka_producer, scope=Scope.singleton)

    return container
