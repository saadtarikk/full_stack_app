from flask import Flask, Blueprint, render_template, request, redirect
from repositories import author_repository, book_repository
from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('/books/index.html', all_books=books)


@books_blueprint.route('/books/new', methods=['GET'])
def new_book():
    books = book_repository.select_all()
    return render_template('/books/new.html', all_books=books)


@books_blueprint.route('/books', methods=['POST'])
def create_new_book():
    title = request.form['title']
    genre = request.form['genre']
    author = request.form['author']
    newbook = Book(title, genre, author)
    new_author = Author[author.name]
    all_authors = author_repository.select_all()
    for author in all_authors:
        if author.name == new_author:
            book_repository.save(newbook)
        # else:
        #     author_repository.save(new_author)
        #     author_repository.select()

    return redirect('/books')


@books_blueprint.route('/books/<id>/delete', methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
