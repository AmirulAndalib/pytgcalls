from ...types.update import Update


class JoinedVoiceChat(Update):
    """The userbot joined to the Group Call

    Attributes:
        chat_id (``int``):
            Unique identifier of chat.

    Parameters:
        chat_id (``int``):
            Unique identifier of chat.
    """

    def __init__(
        self,
        chat_id: int,
    ):
        super().__init__(chat_id)
