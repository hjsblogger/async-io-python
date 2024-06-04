import asyncio
import sys

async def coroutine_1():
    await asyncio.sleep(2)
    raise ValueError(sys._getframe().f_code.co_name + " failed with ValueError")
    return("coroutine_1 finished.")

async def coroutine_2():
    await asyncio.sleep(2)
    return("coroutine_2 finished.")

async def coroutine_3():
    await asyncio.sleep(2)
    raise SystemError(sys._getframe().f_code.co_name + " failed with SystemError")
    return("coroutine_3 finished.")

async def coroutine_4():
    await asyncio.sleep(2)
    return("coroutine_4 finished.")

async def main(return_exceptions_val):
    try:
        results = await asyncio.gather(
            coroutine_1(), coroutine_2(), coroutine_3(), coroutine_4(),
            return_exceptions = return_exceptions_val
        )
        print(results)
    except ValueError as e:
        print("Value Error raised.")

print("Running with return_exceptions = False")
asyncio.run(main(return_exceptions_val = False))

print("\nRunning with return_exceptions = True")
asyncio.run(main(return_exceptions_val = True))