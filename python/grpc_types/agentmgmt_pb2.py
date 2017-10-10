# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agentmgmt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agentmgmt.proto',
  package='grpc_types',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x61gentmgmt.proto\x12\ngrpc_types\"*\n\x19GetAvailableAgentsRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\"/\n\x1aGetAvailableAgentsResponse\x12\x11\n\tagent_ids\x18\x01 \x03(\t\"*\n\x18GetAgentIDFromRefRequest\x12\x0e\n\x06ref_id\x18\x01 \x01(\t\"-\n\x19GetAgentIDFromRefResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x05\"#\n\x10HeartBeatRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"$\n\x11HeartBeatResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"$\n\x11\x41\x63\x63\x65ptCallRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"&\n\x12\x41\x63\x63\x65ptCallResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xf1\x02\n\tAgentMgmt\x12\x65\n\x12GetAvailableAgents\x12%.grpc_types.GetAvailableAgentsRequest\x1a&.grpc_types.GetAvailableAgentsResponse\"\x00\x12\x62\n\x11GetAgentIDFromRef\x12$.grpc_types.GetAgentIDFromRefRequest\x1a%.grpc_types.GetAgentIDFromRefResponse\"\x00\x12J\n\tHeartBeat\x12\x1c.grpc_types.HeartBeatRequest\x1a\x1d.grpc_types.HeartBeatResponse\"\x00\x12M\n\nAcceptCall\x12\x1d.grpc_types.AcceptCallRequest\x1a\x1e.grpc_types.AcceptCallResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETAVAILABLEAGENTSREQUEST = _descriptor.Descriptor(
  name='GetAvailableAgentsRequest',
  full_name='grpc_types.GetAvailableAgentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='grpc_types.GetAvailableAgentsRequest.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=73,
)


_GETAVAILABLEAGENTSRESPONSE = _descriptor.Descriptor(
  name='GetAvailableAgentsResponse',
  full_name='grpc_types.GetAvailableAgentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_ids', full_name='grpc_types.GetAvailableAgentsResponse.agent_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=122,
)


_GETAGENTIDFROMREFREQUEST = _descriptor.Descriptor(
  name='GetAgentIDFromRefRequest',
  full_name='grpc_types.GetAgentIDFromRefRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ref_id', full_name='grpc_types.GetAgentIDFromRefRequest.ref_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=166,
)


_GETAGENTIDFROMREFRESPONSE = _descriptor.Descriptor(
  name='GetAgentIDFromRefResponse',
  full_name='grpc_types.GetAgentIDFromRefResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='grpc_types.GetAgentIDFromRefResponse.agent_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=213,
)


_HEARTBEATREQUEST = _descriptor.Descriptor(
  name='HeartBeatRequest',
  full_name='grpc_types.HeartBeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_types.HeartBeatRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=250,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartBeatResponse',
  full_name='grpc_types.HeartBeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_types.HeartBeatResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=288,
)


_ACCEPTCALLREQUEST = _descriptor.Descriptor(
  name='AcceptCallRequest',
  full_name='grpc_types.AcceptCallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_types.AcceptCallRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=326,
)


_ACCEPTCALLRESPONSE = _descriptor.Descriptor(
  name='AcceptCallResponse',
  full_name='grpc_types.AcceptCallResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='grpc_types.AcceptCallResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=366,
)

DESCRIPTOR.message_types_by_name['GetAvailableAgentsRequest'] = _GETAVAILABLEAGENTSREQUEST
DESCRIPTOR.message_types_by_name['GetAvailableAgentsResponse'] = _GETAVAILABLEAGENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetAgentIDFromRefRequest'] = _GETAGENTIDFROMREFREQUEST
DESCRIPTOR.message_types_by_name['GetAgentIDFromRefResponse'] = _GETAGENTIDFROMREFRESPONSE
DESCRIPTOR.message_types_by_name['HeartBeatRequest'] = _HEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['HeartBeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['AcceptCallRequest'] = _ACCEPTCALLREQUEST
DESCRIPTOR.message_types_by_name['AcceptCallResponse'] = _ACCEPTCALLRESPONSE

GetAvailableAgentsRequest = _reflection.GeneratedProtocolMessageType('GetAvailableAgentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAVAILABLEAGENTSREQUEST,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.GetAvailableAgentsRequest)
  ))
