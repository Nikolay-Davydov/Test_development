import unittest
from Document_self import get_name, get_shelf_number, set_doc, delete_doc, new_shelf


class TestUnitTestMain(unittest.TestCase):
    def setUp(self):
       print("method setUp")

    def tearDown(self):
        print("method teardown")

    @classmethod
    def setUpClass(cls):
        print("method setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("method tearDownClass")

    def test_get_name(self):
        self.assertEqual(get_name("2207 876234"), "Василий Гупкин")

    @unittest.expectedFailure
    def test_get_name_fail(self):
        self.assertEqual(get_name("2207 876234"), "Марфа")

    def test_get_name_not_equal(self):
        self.assertNotEqual(get_name("2207 876234"), "Петя")

    # get_shelf_number

    def test_get_shelf_number(self):
        self.assertEqual(get_shelf_number("10006"), 'Документ находится на полке № : 2')

    @unittest.expectedFailure
    def test_get_shelf_number_fail(self):
        self.assertEqual(get_shelf_number("10006"), 'Документ находится на полке № : 5')

    def test_get_shelf_number_not_equal(self):
        self.assertNotEqual(get_shelf_number("10006"), 'полка')

    # set_doc
    def test_set_doc(self):
        self.assertEqual(set_doc("invoice", "1111", "Филип Подушкин", '3'), 'Документ добавлен')

    @unittest.expectedFailure
    def test_set_doc_fail(self):
        self.assertEqual(set_doc("invoice", "1111", "Филип Подушкин", '10'), 'Документ добавлен')

    def test_set_doc_not_equal(self):
        self.assertNotEqual(set_doc("invoice", "1111", "Филип Подушкин", '3'), 'Документ обновлен')

    def test_set_doc_negative(self):
        self.assertEqual(set_doc("invoice", "1111", "Филип Подушкин", '10'), 'Нет выбранной полки')

    # delete_doc
    def test_delete_doc(self):
        self.assertEqual(delete_doc("11-2"), 'Документ удален')

    @unittest.expectedFailure
    def test_delete_doc_fail(self):
        self.assertEqual(delete_doc("11-2"), 'Документ обновлен')

    def test_delete_doc_not_equal(self):
        self.assertNotEqual(delete_doc("1111"), 'Документ удален')

    def test_delete_doc_negative(self):
        self.assertEqual(delete_doc("1111"), 'Документ введен неверно')

    # new_shelf
    def test_new_shelf_negative(self):
        self.assertEqual(new_shelf('2'), 'Данная полка уже существует!')

    @unittest.expectedFailure
    def test_new_shelf_fail(self):
        self.assertEqual(new_shelf('2'), 'Создана новая полка')

    def test_new_shelf_not_equal(self):
        self.assertNotEqual(new_shelf('2'), 'Нет полки')

    def test_new_shelf(self):
        self.assertEqual(new_shelf('4'), 'Создана новая полка')
