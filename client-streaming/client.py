import grpc
from bookstore_pb2 import BookSearchRequest
from bookstore_pb2_grpc import BookSearchServiceStub


def generate_book_requests():
    requests = [
        BookSearchRequest(title='The Great Gatsby',
                          quantity=3, price_per_book=12.99),
        BookSearchRequest(title='To Kill a Mockingbird',
                          quantity=2, price_per_book=9.99),
        BookSearchRequest(title='1984', quantity=1, price_per_book=7.99),
    ]
    for request in requests:
        yield request


def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = BookSearchServiceStub(channel)
        response = stub.BulkSearchBooks(generate_book_requests())
        print(f'Total price: {response.total_price}')


if __name__ == '__main__':
    client()
