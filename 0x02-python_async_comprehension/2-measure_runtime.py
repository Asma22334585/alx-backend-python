#!/usr/bin/env python3
""" Task2 """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    start = time.perf_counter()
    asycomp = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*asycomp)
    end = time.perf_counter()

    return (end - start)