_sym_db.RegisterMessage(GetAvailableAgentsRequest)

GetAvailableAgentsResponse = _reflection.GeneratedProtocolMessageType('GetAvailableAgentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETAVAILABLEAGENTSRESPONSE,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.GetAvailableAgentsResponse)
  ))
_sym_db.RegisterMessage(GetAvailableAgentsResponse)

GetAgentIDFromRefRequest = _reflection.GeneratedProtocolMessageType('GetAgentIDFromRefRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAGENTIDFROMREFREQUEST,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.GetAgentIDFromRefRequest)
  ))
_sym_db.RegisterMessage(GetAgentIDFromRefRequest)

GetAgentIDFromRefResponse = _reflection.GeneratedProtocolMessageType('GetAgentIDFromRefResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETAGENTIDFROMREFRESPONSE,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.GetAgentIDFromRefResponse)
  ))
_sym_db.RegisterMessage(GetAgentIDFromRefResponse)

HeartBeatRequest = _reflection.GeneratedProtocolMessageType('HeartBeatRequest', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATREQUEST,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.HeartBeatRequest)
  ))
_sym_db.RegisterMessage(HeartBeatRequest)

HeartBeatResponse = _reflection.GeneratedProtocolMessageType('HeartBeatResponse', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATRESPONSE,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.HeartBeatResponse)
  ))
_sym_db.RegisterMessage(HeartBeatResponse)

AcceptCallRequest = _reflection.GeneratedProtocolMessageType('AcceptCallRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTCALLREQUEST,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.AcceptCallRequest)
  ))
_sym_db.RegisterMessage(AcceptCallRequest)

AcceptCallResponse = _reflection.GeneratedProtocolMessageType('AcceptCallResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTCALLRESPONSE,
  __module__ = 'agentmgmt_pb2'
  # @@protoc_insertion_point(class_scope:grpc_types.AcceptCallResponse)
  ))
