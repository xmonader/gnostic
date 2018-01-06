// Copyright 2018 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"flag"
	"log"
	"net"

	pb "github.com/googleapis/gnostic/service/gnostic"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

type GnosticServer struct{}

var gnosticServer GnosticServer

// Publish an API model, returning a URL and a management token.
func (s *GnosticServer) PostModel(context.Context, *pb.PostModelRequest) (*pb.PostModelResponse, error) {
	response := &pb.PostModelResponse{}
	return response, nil
}

// Get a published API model.
func (s *GnosticServer) GetModel(context.Context, *pb.GetModelRequest) (*pb.GetModelResponse, error) {
	response := &pb.GetModelResponse{}
	return response, nil
}

// Remove a published API model.
func (s *GnosticServer) DeleteModel(context.Context, *pb.DeleteModelRequest) (*pb.DeleteModelResponse, error) {
	response := &pb.DeleteModelResponse{}
	return response, nil
}

// List API models published by this service.
func (s *GnosticServer) ListModels(context.Context, *pb.ListModelRequest) (*pb.ListModelResponse, error) {
	response := &pb.ListModelResponse{}
	return response, nil
}

// Validate an API model.
func (s *GnosticServer) Validate(context.Context, *pb.ValidateRequest) (*pb.ValidateResponse, error) {
	response := &pb.ValidateResponse{}
	return response, nil
}

// Check an API model with one or more linters.
func (s *GnosticServer) Check(context.Context, *pb.CheckRequest) (*pb.CheckResponse, error) {
	response := &pb.CheckResponse{}
	return response, nil
}

// Generate API-related code.
func (s *GnosticServer) Generate(context.Context, *pb.GenerateRequest) (*pb.GenerateResponse, error) {
	response := &pb.GenerateResponse{}
	return response, nil
}

func main() {
	var useTLS = flag.Bool("tls", false, "Use tls for connections.")

	flag.Parse()

	var err error
	var listener net.Listener
	var grpcServer *grpc.Server
	if !*useTLS {
		listener, err = net.Listen("tcp", ":8080")
		if err != nil {
			log.Fatalf("failed to listen: %v", err)
		}
		grpcServer = grpc.NewServer()
	} else {
		certFile := "ssl.crt"
		keyFile := "ssl.key"
		creds, err := credentials.NewServerTLSFromFile(certFile, keyFile)
		listener, err = net.Listen("tcp", ":443")
		if err != nil {
			log.Fatalf("failed to listen: %v", err)
		}
		grpcServer = grpc.NewServer(grpc.Creds(creds))
	}
	pb.RegisterGnosticServer(grpcServer, &gnosticServer)
	grpcServer.Serve(listener)
}
