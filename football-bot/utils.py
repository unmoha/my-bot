import hashlib
import asyncio

def hash_text(title, summary):
    return hashlib.md5(f"{title}{summary}".lower().encode()).hexdigest()

async def retry(func, retries=3):
    for i in range(retries):
        try:
            return await func()
        except:
            if i == retries - 1:
                raise
            await asyncio.sleep(2 * (i + 1))