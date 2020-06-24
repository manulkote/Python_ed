from unittest import TestCase


class TestClient(TestCase):

    def test_port(self):
        self.assertEqual(type(port), type(0))

    def test_port_value(self):
        self.assertNotIn(port, range(1, 1024))

    def test_responce(self):
        self.assertEqual(data, type(b''))
