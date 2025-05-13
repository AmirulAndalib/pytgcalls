from enum import auto
from enum import Flag

from ..chats import GroupCallParticipant
from ..update import Update


class UpdatedGroupCallParticipant(Update):
    class Action(Flag):
        JOINED = auto()
        LEFT = auto()
        UPDATED = auto()

    def __init__(
        self,
        chat_id: int,
        action: Action,
        participant: GroupCallParticipant,
    ):
        super().__init__(chat_id)
        self.action = action
        self.participant = participant
