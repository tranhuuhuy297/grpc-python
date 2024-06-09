import greeting_pb2
import greeting_pb2_grpc
import grpc


def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        response = stub.greet(
            greeting_pb2.ClientInput(name='Huy', greeting="Xin chao"))
    print("Greeter client received following from server: " + response.message)


if __name__ == '__main__':
    client()
