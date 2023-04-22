#!/usr/bin/env python3
'''Run time for four parallel comprehensions.
'''
import time
import asyncio
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executing async_comprehension 4 times and measure
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
