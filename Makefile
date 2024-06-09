gen-greeting:
	python -m grpc_tools.protoc --proto_path=proto_files/ --python_out=. --grpc_python_out=.  greeting.proto