# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hello_pb2 as hello__pb2
import world_pb2 as world__pb2


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
