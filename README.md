# ir_sensor_communication_using_nats
Python software developer evaluation task


# basic information
NATS server: 'nats://localhost:4222'
Data is sent to the NATS subject 'ir_sensor.data'
Instructions will be received in the NATS subject 'ir_sensor.control'

# how to use
usage: main.py [-h] [-t {mockup,real}] [-i INTERVAL] [-r RANGE RANGE]

options:
  -h, --help            show this help message and exit
  -t {mockup,real}, --type {mockup,real}
                        Specifies weather the sensor values are randomly generated or come from
                        a real sensor
  -i INTERVAL, --interval INTERVAL
                        Time elapsed between sensor data packages sent. Type = float
  -r RANGE RANGE, --range RANGE RANGE
                        Minimun and maximum values that can be generated by the mockup sensor.
                        Must receive 2 int values