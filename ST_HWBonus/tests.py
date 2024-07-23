import unittest
from main import generate_blocks, main
from unittest.mock import patch
from io import StringIO


class TestGenerateBlocks(unittest.TestCase):

    def test_bcc_mode(self):
        characteristics_dict = {
            'A': ['a1', 'a2'],
            'B': ['b1', 'b2']
        }
        mode = 'BCC'
        base_choices = {
            'A': ['a1'],
            'B': ['b1']
        }
        expected_blocks = [
            ('a1', 'b1'),
            ('a2', 'b1'),
            ('a1', 'b2')
        ]
        self.assertEqual(generate_blocks(characteristics_dict, mode, base_choices), expected_blocks)

    def test_ecc_mode(self):
        characteristics_dict = {
            'A': ['a1', 'a2'],
            'B': ['b1', 'b2']
        }
        mode = 'ECC'
        base_choices = None
        expected_blocks = [
            ('a1', 'b1'),
            ('a2', 'b2')
        ]
        self.assertEqual(generate_blocks(characteristics_dict, mode, base_choices), expected_blocks)

    def test_acoc_mode(self):
        characteristics_dict = {
            'A': ['a1', 'a2'],
            'B': ['b1', 'b2']
        }
        mode = 'ACoC'
        base_choices = None
        expected_blocks = [
            ('a1', 'b1'),
            ('a1', 'b2'),
            ('a2', 'b1'),
            ('a2', 'b2')
        ]
        self.assertEqual(generate_blocks(characteristics_dict, mode, base_choices), expected_blocks)

    def test_mbcc_mode(self):
        characteristics_dict = {
            'A': ['a1', 'a2'],
            'B': ['b1', 'b2']
        }
        mode = 'MBCC'
        # base_choices = "A=a1,A=a2,B=b1,B=b2"
        base_choices = {
            'A': ['a1', 'a2'],
            'B': ['b1', 'b2']
        }
        expected_blocks = [
            ('a1', 'b1'),
            ('a1', 'b2'),
            ('a2', 'b1'),
            ('a2', 'b2')
        ]
        self.assertEqual(generate_blocks(characteristics_dict, mode, base_choices), expected_blocks)

    def test_main(self):
        with patch('builtins.input', side_effect=['A=[a1]-B=[b1]', 'ACoC', None]), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            generated_output = fake_out.getvalue().strip()
            expected_output = "Generated blocks:\n('a1', 'b1')"
            #expected_output_formatted = expected_output.replace("Generated blocks:\n", "")
            self.assertEqual(generated_output, expected_output)


if __name__ == '__main__':
    unittest.main()