_sym_db.RegisterMessage(AcceptCallResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class AgentMgmtStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetAvailableAgents = channel.unary_unary(
          '/grpc_types.AgentMgmt/GetAvailableAgents',
          request_serializer=GetAvailableAgentsRequest.SerializeToString,
          response_deserializer=GetAvailableAgentsResponse.FromString,
          )
      self.GetAgentIDFromRef = channel.unary_unary(
          '/grpc_types.AgentMgmt/GetAgentIDFromRef',
          request_serializer=GetAgentIDFromRefRequest.SerializeToString,
          response_deserializer=GetAgentIDFromRefResponse.FromString,
          )
      self.HeartBeat = channel.unary_unary(
          '/grpc_types.AgentMgmt/HeartBeat',
          request_serializer=HeartBeatRequest.SerializeToString,
          response_deserializer=HeartBeatResponse.FromString,
          )
      self.AcceptCall = channel.unary_unary(
          '/grpc_types.AgentMgmt/AcceptCall',
          request_serializer=AcceptCallRequest.SerializeToString,
          response_deserializer=AcceptCallResponse.FromString,
          )


  class AgentMgmtServicer(object):

    def GetAvailableAgents(self, request, context):
      """AgentMgmt service // Go uses CamelCase so use it for API calls
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetAgentIDFromRef(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AcceptCall(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AgentMgmtServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableAgents': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableAgents,
            request_deserializer=GetAvailableAgentsRequest.FromString,
            response_serializer=GetAvailableAgentsResponse.SerializeToString,
        ),
        'GetAgentIDFromRef': grpc.unary_unary_rpc_method_handler(
            servicer.GetAgentIDFromRef,
            request_deserializer=GetAgentIDFromRefRequest.FromString,
            response_serializer=GetAgentIDFromRefResponse.SerializeToString,
        ),
        'HeartBeat': grpc.unary_unary_rpc_method_handler(
            servicer.HeartBeat,
            request_deserializer=HeartBeatRequest.FromString,
            response_serializer=HeartBeatResponse.SerializeToString,
        ),
        'AcceptCall': grpc.unary_unary_rpc_method_handler(
            servicer.AcceptCall,
            request_deserializer=AcceptCallRequest.FromString,
            response_serializer=AcceptCallResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'grpc_types.AgentMgmt', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAgentMgmtServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetAvailableAgents(self, request, context):
      """AgentMgmt service // Go uses CamelCase so use it for API calls
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetAgentIDFromRef(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def HeartBeat(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AcceptCall(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAgentMgmtStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetAvailableAgents(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """AgentMgmt service // Go uses CamelCase so use it for API calls
      """
      raise NotImplementedError()
    GetAvailableAgents.future = None
    def GetAgentIDFromRef(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetAgentIDFromRef.future = None
    def HeartBeat(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    HeartBeat.future = None
    def AcceptCall(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    AcceptCall.future = None


  def beta_create_AgentMgmt_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('grpc_types.AgentMgmt', 'AcceptCall'): AcceptCallRequest.FromString,
      ('grpc_types.AgentMgmt', 'GetAgentIDFromRef'): GetAgentIDFromRefRequest.FromString,
      ('grpc_types.AgentMgmt', 'GetAvailableAgents'): GetAvailableAgentsRequest.FromString,
      ('grpc_types.AgentMgmt', 'HeartBeat'): HeartBeatRequest.FromString,
    }
    response_serializers = {
      ('grpc_types.AgentMgmt', 'AcceptCall'): AcceptCallResponse.SerializeToString,
      ('grpc_types.AgentMgmt', 'GetAgentIDFromRef'): GetAgentIDFromRefResponse.SerializeToString,
      ('grpc_types.AgentMgmt', 'GetAvailableAgents'): GetAvailableAgentsResponse.SerializeToString,
      ('grpc_types.AgentMgmt', 'HeartBeat'): HeartBeatResponse.SerializeToString,
    }
    method_implementations = {
      ('grpc_types.AgentMgmt', 'AcceptCall'): face_utilities.unary_unary_inline(servicer.AcceptCall),
      ('grpc_types.AgentMgmt', 'GetAgentIDFromRef'): face_utilities.unary_unary_inline(servicer.GetAgentIDFromRef),
      ('grpc_types.AgentMgmt', 'GetAvailableAgents'): face_utilities.unary_unary_inline(servicer.GetAvailableAgents),
      ('grpc_types.AgentMgmt', 'HeartBeat'): face_utilities.unary_unary_inline(servicer.HeartBeat),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_AgentMgmt_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('grpc_types.AgentMgmt', 'AcceptCall'): AcceptCallRequest.SerializeToString,
      ('grpc_types.AgentMgmt', 'GetAgentIDFromRef'): GetAgentIDFromRefRequest.SerializeToString,
      ('grpc_types.AgentMgmt', 'GetAvailableAgents'): GetAvailableAgentsRequest.SerializeToString,
      ('grpc_types.AgentMgmt', 'HeartBeat'): HeartBeatRequest.SerializeToString,
    }
    response_deserializers = {
      ('grpc_types.AgentMgmt', 'AcceptCall'): AcceptCallResponse.FromString,
      ('grpc_types.AgentMgmt', 'GetAgentIDFromRef'): GetAgentIDFromRefResponse.FromString,
      ('grpc_types.AgentMgmt', 'GetAvailableAgents'): GetAvailableAgentsResponse.FromString,
      ('grpc_types.AgentMgmt', 'HeartBeat'): HeartBeatResponse.FromString,
    }
    cardinalities = {
      'AcceptCall': cardinality.Cardinality.UNARY_UNARY,
      'GetAgentIDFromRef': cardinality.Cardinality.UNARY_UNARY,
      'GetAvailableAgents': cardinality.Cardinality.UNARY_UNARY,
      'HeartBeat': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'grpc_types.AgentMgmt', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
