import unittest

from name_function import get_format_name

class NamesTestCase(unittest.TestCase):
    """ тесты для имени """
    def test_first_last(self):
        form_name = get_format_name('semen', 'semenov')
        self.assertEqual(form_name, 'Semen Semenov')
    def test_first_last_otch(self):
        form_name = get_format_name('semen', 'semenov', 'semenovich')
        self.assertEqual(form_name, 'Semen Semenov', 'Semenovich')