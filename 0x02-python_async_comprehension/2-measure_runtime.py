#!/usr/bin/env python3
'''Run time for four parallel comprehensions.
'''
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executing async_comprehension 4 times and measure
    total execution time.
    '''
    start_time = time.time() # Start timing

    # Run async_comprehension four times concurrrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    return end_time - start_time
