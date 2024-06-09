from concurrent import futures

import grpc
from bookstore_pb2 import Book, BookSearch
from bookstore_pb2_grpc import (BookStoreServicer,
                                add_BookStoreServicer_to_server)


class BookStoreService(BookStoreServicer):
    def __init__(self):
        self.books = [
            Book(name="Book 1", author="Author 1", price=10),
            Book(name="Book 2", author="Author 2", price=15),
            Book(name="Book 3", author="Author 1", price=20),
            Book(name="Book 4", author="Author 3", price=12)
        ]

    def searchByAuthor(self, request, context):
        for book in self.books:
            if request.author in book.author:
                yield book


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    add_BookStoreServicer_to_server(BookStoreService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
