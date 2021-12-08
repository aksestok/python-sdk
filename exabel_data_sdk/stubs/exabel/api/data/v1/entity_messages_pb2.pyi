"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class EntityType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    display_name: typing___Text = ...
    description: typing___Text = ...
    read_only: builtin___bool = ...
    is_associative: builtin___bool = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        display_name : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        read_only : typing___Optional[builtin___bool] = None,
        is_associative : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"display_name",b"display_name",u"is_associative",b"is_associative",u"name",b"name",u"read_only",b"read_only"]) -> None: ...
type___EntityType = EntityType

class Entity(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    display_name: typing___Text = ...
    description: typing___Text = ...
    read_only: builtin___bool = ...

    @property
    def properties(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        display_name : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        read_only : typing___Optional[builtin___bool] = None,
        properties : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"properties",b"properties"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"display_name",b"display_name",u"name",b"name",u"properties",b"properties",u"read_only",b"read_only"]) -> None: ...
type___Entity = Entity
