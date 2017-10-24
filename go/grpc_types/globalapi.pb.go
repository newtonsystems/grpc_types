// Code generated by protoc-gen-go. DO NOT EDIT.
// source: globalapi.proto

package grpc_types

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// Client API for GlobalAPI service

type GlobalAPIClient interface {
	// All API calls from all services
	SayHello(ctx context.Context, in *HelloRequest, opts ...grpc.CallOption) (*HelloResponse, error)
	SayWorld(ctx context.Context, in *WorldRequest, opts ...grpc.CallOption) (*WorldResponse, error)
	AddTask(ctx context.Context, in *AddTaskRequest, opts ...grpc.CallOption) (*AddTaskResponse, error)
	GetAvailableAgents(ctx context.Context, in *GetAvailableAgentsRequest, opts ...grpc.CallOption) (*GetAvailableAgentsResponse, error)
	GetAgentIDFromRef(ctx context.Context, in *GetAgentIDFromRefRequest, opts ...grpc.CallOption) (*GetAgentIDFromRefResponse, error)
	HeartBeat(ctx context.Context, in *HeartBeatRequest, opts ...grpc.CallOption) (*HeartBeatResponse, error)
	AcceptCall(ctx context.Context, in *AcceptCallRequest, opts ...grpc.CallOption) (*AcceptCallResponse, error)
}

type globalAPIClient struct {
	cc *grpc.ClientConn
}

func NewGlobalAPIClient(cc *grpc.ClientConn) GlobalAPIClient {
	return &globalAPIClient{cc}
}

