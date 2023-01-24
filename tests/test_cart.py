import unittest

from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.product import ProductPage
from pages.product_details import ProductDetailsPage


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.home_page = HomePage()
        self.product_page = ProductPage()
        self.cart_page = CartPage()
        self.checkout_page = CheckoutPage()
        self.product_details_page = ProductDetailsPage()

        self.home_page.close_ad()

    def test_total_amount_different_products(self):
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")
        self.product_page.add_item_to_cart("men tshirt")
        self.product_page.add_item_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_items_prices()))

    def test_checkout_for_unlogged_user(self):
        self.product_page.add_item_to_cart("unicorn")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.cart_page.check_if_modal_visible()

    def test_10_items_for_single_product(self):
        self.login_page.login_using_email_password("seleniumremote@gmail.com", "tester")
        self.product_page.search_item("unicorn")
        self.product_page.view_product()
        self.product_details_page.add_to_cart(10)
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_items_prices()))


    def tearDown(self) -> None:
        self.cart_page.close_driver()


if __name__ == '__main__':
    unittest.main()
