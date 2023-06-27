class Automobile:

    def __init__(self, model=None, year_create=None,  mfr=None, capacity_engine=None, color=None, price=None, segment=None):
        self.model = model
        self.year_create = year_create
        self.mfr = mfr
        self.capacity_engine = capacity_engine
        self.color = color
        self.price = price
        self.segment = segment

    def input_data(self):
        self.model = input('Введіть модель авто ')
        self.year_create = input('Введіть рік випуску авто ')
        self.mfr = input('Введіть виробника авто ')
        self.capacity_engine = input("Введіть об'єм авто ")
        self.color = input('Введіть колір авто ')
        self.price = int(input('Введіть price авто '))
        self.segment = input('''Введіть сегмент авто:
        1. Casual
        2. Premium
        ''')

    def output_data(self):
        print(f'Модель авто: {self.model}')
        print(f"Рік випуску: {self.year_create}")
        print(f'Виробник: : {self.mfr}')
        print(f"Об'єм авто: : {self.capacity_engine}")
        print(f'Колір: : {self.color}')
        print(f'Звичайна ціна: : {self.price}')
        # print(type(self.segment))

    def update_price(self):
        if self.segment == '2':
            self.price += 2000
            print(f'Преміум сегмент коштує {self.price}')


samohud = Automobile()
samohud.input_data()
samohud.output_data()
samohud.update_price()
print("------------------")

# # --2
class Book:

    # def __init__(self, name=None, year, production, genre, autor, price):
    def __init__(self, name=None, year=None, production=None, genre=None, autor=None, price=None):
        self.name = name
        self.year = year
        self.production = production
        self.genre = genre
        self.autor = autor
        self.price = price

    def input_data(self):
        self.name = input('Введіть назву книги ')
        self.year= input('Введіть рік видання книги ')
        self.production = input('Введіть видавництво ')
        self.genre = input('Введіть жанр книги ')
        self.autor = input('Введіть автора книги ')
        self.price = int(input('Введіть ціну книги '))

    def output_data(self):
        print(f'Назва книги: {self.name}. Автор {self.autor}. Жанр: {self.genre}.')
        print(f"Рік видання: {self.year}. Видавництво: {self.production} ")
        print(f'Ціна книги становить: {self.price}')

    def update_price(self, count=150):
        if self.production == 'Lviv':
            self.price += count
        print(f'Ціна книги за видавництвом "{self.production}" коштує {self.price}')


book1 = Book()
book1.input_data()
book1.output_data()
book1.update_price()
print("------------------")

# ---3
class Stadium:

    def __init__(self, name=None, date_open=None, country=None, city=None, count_place=None):
        self.name = name
        self.date_open = date_open
        self.country = country
        self.city = city
        self.count_place = count_place
        self.podii = []

    def input_data(self):
        self.name = input('Введіть назву cтадіону ')
        self.date_open= input('Введіть рік видкриття ')
        self.country = input('Введіть страну розташування стадіону ')
        self.city = input('Введіть місто ')
        self.count_place = int(input('Введіть кількість місць на стадіоні '))

    def new_event(self, smth):
        if smth in (self.podii):
            print(f'Така подія вже є')
        else:
            self.podii.append(smth)
            print(f'Подія {self.podii} додана до програми')


    def output_data(self):
        print(f'Стадіон {self.name} знаходиться в {self.city}, {self.country}. Був відкритий у {self.date_open}.\nКількість місць для сидіння становить {self.count_place}')


place = Stadium()
place.input_data()
place.output_data()
place.new_event('Політичні дебати')


