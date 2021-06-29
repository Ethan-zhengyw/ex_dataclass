# -*- coding: utf-8 -*-

from ex_dataclass import ex_dataclass, field
import typing


@ex_dataclass
class MsgReqContentText(object):
    text: str = field(default_factory=str)


@ex_dataclass
class MsgReqContentPostTagText(object):
    text: str = field(default_factory=str)
    un_escape: bool = field(default_factory=bool)


@ex_dataclass
class MsgReqContentPostTagA(object):
    text: str = field(default_factory=str)
    href: str = field(default_factory=str)


@ex_dataclass
class MsgReqContentPostTagAt(object):
    user_id: str = field(default_factory=str)
    user_name: str = field(default_factory=str)


@ex_dataclass
class MsgReqContentPostLang(object):
    title: str = field(default_factory=str)
    content: typing.List[typing.List[
        typing.Union[MsgReqContentPostTagText,
                     MsgReqContentPostTagA,
                     MsgReqContentPostTagAt]]] = field(default_factory=typing.List)


@ex_dataclass
class MsgReqContentPost(object):
    zh_cn: MsgReqContentPostLang = field(default_factory=MsgReqContentPostLang)
    en_us: MsgReqContentPostLang = field(default_factory=MsgReqContentPostLang)


@ex_dataclass
class MsgReq(object):
    receive_id: str = field(default_factory=str)
    msg_type: str = field(default_factory=str)
    content: typing.Union[MsgReqContentText, MsgReqContentPost] = field(default_factory=MsgReqContentText)
