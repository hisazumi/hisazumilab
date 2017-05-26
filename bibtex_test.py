import unittest

from bibtex import *

class BibtexTest(unittest.TestCase):

    def test_authors_format_en(self):
        authors = "Hirakawa, Go and Hisazumi, Kenji and Nagatsuji, Ryoichi and Nakanishi, Tsuneo and Fukuda, Akira"
        self.assertEqual(format_authors(authors),
                             'Go Hirakawa, Kenji Hisazumi, Ryoichi Nagatsuji, Tsuneo Nakanishi, Akira Fukuda')

    def test_authors_format_hazriani(self):
        authors = "Hazriani and Hisazumi, Kenji"
        self.assertEqual(format_authors(authors), 'Hazriani, Kenji Hisazumi')

        
    def test_authors_format_ja(self):
        authors = "久住, 憲嗣 and 北須賀, 輝明 and 中西, 恒夫 and 福田, 晃"
        self.assertEqual(format_authors(authors), '久住憲嗣, 北須賀輝明, 中西恒夫, 福田晃')

        
if __name__ == '__main__':
    unittest.main()
