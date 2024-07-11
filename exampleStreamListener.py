import asyncio
import os
import sys
import time
import numpy as np

import RedisAdapter
from exampleDevice import Device

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)


async def main(base_key, redis_host):
    # Initialize the device
    device = Device(base_key, redis_host)
    await device.initialize()

    error_counter = 0
    while True:
        try:
            await device.runDeviceDataflow(f"MY_DATA_STREAM_SUBKEY")
        except Exception as e:
            print(f"An error occurred: {e}" )
            print("Restarting in 5 seconds...")
            error_counter += 1

            if error_counter > 10:
                print("Too many errors. Exiting.")
                break
            else:
                "Restarting in 5 seconds..."
                await asyncio.sleep(5)

    print("Device Dataflow exited.")

if __name__ == "__main__":

    redis_host = None
    base_key = None

    # Check if arguments are provided via command line or environment variables
    if len(sys.argv) == 3:
        redis_host = sys.argv[1]
        base_key = sys.argv[2]
    else:
        base_key = os.getenv('DEVICE_BASE_KEY')
        redis_host = os.getenv('REDIS_HOST')

    # Check if all required pieces of information are available
    if base_key is None or redis_host is None:
        print("Missing required information. Please provide the REDIS_HOST and DEVICE_BASE_KEY as arguments or environment")
        print("Usage: python exampleStreamListener.py  <REDIS_HOST> <DEVICE_BASE_KEY> or set input as an environment variable.")
        exit(1)
    else:
        print(f"REDIS_HOST: {redis_host}", flush=True)
        print(f"DEVICE_BASE_KEY: {base_key}", flush=True)

    asyncio.run(main(base_key, redis_host))

