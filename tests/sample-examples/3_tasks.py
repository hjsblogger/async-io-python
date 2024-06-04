import asyncio
import sys
import time
from datetime import datetime

async def test_1():
    print("Enter " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    await asyncio.sleep(2)
    print("After sleep " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    return "test_1"

async def test_2():
    print("Enter " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    await asyncio.sleep(2)
    print("Exit " + sys._getframe().f_code.co_name)
    return "test_2"

async def main():
    print("Enter main")
    start_time = time.perf_counter()

    # Create tasks for concurrent execution
    task1 = asyncio.create_task(test_1())
    task2 = asyncio.create_task(test_2())

    # Await both tasks
    ret_info_1 = await task1
    print(f"Data received from test_1: {ret_info_1} " + str(datetime.now().time()))
    ret_info_2 = await task2
    print(f"Data received from test_2: {ret_info_2} " + str(datetime.now().time()))

    print("Exit main")
    end_time = time.perf_counter()
    print(f'It took {round(end_time - start_time, 0)} second(s) to complete.')

if __name__ == '__main__':
    # Run the main coroutine
    asyncio.run(main())