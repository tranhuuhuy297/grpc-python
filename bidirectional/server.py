from concurrent import futures

import grpc
from bookstore_pb2 import Book, Cart
from bookstore_pb2_grpc import (BookStoreServicer,
                                add_BookStoreServicer_to_server)


class BookStoreService(BookStoreServicer):
    def liveCartValue(self, request_iterator, context):
        total_books = 0
        total_price = 0

        for book in request_iterator:
            total_books += 1
            total_price += book.price
            yield Cart(books=total_books, price=total_price)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BookStoreServicer_to_server(BookStoreService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
