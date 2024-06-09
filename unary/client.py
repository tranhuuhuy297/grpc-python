import bookstore_pb2
import bookstore_pb2_grpc
import grpc


def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bookstore_pb2_grpc.BookStoreStub(channel)
        response = stub.first(
            bookstore_pb2.BookSearch(name='Harry Potter', author="Huy", genre="horror"))
    # print("Name: {}, Author: {}, Genre: {}".format(
    #     response.name, response.author, response.genre))
        print(response)


if __name__ == '__main__':
    client()
