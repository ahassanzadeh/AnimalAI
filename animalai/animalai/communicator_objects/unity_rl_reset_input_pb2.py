# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animalai/communicator_objects/unity_rl_reset_input.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from animalai.communicator_objects import arena_parameters_proto_pb2 as animalai_dot_communicator__objects_dot_arena__parameters__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='animalai/communicator_objects/unity_rl_reset_input.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n8animalai/communicator_objects/unity_rl_reset_input.proto\x12\x14\x63ommunicator_objects\x1a:animalai/communicator_objects/arena_parameters_proto.proto\"\xb3\x01\n\x11UnityRLResetInput\x12\x43\n\x06\x61renas\x18\x01 \x03(\x0b\x32\x33.communicator_objects.UnityRLResetInput.ArenasEntry\x1aY\n\x0b\x41renasEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.communicator_objects.ArenaParametersProto:\x02\x38\x01\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[animalai_dot_communicator__objects_dot_arena__parameters__proto__pb2.DESCRIPTOR,])




_UNITYRLRESETINPUT_ARENASENTRY = _descriptor.Descriptor(
  name='ArenasEntry',
  full_name='communicator_objects.UnityRLResetInput.ArenasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='communicator_objects.UnityRLResetInput.ArenasEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='communicator_objects.UnityRLResetInput.ArenasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=322,
)

_UNITYRLRESETINPUT = _descriptor.Descriptor(
  name='UnityRLResetInput',
  full_name='communicator_objects.UnityRLResetInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arenas', full_name='communicator_objects.UnityRLResetInput.arenas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UNITYRLRESETINPUT_ARENASENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=322,
)

_UNITYRLRESETINPUT_ARENASENTRY.fields_by_name['value'].message_type = animalai_dot_communicator__objects_dot_arena__parameters__proto__pb2._ARENAPARAMETERSPROTO
_UNITYRLRESETINPUT_ARENASENTRY.containing_type = _UNITYRLRESETINPUT
_UNITYRLRESETINPUT.fields_by_name['arenas'].message_type = _UNITYRLRESETINPUT_ARENASENTRY
DESCRIPTOR.message_types_by_name['UnityRLResetInput'] = _UNITYRLRESETINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityRLResetInput = _reflection.GeneratedProtocolMessageType('UnityRLResetInput', (_message.Message,), {

  'ArenasEntry' : _reflection.GeneratedProtocolMessageType('ArenasEntry', (_message.Message,), {
    'DESCRIPTOR' : _UNITYRLRESETINPUT_ARENASENTRY,
    '__module__' : 'animalai.communicator_objects.unity_rl_reset_input_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLResetInput.ArenasEntry)
    })
  ,
  'DESCRIPTOR' : _UNITYRLRESETINPUT,
  '__module__' : 'animalai.communicator_objects.unity_rl_reset_input_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLResetInput)
  })
_sym_db.RegisterMessage(UnityRLResetInput)
_sym_db.RegisterMessage(UnityRLResetInput.ArenasEntry)


DESCRIPTOR._options = None
_UNITYRLRESETINPUT_ARENASENTRY._options = None
# @@protoc_insertion_point(module_scope)
