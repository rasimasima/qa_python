import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()

        collector.add_new_book("")
        assert "" not in collector.books_genre

    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ''

    def test_set_book_genre_success_when_book_and_genre_valid(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
        genre = "Фантастика"

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_returns_correct_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
        genre = "Фантастика"

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_book_genre(book_name)
        assert result == genre

    def test_get_book_genre_basic_scenarios(self, book_name, genre, expected_result,collector):
        collector = BooksCollector()
        genre = "Фантастика"

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.add_new_book("Манюня")
        collector.set_book_genre("Манюня", "Комедии")

        result = collector.get_books_with_specific_genre(genre)
        assert result == ["Гарри Поттер", "Дюна"]

    @pytest.mark.parametrize(
        "genre, expected_books",
        [
            ("Фантастика", ["Хоббит", "Голодные игры"]),
            ("Ужасы", ["Оно"]),
            ("Неизвестный жанр", []),
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books,collector):
        collector = BooksCollector()
        books_data = [
            ("Хоббит", "Фантастика"),
            ("Оно", "Ужасы"),
            ("Голодные игры", "Фантастика")
        ]
        for name, gen in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, gen)

        result = collector.get_books_with_specific_genre(genre)
        assert sorted(result) == sorted(expected_books)

    def test_get_books_genre_one_book_no_genre(self):
        collector = BooksCollector()
        book_name = "Три товарища"
        collector.add_new_book(book_name)

        result = collector.get_books_genre()
        expected = {book_name: ""}
        assert result == expected

    def test_get_books_for_children_empty_collection(self):
        collector = BooksCollector()
        result = collector.get_books_for_children()
        assert result == []

    def test_add_book_in_favorites_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book("Убить пересмешника")
        collector.add_book_in_favorites("Убить пересмешника")
        assert "Убить пересмешника" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()

        book_name = "Волшебник изумрудного города"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book("Гордость и предубеждение")
        collector.add_book_in_favorites("Гордость и предубеждение")
        collector.delete_book_from_favorites("Гордость и предубеждение")
        assert "Гордость и предубеждение" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book("Маленькие женщины")
        collector.add_new_book("Джейн Эйр")
        collector.add_book_in_favorites("Маленькие женщины")
        collector.add_book_in_favorites("Джейн Эйр")

        result = collector.get_list_of_favorites_books()

        assert result == ["Маленькие женщины", "Джейн Эйр"]