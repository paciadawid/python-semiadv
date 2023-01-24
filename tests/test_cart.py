import unittest

from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.product import ProductPage


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.home_page = HomePage()
        self.product_page = ProductPage()
        self.cart_page = CartPage()
        self.checkout_page = CheckoutPage()

        self.home_page.close_ad()

    def test_total_amount_different_products(self):
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")
        self.product_page.add_item_to_cart("men tshirt")
        self.product_page.add_item_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_items_prices()))

    def tearDown(self) -> None:
        self.cart_page.close_driver()

if __name__ == '__main__':
    unittest.main()
