# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/appengine_legacy/proto/audit_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/appengine_legacy/proto/audit_data.proto',
  package='google.appengine.legacy',
  syntax='proto3',
  serialized_options=b'\n\033com.google.appengine.legacyB\016AuditDataProtoP\001Z=google.golang.org/genproto/googleapis/appengine/legacy;legacy',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4google/cloud/appengine_legacy/proto/audit_data.proto\x12\x17google.appengine.legacy\x1a\x1cgoogle/api/annotations.proto\"\x9b\x01\n\tAuditData\x12\x15\n\revent_message\x18\x01 \x01(\t\x12\x45\n\nevent_data\x18\x02 \x03(\x0b\x32\x31.google.appengine.legacy.AuditData.EventDataEntry\x1a\x30\n\x0e\x45ventDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42n\n\x1b\x63om.google.appengine.legacyB\x0e\x41uditDataProtoP\x01Z=google.golang.org/genproto/googleapis/appengine/legacy;legacyb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_AUDITDATA_EVENTDATAENTRY = _descriptor.Descriptor(
  name='EventDataEntry',
  full_name='google.appengine.legacy.AuditData.EventDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.appengine.legacy.AuditData.EventDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.appengine.legacy.AuditData.EventDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=267,
)

_AUDITDATA = _descriptor.Descriptor(
  name='AuditData',
  full_name='google.appengine.legacy.AuditData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_message', full_name='google.appengine.legacy.AuditData.event_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_data', full_name='google.appengine.legacy.AuditData.event_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_AUDITDATA_EVENTDATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=267,
)

_AUDITDATA_EVENTDATAENTRY.containing_type = _AUDITDATA
_AUDITDATA.fields_by_name['event_data'].message_type = _AUDITDATA_EVENTDATAENTRY
DESCRIPTOR.message_types_by_name['AuditData'] = _AUDITDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditData = _reflection.GeneratedProtocolMessageType('AuditData', (_message.Message,), {

  'EventDataEntry' : _reflection.GeneratedProtocolMessageType('EventDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _AUDITDATA_EVENTDATAENTRY,
    '__module__' : 'google.cloud.appengine_legacy.proto.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.appengine.legacy.AuditData.EventDataEntry)
    })
  ,
  'DESCRIPTOR' : _AUDITDATA,
  '__module__' : 'google.cloud.appengine_legacy.proto.audit_data_pb2'
  ,
  '__doc__': """Admin Console legacy audit log.
  
  Attributes:
      event_message:
          Text description of the admin event. This is the “Event”
          column in Admin Console’s Admin Logs.
      event_data:
          Arbitrary event data. This is the “Result” column in Admin
          Console’s Admin Logs.
  """,
  # @@protoc_insertion_point(class_scope:google.appengine.legacy.AuditData)
  })
_sym_db.RegisterMessage(AuditData)
_sym_db.RegisterMessage(AuditData.EventDataEntry)


DESCRIPTOR._options = None
_AUDITDATA_EVENTDATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
