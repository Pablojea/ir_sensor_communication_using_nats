import argument_parser
import asyncio
import logger
import nats
import numpy as np


async def main():

    async def message_handler(msg):
        data = msg.data.decode()
        nonlocal send
        if data == 'PAUSE' or data == 'R':
            send = False
            log.paused()
        if data == 'RESUME' or data == 'R':
            send = True
            log.resumed()


    log = logger.Logger()
    (sensor_type , interval, data_range) = argument_parser.parse()

    nats_conection = await nats.connect('nats://localhost:4222')
    sensor_control_sub = await nats_conection.subscribe("ir_sensor.control", cb=message_handler)
    rng = np.random.default_rng()

    send = True

    while True:

        if send and sensor_type == "mockup":
            data_package = rng.integers(low=data_range[0], high=data_range[1], size=(64), dtype=np.int16)
            data_string = np.array2string(data_package)
            log.data_sent(data_string)
            await nats_conection.publish('ir_sensor.data', data_string.encode('UTF-8'))

        elif send and sensor_type == "real":
            log.not_implemented()

        await asyncio.sleep(interval)


if __name__ == '__main__':
    asyncio.run(main())