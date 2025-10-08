@pytest.fixture
def books_collection():
    return books_collection

@pytest.fixture
def my_books_collection():
    collector = BooksCollector()
    # Добавляем книги с разными жанрами для тестирования
    collector.add_new_book('Симбиоз')
    collector.set_book_genre('Симбиоз', 'Фантастика')
    
    collector.add_new_book('Гадкий Я')
    collector.set_book_genre('Гадкий Я', 'Мультфильмы')
    
    collector.add_new_book('Ревизор')
    collector.set_book_genre('Ревизор', 'Комедии')
    
    collector.add_new_book('Шерлок')
    collector.set_book_genre('Шерлок', 'Детективы')
    
    collector.add_new_book('Дракула')
    collector.set_book_genre('Дракула', 'Ужасы')
    
    return collector

