import asyncio
from aiokafka import AIOKafkaProducer


async def send_message():
    producer = AIOKafkaProducer(
        bootstrap_servers='kafka:29092',
    )

    await producer.start()

    try:
        await producer.send_and_wait('test-topic', b'Hello Kafka!')
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:

        await producer.stop()


asyncio.run(send_message())
