# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class Success(p.MessageType):
    MESSAGE_WIRE_TYPE = 2

    def __init__(
        self,
        message: str = None,
    ) -> None:
        self.message = message

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('message', p.UnicodeType, 0),
        }