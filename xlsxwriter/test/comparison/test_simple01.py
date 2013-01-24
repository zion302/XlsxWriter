###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013, John McNamara, jmcnamara@cpan.org
#

import unittest
import os
from ...workbook import Workbook
from ..helperfunctions import _compare_xlsx_files


class TestCreateXLSXFile(unittest.TestCase):
    """
    Test TODO.

    """
    def test_create_file(self):
        """Test TODO."""
        self.maxDiff = None

        filename = 'simple01.xlsx'
        test_dir = 'xlsxwriter/test/comparison/'
        got_filename = test_dir + '_test_' + filename
        exp_filename = test_dir + 'xlsx_files/' + filename

        ignore_members = []
        ignore_elements = {}

        workbook = Workbook(got_filename)
        worksheet = workbook.add_worksheet()

        worksheet.write_string(0, 0, 'Hello')
        worksheet.write_number(1, 0, 123)

        workbook.close()

        exp, got = _compare_xlsx_files(got_filename,
                                       exp_filename,
                                       ignore_members,
                                       ignore_elements)

        self.assertEqual(got, exp)

        # Cleanup.
        os.remove(got_filename)


if __name__ == '__main__':
    unittest.main()