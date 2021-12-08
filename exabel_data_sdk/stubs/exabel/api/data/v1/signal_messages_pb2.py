# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exabel/api/data/v1/signal_messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from exabel_data_sdk.stubs.exabel.api.math import aggregation_pb2 as exabel_dot_api_dot_math_dot_aggregation__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exabel/api/data/v1/signal_messages.proto',
  package='exabel.api.data.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.exabel.api.data.v1B\023SignalMessagesProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(exabel/api/data/v1/signal_messages.proto\x12\x12\x65xabel.api.data.v1\x1a!exabel/api/math/aggregation.proto\x1a\x1fgoogle/api/field_behavior.proto\"\xd5\x01\n\x06Signal\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0\x41\x05\xe0\x41\x02\x12\x17\n\x0b\x65ntity_type\x18\x02 \x01(\tB\x02\x18\x01\x12\x19\n\x0c\x64isplay_name\x18\x03 \x01(\tB\x03\xe0\x41\x02\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x39\n\x13\x64ownsampling_method\x18\x05 \x01(\x0e\x32\x1c.exabel.api.math.Aggregation\x12\x16\n\tread_only\x18\x06 \x01(\x08\x42\x03\xe0\x41\x03\x12\x19\n\x0c\x65ntity_types\x18\x07 \x03(\tB\x03\xe0\x41\x03\x42/\n\x16\x63om.exabel.api.data.v1B\x13SignalMessagesProtoP\x01\x62\x06proto3'
  ,
  dependencies=[exabel_dot_api_dot_math_dot_aggregation__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,])




_SIGNAL = _descriptor.Descriptor(
  name='Signal',
  full_name='exabel.api.data.v1.Signal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='exabel.api.data.v1.Signal.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='exabel.api.data.v1.Signal.entity_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='exabel.api.data.v1.Signal.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='exabel.api.data.v1.Signal.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downsampling_method', full_name='exabel.api.data.v1.Signal.downsampling_method', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_only', full_name='exabel.api.data.v1.Signal.read_only', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_types', full_name='exabel.api.data.v1.Signal.entity_types', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=346,
)

_SIGNAL.fields_by_name['downsampling_method'].enum_type = exabel_dot_api_dot_math_dot_aggregation__pb2._AGGREGATION
DESCRIPTOR.message_types_by_name['Signal'] = _SIGNAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Signal = _reflection.GeneratedProtocolMessageType('Signal', (_message.Message,), {
  'DESCRIPTOR' : _SIGNAL,
  '__module__' : 'exabel.api.data.v1.signal_messages_pb2'
  # @@protoc_insertion_point(class_scope:exabel.api.data.v1.Signal)
  })
_sym_db.RegisterMessage(Signal)


DESCRIPTOR._options = None
_SIGNAL.fields_by_name['name']._options = None
_SIGNAL.fields_by_name['entity_type']._options = None
_SIGNAL.fields_by_name['display_name']._options = None
_SIGNAL.fields_by_name['read_only']._options = None
_SIGNAL.fields_by_name['entity_types']._options = None
# @@protoc_insertion_point(module_scope)
