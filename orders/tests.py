from customers.tests.test_setup import TestSetUp
# Create your tests here.


class TestOrder(TestSetUp):
    def test_user_can_see_their_orders(self):
        res = self.client.get(self.orders_url)
        self.assertEqual(res.status_code, 200)


