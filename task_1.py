import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            'чипсы': 50,
            'кола': 100,
            'печенье': 45,
            'молоко': 55,
            'кефир': 70
        }
        self.__tax_rate = {
            'чипсы': 20,
            'кола': 20,
            'печенье': 20,
            'молоко': 10,
            'кефир': 10
        }

    # Геттер для списка товаров
    @property
    def name_items(self):
        return self.__name_items

    # Геттер для количества товаров
    @property
    def number_items(self):
        return self.__number_items

    # Добавление товара в чек
    def add_item_to_cheque(self, name):

        if len(name) == 0 or len(name) > 40:
            raise ValueError(
                'Нельзя добавить товар, если в его названии нет символов или их больше 40'
            )

        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1

    # Удаление товара из чека
    def delete_item_from_check(self, name):

        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')

        self.__name_items.remove(name)
        self.__number_items -= 1

    # Подсчёт общей суммы
    def check_amount(self):

        total = []

        for item in self.__name_items:
            total.append(self.__item_price[item])

        amount = sum(total)

        if self.__number_items > 10:
            return amount * 0.9

        return amount

    # НДС 20%
    def twenty_percent_tax_calculation(self):

        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)

        for item in twenty_percent_tax:
            total.append(self.__item_price[item])

        tax = sum(total) * 0.2

        if self.__number_items > 10:
            return tax * 0.9

        return tax

    # НДС 10%
    def ten_percent_tax_calculation(self):

        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)

        for item in ten_percent_tax:
            total.append(self.__item_price[item])

        tax = sum(total) * 0.1

        if self.__number_items > 10:
            return tax * 0.9

        return tax

    # Общая сумма НДС
    def total_tax(self):
        return (
            self.ten_percent_tax_calculation() +
            self.twenty_percent_tax_calculation()
        )

    # Статический метод для телефона
    @staticmethod
    def get_telephone_number(telephone_number):

        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        if len(str(telephone_number)) > 10:
            raise ValueError(
                'Необходимо ввести 10 цифр после "+7"'
            )

        return f'+7{telephone_number}'



collector = OnlineSalesRegisterCollector()

collector.add_item_to_cheque('кола')
collector.add_item_to_cheque('молоко')

print(collector.name_items)
print(collector.number_items)
print(collector.check_amount())
print(collector.total_tax())
print(collector.get_telephone_number(9991234567))