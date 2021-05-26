import pdb
from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()


author1 = Author("Jack Jones")
author_repository.save(author1)
author2 = Author("Davi Jone")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Mobi Dick", "classic", author1)
book_repository.save(book1)
book2 = Book("Mobi Dick", "classic", author1)
book_repository.save(book2)
book_repository.select(book2.id)

pdb.set_trace()

# book_repository.select_all()


# author1.author_name1= "david jones"
# author_repository.update(author1)


# author_repository.delete(author1.id)
