
"""Tests for parsing a file containing no headline
 but that contains a bold element (thanks whacked)
 You need the fr_FR.UTF-8 locale to run these tests
 """

import PyOrgMode
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestExampleOrgFile(unittest.TestCase):
    def setUp(self):
        self.tree = PyOrgMode.OrgDataStructure()
        self.tree.add_todo_state('TODO')
        self.tree.load_from_file("tags.org")
        self.todolist = self.tree.extract_todo_list()

    def test_has_three_top_level_headings(self):
        """The file has three top-level headings"""
        self.assertEqual(len(self.tree.root.content), 3)

    def test_the_first_item_has_one_tag(self):
        node = self.tree.root.content[0]
        self.assertEqual(len(node.tags), 1)
        self.assertEqual(node.heading.strip(), "First header")

    def test_the_second_item_has_two_tags(self):
        """The file has three top-level headings"""
        node = self.tree.root.content[1]

        self.assertEqual(len(node.tags), 2)
        self.assertEqual(node.tags, ["onetag", "twotag"])
        self.assertEqual(node.heading.strip(), "Second header")

    def test_third_item_has_three_tags(self):
        """The file has three top-level headings"""
        node = self.tree.root.content[2]
        self.assertEqual(len(node.tags), 3)
        self.assertEqual(node.heading.strip(), "Third header")
        self.assertEqual(node.output(), "* TODO Third header              " +
                         "                    :onetag:twotag:threetag:\n\n")


if __name__ == '__main__':
    unittest.main()
