
NO_COLOR=\033[0m
GREEN=\033[0;32m
RED=\033[31;01m
WARN_COLOR=\033[33;01m
 
OK_STRING=$(OK_COLOR)[OK]$(NO_COLOR)
INFO=$(GREEN)[INFO]$(NO_COLOR)
ERROR_STRING=$(RED)[ERRORS]$(NO_COLOR)
WARN_STRING=$(WARN_COLOR)[WARNINGS]$(NO_COLOR)


PROTOS_DIR=../protos


all: build_python build_go

.PHONY: build_python build_go

build_python:
	@echo "$(INFO) Building Python Files from .protos"
	python -m grpc_tools.protoc -I $(PROTOS_DIR)  --python_out=./python/grpc_types/ --grpc_python_out=./python/grpc_types/ $(PROTOS_DIR)/*.proto

build_go:
	@echo "$(INFO) Building go Files from .protos"
	mkdir -p go/grpc_types
	@for proto_file in $(PROTOS_DIR)/*.proto; do \
		echo "$(INFO) Found $$proto_file. Processing for package grpc_types ..."; \
		protoc -I $(PROTOS_DIR) $$proto_file --go_out=plugins=grpc:go/grpc_types; \
	done

