import asyncio
import random
import time
import numpy as np
import os
import sys

import RedisAdapter
from exampleDevice import Device

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

async def main():

    # Create a DeliveryRingBpmDigitizer object
    device = Device('LINAC:BCM', 'bidaqt')
    await device.initialize()
    
  
    #Open your file and dump data to a numpy array
    print(f"Data Parsing")


    # Generate Gaussian noise
    numpy_data = np.random.normal().astype(np.float32)



#Data from 1 generator
    stream_key = f"{device.base_key}:RAW_DATA"
    stream_key_noise = f"{device.base_key}:RAW_DATA_NOISE"

    binary_field = '_'
    data_type_field = 'TYPE'
    data_type = 'INT16'

    # Stream the data to Redis key base_key:DMA_DATA
    data_point_raw = {binary_field: numpy_data, data_type_field: data_type}
    data_point_noise = {binary_field: numpy_data, data_type_field: data_type}
    
    await device.redis_adapter.streamAdd(stream_key, data_point_raw, maxlen=10)
    await device.redis_adapter.streamAdd(stream_key_noise, data_point_noise, maxlen=10)




if __name__ == "__main__":
    asyncio.run(main())