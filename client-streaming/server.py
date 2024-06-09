from concurrent import futures

import grpc
from bookstore_pb2 import BookSearchRequest, BookSearchResponse
from bookstore_pb2_grpc import (BookSearchServiceServicer,
                                add_BookSearchServiceServicer_to_server)


class BookSearchServiceImpl(BookSearchServiceServicer):
    def BulkSearchBooks(self, request_iterator, context):
        total_price = 0.0
        for request in request_iterator:
            total_price += request.quantity * request.price_per_book
        return BookSearchResponse(total_price=total_price)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BookSearchServiceServicer_to_server(BookSearchServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
