# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fib.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fib.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tfib.proto\"\x1b\n\nFibRequest\x12\r\n\x05order\x18\x01 \x01(\x03\"\x1c\n\x0b\x46ibResponse\x12\r\n\x05value\x18\x01 \x01(\x03\x32\x35\n\rFibCalculator\x12$\n\x07\x43ompute\x12\x0b.FibRequest\x1a\x0c.FibResponseb\x06proto3'
)




_FIBREQUEST = _descriptor.Descriptor(
  name='FibRequest',
  full_name='FibRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='order', full_name='FibRequest.order', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=13,
  serialized_end=40,
)


_FIBRESPONSE = _descriptor.Descriptor(
  name='FibResponse',
  full_name='FibResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='FibResponse.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=42,
  serialized_end=70,
)


DESCRIPTOR.message_types_by_name['FibRequest'] = _FIBREQUEST
DESCRIPTOR.message_types_by_name['FibResponse'] = _FIBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FibRequest = _reflection.GeneratedProtocolMessageType('FibRequest', (_message.Message,), {
  'DESCRIPTOR' : _FIBREQUEST,
  '__module__' : 'fib_pb2'
  # @@protoc_insertion_point(class_scope:FibRequest)
  })
_sym_db.RegisterMessage(FibRequest)

FibResponse = _reflection.GeneratedProtocolMessageType('FibResponse', (_message.Message,), {
  'DESCRIPTOR' : _FIBRESPONSE,
  '__module__' : 'fib_pb2'
  # @@protoc_insertion_point(class_scope:FibResponse)
  })
_sym_db.RegisterMessage(FibResponse)



_FIBCALCULATOR = _descriptor.ServiceDescriptor(
  name='FibCalculator',
  full_name='FibCalculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=72,
  serialized_end=125,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='FibCalculator.Compute',
    index=0,
    containing_service=None,
    input_type=_FIBREQUEST,
    output_type=_FIBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FIBCALCULATOR)

DESCRIPTOR.services_by_name['FibCalculator'] = _FIBCALCULATOR

# @@protoc_insertion_point(module_scope)
