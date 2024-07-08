#!/usr/bin/env python3
'''takes in an integer argument (max_delay,
with a default value of 10'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''wait random'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