func (c *globalAPIClient) SayHello(ctx context.Context, in *HelloRequest, opts ...grpc.CallOption) (*HelloResponse, error) {
	out := new(HelloResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/sayHello", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *globalAPIClient) SayWorld(ctx context.Context, in *WorldRequest, opts ...grpc.CallOption) (*WorldResponse, error) {
	out := new(WorldResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/sayWorld", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *globalAPIClient) AddTask(ctx context.Context, in *AddTaskRequest, opts ...grpc.CallOption) (*AddTaskResponse, error) {
	out := new(AddTaskResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/AddTask", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *globalAPIClient) GetAvailableAgents(ctx context.Context, in *GetAvailableAgentsRequest, opts ...grpc.CallOption) (*GetAvailableAgentsResponse, error) {
	out := new(GetAvailableAgentsResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/GetAvailableAgents", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *globalAPIClient) GetAgentIDFromRef(ctx context.Context, in *GetAgentIDFromRefRequest, opts ...grpc.CallOption) (*GetAgentIDFromRefResponse, error) {
	out := new(GetAgentIDFromRefResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/GetAgentIDFromRef", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *globalAPIClient) HeartBeat(ctx context.Context, in *HeartBeatRequest, opts ...grpc.CallOption) (*HeartBeatResponse, error) {
	out := new(HeartBeatResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/HeartBeat", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *globalAPIClient) AcceptCall(ctx context.Context, in *AcceptCallRequest, opts ...grpc.CallOption) (*AcceptCallResponse, error) {
	out := new(AcceptCallResponse)
	err := grpc.Invoke(ctx, "/grpc_types.GlobalAPI/AcceptCall", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// Server API for GlobalAPI service

type GlobalAPIServer interface {
	// All API calls from all services
	SayHello(context.Context, *HelloRequest) (*HelloResponse, error)
	SayWorld(context.Context, *WorldRequest) (*WorldResponse, error)
	AddTask(context.Context, *AddTaskRequest) (*AddTaskResponse, error)
	GetAvailableAgents(context.Context, *GetAvailableAgentsRequest) (*GetAvailableAgentsResponse, error)
	GetAgentIDFromRef(context.Context, *GetAgentIDFromRefRequest) (*GetAgentIDFromRefResponse, error)
	HeartBeat(context.Context, *HeartBeatRequest) (*HeartBeatResponse, error)
	AcceptCall(context.Context, *AcceptCallRequest) (*AcceptCallResponse, error)
}

func RegisterGlobalAPIServer(s *grpc.Server, srv GlobalAPIServer) {
	s.RegisterService(&_GlobalAPI_serviceDesc, srv)
}

func _GlobalAPI_SayHello_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(HelloRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).SayHello(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/SayHello",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).SayHello(ctx, req.(*HelloRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GlobalAPI_SayWorld_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorldRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).SayWorld(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/SayWorld",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).SayWorld(ctx, req.(*WorldRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GlobalAPI_AddTask_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddTaskRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).AddTask(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/AddTask",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).AddTask(ctx, req.(*AddTaskRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GlobalAPI_GetAvailableAgents_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetAvailableAgentsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).GetAvailableAgents(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/GetAvailableAgents",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).GetAvailableAgents(ctx, req.(*GetAvailableAgentsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GlobalAPI_GetAgentIDFromRef_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetAgentIDFromRefRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).GetAgentIDFromRef(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/GetAgentIDFromRef",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).GetAgentIDFromRef(ctx, req.(*GetAgentIDFromRefRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GlobalAPI_HeartBeat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(HeartBeatRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).HeartBeat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/HeartBeat",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).HeartBeat(ctx, req.(*HeartBeatRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GlobalAPI_AcceptCall_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AcceptCallRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GlobalAPIServer).AcceptCall(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc_types.GlobalAPI/AcceptCall",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GlobalAPIServer).AcceptCall(ctx, req.(*AcceptCallRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _GlobalAPI_serviceDesc = grpc.ServiceDesc{
	ServiceName: "grpc_types.GlobalAPI",
	HandlerType: (*GlobalAPIServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "sayHello",
			Handler:    _GlobalAPI_SayHello_Handler,
		},
		{
			MethodName: "sayWorld",
			Handler:    _GlobalAPI_SayWorld_Handler,
		},
		{
			MethodName: "AddTask",
			Handler:    _GlobalAPI_AddTask_Handler,
		},
		{
			MethodName: "GetAvailableAgents",
			Handler:    _GlobalAPI_GetAvailableAgents_Handler,
		},
		{
			MethodName: "GetAgentIDFromRef",
			Handler:    _GlobalAPI_GetAgentIDFromRef_Handler,
		},
		{
			MethodName: "HeartBeat",
			Handler:    _GlobalAPI_HeartBeat_Handler,
		},
		{
			MethodName: "AcceptCall",
			Handler:    _GlobalAPI_AcceptCall_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "globalapi.proto",
}

func init() { proto.RegisterFile("globalapi.proto", fileDescriptor1) }

var fileDescriptor1 = []byte{
	// 280 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x84, 0x92, 0xbd, 0x4e, 0xc3, 0x30,
	0x14, 0x85, 0x19, 0x10, 0xd0, 0xdb, 0xa1, 0xc2, 0x13, 0x84, 0x9f, 0x01, 0x51, 0xc6, 0x0c, 0xf0,
	0x04, 0x86, 0x8a, 0xb6, 0x48, 0x48, 0xa8, 0x42, 0x62, 0x44, 0x37, 0xc9, 0x25, 0x54, 0x38, 0xb5,
	0xb1, 0x0d, 0xa8, 0x0f, 0xc7, 0xbb, 0x21, 0xa7, 0xb6, 0xdb, 0xd0, 0x54, 0x1d, 0x73, 0xbe, 0x73,
	0xbf, 0xa3, 0x44, 0x81, 0x5e, 0x29, 0x64, 0x86, 0x02, 0xd5, 0x34, 0x55, 0x5a, 0x5a, 0xc9, 0xa0,
	0xd4, 0x2a, 0x7f, 0xb5, 0x73, 0x45, 0x26, 0xe9, 0xbe, 0x93, 0x10, 0x72, 0x01, 0x92, 0xee, 0x8f,
	0xd4, 0xa2, 0xf0, 0x0f, 0x3d, 0x2c, 0x69, 0x66, 0xab, 0xb2, 0xb2, 0x8b, 0xe0, 0xfa, 0x77, 0x17,
	0x3a, 0xc3, 0x5a, 0xc5, 0x9f, 0xc6, 0x8c, 0xc3, 0x81, 0xc1, 0xf9, 0xc8, 0x5d, 0xb3, 0xa3, 0x74,
	0x69, 0x4c, 0xeb, 0x68, 0x42, 0x9f, 0x5f, 0x64, 0x6c, 0x72, 0xdc, 0x42, 0x8c, 0x92, 0x33, 0x43,
	0x17, 0x3b, 0x5e, 0xf1, 0xe2, 0x36, 0x9b, 0x8a, 0x3a, 0x6a, 0x55, 0x78, 0x12, 0x15, 0x03, 0xd8,
	0xe7, 0x45, 0xf1, 0x8c, 0xe6, 0x83, 0x25, 0xab, 0x3d, 0x1f, 0x06, 0xc7, 0x49, 0x2b, 0x8b, 0x16,
	0x02, 0x36, 0x24, 0xcb, 0xbf, 0x71, 0x2a, 0x30, 0x13, 0xc4, 0xdd, 0x8b, 0x1b, 0xd6, 0x5f, 0x3d,
	0x5a, 0xe7, 0xc1, 0x7d, 0xb5, 0xad, 0x16, 0x67, 0x32, 0x38, 0x74, 0xdc, 0xc5, 0xe3, 0xc1, 0xbd,
	0x96, 0xd5, 0x84, 0xde, 0xd8, 0xe5, 0xff, 0xf3, 0x06, 0x0e, 0x23, 0xfd, 0x2d, 0xad, 0xb8, 0xf1,
	0x00, 0x9d, 0x11, 0xa1, 0xb6, 0xb7, 0x84, 0x96, 0x9d, 0x36, 0xbf, 0xbe, 0x8f, 0x83, 0xf3, 0x6c,
	0x03, 0x8d, 0xae, 0x47, 0x00, 0x9e, 0xe7, 0xa4, 0xec, 0x1d, 0x0a, 0xc1, 0x1a, 0xf5, 0x65, 0x1e,
	0x6c, 0xe7, 0x9b, 0x70, 0xd0, 0x65, 0x7b, 0xf5, 0x6f, 0x74, 0xf3, 0x17, 0x00, 0x00, 0xff, 0xff,
	0xe7, 0xd9, 0x0d, 0x76, 0x90, 0x02, 0x00, 0x00,
}
