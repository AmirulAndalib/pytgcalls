from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import filters as fl
from pytgcalls import PyTgCalls
from pytgcalls.types import ChatUpdate

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)
call_py = PyTgCalls(app)

test_stream = 'http://docs.evostream.com/sample_content/assets/' \
              'sintel1m720p.mp4'


@app.on_message(filters.regex('!call'))
async def play_handler(_: Client, message: Message):
    await call_py.play(
        message.chat.id,
        test_stream,
    )


@app.on_message(filters.regex('!hangup'))
async def stop_handler(_: Client, message: Message):
    await call_py.leave_call(
        message.chat.id,
    )


@call_py.on_update(fl.chat_update(ChatUpdate.Status.INCOMING_CALL))
async def incoming_handler(_: PyTgCalls, update: ChatUpdate):
    await call_py.mtproto_client.send_message(
        update.chat_id,
        'You are calling me!',
    )
    await call_py.play(
        update.chat_id,
        test_stream,
    )
call_py.run()
