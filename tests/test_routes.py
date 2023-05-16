import unittest
from app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'INI page Home')

    def test_profil_route(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'INI page profile')

    def test_contact_route(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'INI page contact')
    
    def test_about_route(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'INI page about')

if __name__ == '__main__':
    unittest.main()