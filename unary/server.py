from concurrent import futures

import bookstore_pb2
import bookstore_pb2_grpc
import grpc


class Firster(bookstore_pb2_grpc.BookStoreServicer):
    def first(self, request, context):
        print(str(request))
        return bookstore_pb2.Book(name=request.name, author=request.author, price=3)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    bookstore_pb2_grpc.add_BookStoreServicer_to_server(Firster(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
