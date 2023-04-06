from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def test_init(self):
        cart = ShoppingCart("ShopA", 500.0)
        self.assertEqual(cart.shop_name, "ShopA")
        self.assertEqual(cart.budget, 500.0)
        self.assertEqual(cart.products, {})

    def test_invalid_shop_name(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("shopA", 500.0)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart(self):
        cart = ShoppingCart("ShopA", 500.0)
        message = cart.add_to_cart("ProductA", 50.0)
        self.assertEqual(message, "ProductA product was successfully added to the cart!")
        self.assertEqual(cart.products, {"ProductA": 50.0})

    def test_add_to_cart_expensive_product(self):
        cart = ShoppingCart("ShopA", 500.0)
        with self.assertRaises(ValueError) as ex:
            cart.add_to_cart("ProductA", 100.0)
        self.assertEqual("Product ProductA cost too much!", str(ex.exception))

    def test_remove_from_cart(self):
        cart = ShoppingCart("Shop", 500.0)
        cart.products = {"Product": 50.0}
        message = cart.remove_from_cart("Product")
        self.assertEqual(message, "Product Product was successfully removed from the cart!")
        self.assertEqual(cart.products, {})

    def test_remove_nonexistent_product(self):
        cart = ShoppingCart("ShopA", 500.0)
        cart.products = {"ProductA": 50.0}
        with self.assertRaises(ValueError) as ex:
            cart.remove_from_cart("ProductB")
            self.assertEqual(str(ex.exception), "No product with name ProductB in the cart!")

    def test_add_shopping_carts(self):
        cart1 = ShoppingCart("ShopA", 500.0)
        cart1.products = {"ProductA": 50.0}
        cart2 = ShoppingCart("ShopB", 300.0)
        cart2.products = {"ProductB": 30.0}
        cart3 = cart1 + cart2
        self.assertEqual(cart3.shop_name, "ShopAShopB")
        self.assertEqual(cart3.budget, 800.0)
        self.assertEqual(cart3.products, {"ProductA": 50.0, "ProductB": 30.0})

    def test_buy_products(self):
        cart = ShoppingCart("ShopA", 500.0)
        cart.products = {"ProductA": 50.0, "ProductB": 30.0}
        message = cart.buy_products()
        self.assertEqual(message, "Products were successfully bought! Total cost: 80.00lv.")

    def test_buy_products_over_budget(self):
        cart = ShoppingCart("ShopA", 70.0)
        cart.products = {"ProductA": 50.0, "ProductB": 30.0}
        with self.assertRaises(ValueError) as ex:
            cart.buy_products()
        self.assertEqual(str(ex.exception), "Not enough money to buy the products! Over budget with 80lv!")


if __name__ == "__main__":
    unittest.main()
