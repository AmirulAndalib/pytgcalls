import asyncio

from ...exceptions import NodeJSNotRunning
from ...exceptions import NoMtProtoClientSet
from ...scaffold import Scaffold


class UnMuteStream(Scaffold):
    async def unmute_stream(
        self,
        chat_id: int,
    ):
        """UnMute the userbot

        This method allow to unmute the userbot via MtProto APIs

        Parameters:
            chat_id (``int``):
                Unique identifier (int) of the target chat.

        Raises:
            NoMtProtoClientSet: In case you try
                to call this method without any MtProto client
            NodeJSNotRunning: In case you try
                to call this method without do
                :meth:`~pytgcalls.PyTgCalls.start` before

        Example:
            .. code-block:: python
                :emphasize-lines: 10-12

                from pytgcalls import Client
                from pytgcalls import idle
                ...

                app = PyTgCalls(client)
                app.start()

                ...  # Call API methods

                app.unmute_stream(
                    -1001185324811,
                )

                idle()
        """
        if self._app is not None:
            if self._wait_until_run is not None:
                async def internal_sender():
                    if not self._wait_until_run.done():
                        await self._wait_until_run
                    await self._binding.send({
                        'action': 'unmute_stream',
                        'chat_id': chat_id,
                    })

                asyncio.ensure_future(internal_sender())
            else:
                raise NodeJSNotRunning()
        else:
            raise NoMtProtoClientSet()
