import argparse
def parse() -> (str, int, []):

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type',
                        choices=['mockup', 'real'],
                        default='mockup',
                        help="Specifies weather the sensor values are randomly generated or come from a real sensor")

    parser.add_argument('-i', '--interval',
                        type=float,
                        default=2.0,
                        help="Time elapsed between sensor data packages sent")

    parser.add_argument('-r', '--range',
                        type=int,
                        nargs=2,
                        default=[0, 50],
                        help="Minimun and maximum values that can be generated by the mockup sensor")

    args = parser.parse_args()

    print("Starting application  with following configuration:")
    print(f"sensor_type: {args.type}")
    print(f"interval: {args.interval}")
    print(f"sensor_range: {args.range}")

    return (args.type, args.interval, args.range)