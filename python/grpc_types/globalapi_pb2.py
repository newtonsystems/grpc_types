# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: globalapi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hello_pb2 as hello__pb2
import world_pb2 as world__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='globalapi.proto',
  package='grpc_types',
  syntax='proto3',
  serialized_pb=_b('\n\x0fglobalapi.proto\x12\ngrpc_types\x1a\x0bhello.proto\x1a\x0bworld.proto2\x91\x01\n\tGlobalAPI\x12\x41\n\x08sayHello\x12\x18.grpc_types.HelloRequest\x1a\x19.grpc_types.HelloResponse\"\x00\x12\x41\n\x08sayWorld\x12\x18.grpc_types.WorldRequest\x1a\x19.grpc_types.WorldResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[hello__pb2.DESCRIPTOR,world__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class GlobalAPIStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.sayHello = channel.unary_unary(
          '/grpc_types.GlobalAPI/sayHello',
          request_serializer=hello__pb2.HelloRequest.SerializeToString,
          response_deserializer=hello__pb2.HelloResponse.FromString,
          )
      self.sayWorld = channel.unary_unary(
          '/grpc_types.GlobalAPI/sayWorld',
          request_serializer=world__pb2.WorldRequest.SerializeToString,
          response_deserializer=world__pb2.WorldResponse.FromString,
          )


  class GlobalAPIServicer(object):

    def sayHello(self, request, context):
      """All API calls from all services
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def sayWorld(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_GlobalAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'sayHello': grpc.unary_unary_rpc_method_handler(
            servicer.sayHello,
            request_deserializer=hello__pb2.HelloRequest.FromString,
            response_serializer=hello__pb2.HelloResponse.SerializeToString,
        ),
        'sayWorld': grpc.unary_unary_rpc_method_handler(
            servicer.sayWorld,
            request_deserializer=world__pb2.WorldRequest.FromString,
            response_serializer=world__pb2.WorldResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'grpc_types.GlobalAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaGlobalAPIServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def sayHello(self, request, context):
      """All API calls from all services
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def sayWorld(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaGlobalAPIStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def sayHello(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """All API calls from all services
      """
      raise NotImplementedError()
    sayHello.future = None
    def sayWorld(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    sayWorld.future = None


  def beta_create_GlobalAPI_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('grpc_types.GlobalAPI', 'sayHello'): hello__pb2.HelloRequest.FromString,
      ('grpc_types.GlobalAPI', 'sayWorld'): world__pb2.WorldRequest.FromString,
    }
    response_serializers = {
      ('grpc_types.GlobalAPI', 'sayHello'): hello__pb2.HelloResponse.SerializeToString,
      ('grpc_types.GlobalAPI', 'sayWorld'): world__pb2.WorldResponse.SerializeToString,
    }
    method_implementations = {
      ('grpc_types.GlobalAPI', 'sayHello'): face_utilities.unary_unary_inline(servicer.sayHello),
      ('grpc_types.GlobalAPI', 'sayWorld'): face_utilities.unary_unary_inline(servicer.sayWorld),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_GlobalAPI_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('grpc_types.GlobalAPI', 'sayHello'): hello__pb2.HelloRequest.SerializeToString,
      ('grpc_types.GlobalAPI', 'sayWorld'): world__pb2.WorldRequest.SerializeToString,
    }
    response_deserializers = {
      ('grpc_types.GlobalAPI', 'sayHello'): hello__pb2.HelloResponse.FromString,
      ('grpc_types.GlobalAPI', 'sayWorld'): world__pb2.WorldResponse.FromString,
    }
    cardinalities = {
      'sayHello': cardinality.Cardinality.UNARY_UNARY,
      'sayWorld': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'grpc_types.GlobalAPI', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
