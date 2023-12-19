class LibraryItem:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Title: {self.title}"

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

class Magazine(LibraryItem):
    def __init__(self, title, issue):
        super().__init__(title)
        self.issue = issue

    def __str__(self):
        return f"Title: {self.title}, Issue: {self.issue}"

class DVD(LibraryItem):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}"

class LibraryItemFactory:
    @staticmethod
    def create_item(item_type, **kwargs):
        if item_type == "book":
            return Book(kwargs.get("title"), kwargs.get("author"))
        elif item_type == "magazine":
            return Magazine(kwargs.get("title"), kwargs.get("issue"))
        elif item_type == "dvd":
            return DVD(kwargs.get("title"), kwargs.get("director"))
        else:
            raise ValueError("Invalid item type")

# Приклад використання фабрики для створення об'єктів в бібліотеці
if __name__ == "__main__":
    factory = LibraryItemFactory()

    # Створення книги за допомогою фабрики
    book = factory.create_item("book", title="The Great Gatsby", author="F. Scott Fitzgerald")
    print(book)  # Виведе інформацію про книгу

    # Створення журналу за допомогою фабрики
    magazine = factory.create_item("magazine", title="National Geographic", issue="December 2023")
    print(magazine)  # Виведе інформацію про журнал

    # Створення DVD за допомогою фабрики
    dvd = factory.create_item("dvd", title="Inception", director="Christopher Nolan")
    print(dvd)  # Виведе інформацію про DVD
