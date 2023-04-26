from dataclasses import field
from typing import ClassVar

from marshmallow import EXCLUDE
from marshmallow import Schema
from marshmallow_dataclass import dataclass


@dataclass
class MessageFrom:
    """Telegram API: https://core.telegram.org/bots/api#user"""
    id: int
    first_name: str
    last_name: str | None
    username: str | None

    class Meta:
        unknown = EXCLUDE


@dataclass
class Chat:
     """Telegram API: https://core.telegram.org/bots/api#chat"""
    id: int
    type: str
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    """Telegram API: https://core.telegram.org/bots/api#message"""
    message_id: int
    from_: MessageFrom = field(metadata={"data_key": "from"})
    chat: Chat
    text: str | None = None

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    """Telegram API: https://core.telegram.org/bots/api#getting-updates"""
    update_id: int
    message: Message

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    """https://core.telegram.org/bots/api#getupdates"""
    ok: bool
    result: list[UpdateObj]
    Schema: ClassVar[type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
     """https://core.telegram.org/bots/api#sendmessage"""
    ok: bool
    result: Message
    Schema: ClassVar[type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE
