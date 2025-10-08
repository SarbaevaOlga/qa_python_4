from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collection.books_genre) == 2
        assert 'Гордость и предубеждение и зомби' in books_collection.books_genre
        assert 'Что делать, если ваш кот хочет вас убить' in books_collection.books_genre



    def test_add_new_book_already_added_book(self):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(books_collection.books_genre) == 1
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}


    @pytest.mark.parametrize('name', ['',
                                      'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0


    @pytest.mark.parametrize('name', ['К югу от границы',
                                      'Любовь как роза, красива, но шипы больны',
                                      'Я'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()


    def test_set_book_genre_to_existing_book(self, books_collection):
        books_collection.add_new_book('Гордость и предубеждение')
        books_collection.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert books_collection.books_genre() == {'Гордость и предубеждение': 'Фантастика'}


    def test_set_book_genre_to_not_existing_book(self, books_collection):
        books_collection.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert 'Гордость и предубеждение' not in books_collection.books_genre


    def test_set_book_genre_to_not_existing_genre(self, books_collection):
        books_collection.add_new_book('Гордость и предубеждение')
        books_collection.set_book_genre('Гордость и предубеждение', 'Трагикомедии')
        assert books_collection.books_genre() == {'Гордость и предубеждение': ''}


    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre, books_collection):
        books_collection.add_new_book(name)
        books_collection.set_book_genre(name, genre)
        assert books_collection.get_books_with_specific_genre(name) == [genre]


    def test_get_books_with_specific_genre_by_wrong_genre(self, books_collection):
        assert len(books_collection.get_books_with_specific_genre('Трагикомедии')) == 0


    def test_get_books_for_children(self, my_books_collection):
        result = my_books_collection.get_books_for_children()
        assert len(result) == 3 
        assert result == ['Симбиоз', 'Гадкий Я', 'Ревизор']


    def test_add_book_in_favorites_not_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        assert 'Симбиоз' in my_books_collection.favorites
        assert len(my_books_collection.favorites) == 1


    def test_add_book_in_favorites_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        assert 'Симбиоз' in my_books_collection.favorites
        assert len(my_books_collection.favorites) == 1


    def test_add_book_in_favorites_not_added_dict_book(self, my_books_collection):
        book = 'Идиот'
        my_books_collection.add_book_in_favorites(book)
        assert len(my_books_collection.favorites) == 0


    def test_delete_book_from_favorites(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.delete_book_from_favorites('Симбиоз')
        assert len(my_books_collection.favorites) == 0


    def test_delete_book_from_favorites_deleted_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.delete_book_from_favorites('Гадкий Я')
        assert len(my_books_collection.favorites) == 1 
        assert 'Гадкий Я' not in my_books_collection.favorites


    def test_get_list_of_favorites_books(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.add_book_in_favorites('Гадкий Я')
        assert my_books_collection.get_list_of_favorites_books() == ['Симбиоз', 'Гадкий Я']


    def test_get_books_genre(self, books_collection):
        books_collection.add_new_book('Гордость и предубеждение')
        books_collection.set_book_genre('Гордость и предубеждение', 'Фантастика')
        result = books_collection.get_books_genre()
        assert result == {'Гордость и предубеждение': 'Фантастика'}