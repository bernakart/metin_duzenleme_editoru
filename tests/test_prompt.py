import unittest
import os
import sys

# Üst dizini path'e ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from prompt import create_prompt

class TestCreatePrompt(unittest.TestCase):

    def setUp(self):
        self.dil_mesajlari = {
            "türkce": "Metni Türkçe olarak sun.",
            "ingilizce": "Metni İngilizce olarak sun."
        }
        self.tarz_mesajlari = {
            "kurumsal": "Metni profesyonel ve resmi algılanan bir dil ile yeniden yaz.",
            "hicbiri": "Metni olduğu gibi koru."
        }

    def test_turkce_kurumsal_baslik_ozet(self):
        result = create_prompt(
            self.dil_mesajlari,
            self.tarz_mesajlari,
            "türkce",
            "kurumsal",
            baslik=True,
            ozet=True
        )
        self.assertIn("Türkçe olarak sun", result)
        self.assertIn("profesyonel", result)
        self.assertIn("başlık", result)
        self.assertIn("özetle", result)

    def test_bilinmeyen_dil_tarz(self):
        result = create_prompt(
            {},
            {"hicbiri": "Metni olduğu gibi koru."},
            "bilinmeyen",
            "bilinmeyen",
            baslik=False,
            ozet=False
        )
        self.assertIn("Metni olduğu gibi koru", result)

if __name__ == '__main__':
    unittest.main()
