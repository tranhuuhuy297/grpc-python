import grpc
from bookstore_pb2 import BookSearch
from bookstore_pb2_grpc import BookStoreStub


def search_books_by_author(author):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = BookStoreStub(channel)
        book_search = BookSearch(author=author)
        response = stub.searchByAuthor(book_search)
        for book in response:
            print(
                f"Name: {book.name}, Author: {book.author}, Price: {book.price}")


if __name__ == '__main__':
    search_books_by_author("Author 1")
