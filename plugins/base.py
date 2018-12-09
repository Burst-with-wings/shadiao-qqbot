from none import on_command, CommandSession, permission as perm
from none.message import unescape
from none import on_natural_language, NLPSession
import random
from function.weather import query_weather


@on_command('echo', only_to_me=False)
async def echo(session: CommandSession):
    await session.send(session.get_optional('message') or session.current_arg)


@on_command('say', permission=perm.SUPERUSER)
async def _(session: CommandSession):
    await session.send(
        unescape(session.get_optional('message') or session.current_arg))


@on_command('inform', permission=perm.SUPERUSER)
async def inform(session: CommandSession):
    await session.send(session.get_optional('message') or session.current_arg)


@on_command('天气', only_to_me=False)
async def weather(session: CommandSession):
    info = (session.get_optional('message') or session.current_arg).split(' ')
    if len(info) == 1:
        await session.send(query_weather(info[0]))
    else:
        await session.send(query_weather(info[0], info[1]))


@on_natural_language()
async def repeat(session: NLPSession):
    i = random.random()-0.5
    msg = session.msg.strip("么吧吗?？")+("!" if i < 0 else '')
    await session.send(msg)
