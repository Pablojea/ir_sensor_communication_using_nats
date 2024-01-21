import argument_parser
import asyncio
import logger
import nats
import numpy as np


async def main():

    async def message_handler(msg):
        '''Callback function that gets triggered when a message is received
        in the ir_sensor.control subscription.
        The content of the payload will prevent/allow the sensor
        to keep publishing data
        '''
        data = msg.data.decode()
        nonlocal send_data
        if data == 'PAUSE' or data == 'P':
            send_data = False
            log.paused()
        if data == 'RESUME' or data == 'R':
            send_data = True
            log.resumed()


    log = logger.Logger()
    (sensor_type , interval, data_range) = argument_parser.parse()

    # NATS connection to server
    nats_conection = await nats.connect('nats://localhost:4222')

    # Subscription to the sensor control subjet were instructions will be received
    sensor_control_sub = await nats_conection.subscribe("ir_sensor.control", cb=message_handler)

    # Random number generator instance to be used by the mockup sensor
    rng = np.random.default_rng()

    # If True the sensor will send data at ceretain frequency, if false no data will be sent
    send_data = True


    # Main loop
    while True:

        # Sensor type will determine what kind of data will be sent to ir_sensor.data subject
        if send_data and sensor_type == "mockup":
            # Generates a list of 64 random int16
            data_package = rng.integers(low=data_range[0], high=data_range[1], size=(64), dtype=np.int16)
            data_string = np.array2string(data_package)
            log.data_sent(data_string)
            # Sends the list of int16 to ir_sensor.data subject
            await nats_conection.publish('ir_sensor.data', data_string.encode('UTF-8'))

        elif send_data and sensor_type == "real":
            log.not_implemented()

        # Waits the specified time before sending the next data package
        await asyncio.sleep(interval)


if __name__ == '__main__':
    asyncio.run(main())