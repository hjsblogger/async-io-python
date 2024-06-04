import asyncio
import sys
import time
from datetime import datetime

async def coroutine_1():
    print("Enter asyncio.gather " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    await asyncio.sleep(2)
    print("After sleep " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    return "coroutine_1"

async def coroutine_2():
    print("Enter asyncio.gather " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    await asyncio.sleep(2)
    print("After sleep " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    return "coroutine_2"

async def main():
    print("Enter main")
    start_time = time.perf_counter()
    
    # Use asyncio.gather to run test_1 and test_2 concurrently
    ret_info_1, ret_info_2 = await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        return_exceptions = True
    )
    
    print(f"[asyncio.gather] Data received from coroutine_1: {ret_info_1} " + str(datetime.now().time()))
    print(f"[asyncio.gather] Data received from coroutine_2: {ret_info_2} " + str(datetime.now().time()))
    print("Exit main")
    
    end_time = time.perf_counter()
    print(f'It took {round(end_time - start_time, 0)} second(s) to complete.')

if __name__ == '__main__':
    asyncio.run(main())