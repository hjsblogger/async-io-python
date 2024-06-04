import asyncio
import sys
import time
from datetime import datetime

async def test_1():
    # Get function name
    # https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function
    print("Enter " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    # Could be an I/O operation, network request, database operation, and more
    await asyncio.sleep(2)
    print("After sleep " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    return "test_1"

async def test_2():
    print("Enter " + sys._getframe().f_code.co_name + " " + str(datetime.now().time()))
    # Sleep of 2 seconds
    await asyncio.sleep(2)
    print("Exit " + sys._getframe().f_code.co_name)
    return "test_2"

async def main():
    print("Enter main")
    start_time = time.perf_counter()
    # Await test_1
    ret_info = await test_1()
    print(f"Data received from the test_1: {ret_info}" + " " + str(datetime.now().time()))
    # Await test_2
    ret_info = await test_2()
    print(f"Data received from the test_2: {ret_info}" + " " + str(datetime.now().time()))
    print("Exit main")
    end_time = time.perf_counter()
    print(f'It took {round(end_time - start_time,0)} second(s) to complete.')

if __name__ == '__main__':
    # Explicitly create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()