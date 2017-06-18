# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import world_pb2 as world__pb2


class WorldStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sayWorld = channel.unary_unary(
        '/world.World/sayWorld',
        request_serializer=world__pb2.WorldRequest.SerializeToString,
        response_deserializer=world__pb2.WordResponse.FromString,
        )


class WorldServicer(object):

  def sayWorld(self, request, context):
    """World service 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorldServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sayWorld': grpc.unary_unary_rpc_method_handler(
          servicer.sayWorld,
          request_deserializer=world__pb2.WorldRequest.FromString,
          response_serializer=world__pb2.WordResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'world.World', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
