import unittest
import Yandex

TOKEN = 'ya_token'
class TestYandex(unittest.TestCase):
    def setUp(self):
        print("method setUp")
        self.ya = Yandex.YandexDisk(token=TOKEN)

    def tearDown(self):
        print("method teardown")
        self.ya.dispose()

    @classmethod
    def setUpClass(cls):
        print("method setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("method tearDownClass")

    def test_create_folder(self):
        folder_name = 'test_folder'
        self.assertTrue(self.ya.is_not_exist_folder(folder_name))
        self.assertEqual(self.ya.create_folder(folder_name), 'Создание папки на Yandex диске')
        self.assertFalse(self.ya.is_not_exist_folder(folder_name))

    def test_create_folder_negative(self):
        folder_name = 'test_folder'
        self.assertTrue(self.ya.is_not_exist_folder(folder_name))
        self.assertEqual(self.ya.create_folder(folder_name), 'При попытке создания папки на Yandex диск произошла ошибка, проверьте токен Yandex.')
        self.assertTrue(self.ya.is_not_exist_folder(folder_name))
