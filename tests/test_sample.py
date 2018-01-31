import unittest
from galeria.galeria.spiders import loaders
from .responses import fake_response_from_file

class LoadersSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = loaders.BasicSpider()

    def _test_item_results(self, results, expected_length):
        count = 0
        permalinks = set()
        for item in results:
            self.assertIsNotNone(item['text'])
        self.assertEqual(count, expected_length)

    def test_parse(self):
        response = fake_response_from_file('input.html')
        item = self.spider.parse(response)
        self._test_item_results(item, 1)