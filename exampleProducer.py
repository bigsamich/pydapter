import asyncio
import random
import time
import numpy as np
import os
import sys

import RedisAdapter

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

async def main():

    # Create a DeliveryRingBpmDigitizer object
    digitizer = Device('10.200.22.10', '../../config/bpm_config.json')
    await digitizer.initialize()
    
    # Generate an array of 1000 floats
    start_time = time.time()
    # Define the repeating sequence
    repeating_sequence = np.array([1000., 1000., 2000., 2000., 3000., 3000., 4000., 4000.], dtype=np.float32)
    # Repeat the sequence to achieve a total size of 400,000
    data_array = np.tile(repeating_sequence, 50000)


    # Specify noise parameters
    noise_mean = 0
    noise_std_dev = 10  # Adjust this value based on the desired noise level

    print(f"Data array generation time {(time.time() - start_time) * 1000:.3f} miliseconds.")

    while(True):
        start_time = time.time()
        # Generate Gaussian noise
        noise = np.random.normal(noise_mean, noise_std_dev, data_array.shape).astype(np.float32)

        # Add noise to the data_array
        noisy_data_array = data_array + noise
        #print(f"Size of noisy_data_array: {noisy_data_array.size} floats.")

        # Stream the data to Redis key base_key:DMA_DATA
        await digitizer.redis_adapter.streamAdd(f"{digitizer.base_key}:DMA_DATA", {'_': noisy_data_array}, maxlen=100)
        print(f"Stream loop time {(time.time() - start_time) * 1000:.3f} miliseconds.")

        # Sleep for 5 second
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())