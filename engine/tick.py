import asyncio
import logging

logger = logging.getLogger(__name__)


async def tick_loop():
    tick_number = 0
    while True:
        tick_number += 1
        logger.info(f'=== URF TICK {tick_number} ===')
        await asyncio.sleep(60 * 60)
