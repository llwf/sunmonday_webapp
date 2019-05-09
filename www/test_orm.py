import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='sunmonday', password='password', db='sunmonday')

    u = User(name='Test1', email='llwf@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop=asyncio.get_event_loop() 
loop.run_until_complete(test(loop))
loop.close()

