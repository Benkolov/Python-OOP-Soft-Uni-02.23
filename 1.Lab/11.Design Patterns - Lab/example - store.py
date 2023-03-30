from abc import ABC, abstractmethod
from typing import List


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class StoreModel:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_products(self):
        return self.products


class StoreView:
    def display_products(self, products: list[Product]):
        print('Available products:')
        for product in products:
            print(f'{product.name} {product.price:.2f}')

    def get_user_input(self):
        return input('Enter product name to purchase or "exit" to quit:')

    def display_error(self, message):
        print(f'Error {message}')


class StoreController:
    def __init__(self, model: StoreModel, view: StoreView):
        self.model = model
        self.view = view

    def add_product(self, product: Product):
        self.model.add_product(product)

    def get_products(self):
        return self.model.get_products()

    def run(self):
        while True:
            products = self.get_products()
            self.view.display_products(products)
            user_input = self.view.get_user_input()
            if user_input == 'exit':
                break
            else:
                product_names = [product.name for product in products]
                if user_input in product_names:
                    product = products[product_names.index(user_input)]
                    print(f'You purchased {product.name} for ${product.price}')
                else:
                    self.view.display_error('Invalid product name')


def main():
    model = StoreModel()
    view = StoreView()
    controller = StoreController(model, view)
    controller.add_product(Product('Shirt', 20.0))
    controller.add_product(Product('Pants', 30.0))
    controller.add_product(Product('Shoes', 40.0))
    controller.run()


if __name__ == '__main__':
    main()
