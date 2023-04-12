import asyncio
import os
from Wanderer import Wanderer

from dotenv import load_dotenv

load_dotenv(verbose=True)

SERVER_DATA = os.getenv('SERVERDATA')
DATABASE = os.getenv('DATABASE')

async def main():
    Wander = Wanderer()

asyncio.run(main())
