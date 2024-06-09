import grpc
from bookstore_pb2 import Book
from bookstore_pb2_grpc import BookStoreStub

def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = BookStoreStub(channel)
        books = [
            Book(name="Book 1", author="Author 1", price=10),
            Book(name="Book 2", author="Author 2", price=15),
            Book(name="Book 3", author="Author 3", price=20)
        ]
        
        cart_stream = stub.liveCartValue(iter(books))
        for cart in cart_stream:
            print(f"Total books: {cart.books}, Total price: {cart.price}")

if __name__ == '__main__':
    client()