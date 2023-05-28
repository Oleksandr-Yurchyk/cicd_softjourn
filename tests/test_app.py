import unittest

from cicd_softjourn.app import app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        expected_result = ('Hi there! This app has two endpoints: '
                           '1. /api/add - to add 2 numbers; '
                           '2. /api/multiply - to multiply 2 numbers.')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), expected_result)

    def test_add_numbers(self):
        data = {'num1': 7, 'num2': 8}
        response = self.app.post('/api/add', json=data)
        result = response.get_json().get('result', '')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result, 15)

    def test_multiply_numbers(self):
        data = {'num1': 7, 'num2': 8}
        response = self.app.post('/api/multiply', json=data)
        result = response.get_json().get('result', '')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result, 56)


if __name__ == '__main__':
    unittest.main()
