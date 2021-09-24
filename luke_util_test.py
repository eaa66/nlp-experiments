import unittest
from luke_util import take_closure_over_entity_spans_to_labels


class LukeUtilTest(unittest.TestCase):

    def test_take_closure_over_entity_spans_to_labels_1(self):
        entity_spans = {
            (0, 1): 500
        }
        closure = take_closure_over_entity_spans_to_labels(entity_spans)
        expected = {
            (0, 1): 500
        }
        self.assertEqual(closure, expected)

        entity_spans = {
            (2, 4): 500
        }
        closure = take_closure_over_entity_spans_to_labels(entity_spans)
        expected = {
            (2, 3): 500,
            (3, 4): 500,
            (2, 4): 500
        }
        self.assertEqual(closure, expected)

        entity_spans = {
            (2, 4): 500, (6, 7): 501
        }
        closure = take_closure_over_entity_spans_to_labels(entity_spans)
        expected = {
            (2, 3): 500, (3, 4): 500, (2, 4): 500,
            (6, 7): 501
        }
        self.assertEqual(closure, expected)

        closure = {
            (2, 3): 500, (3, 4): 500, (2, 4): 500,
            (6, 7): 501
        }
        expected = closure
        self.assertEqual(closure, expected)


if __name__ == '__main__':
    unittest.main()
