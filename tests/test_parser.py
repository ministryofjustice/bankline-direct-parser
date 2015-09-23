import unittest

from bankline_parser.data_services import parse_file


class DataServicesParserTestCase(unittest.TestCase):

    def test_nwb_testfile_successful_parse(self):
        with open('tests/testfile_nwb') as f:
            output = parse_file(f)

        self.assertTrue(output.is_valid())
