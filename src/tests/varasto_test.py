import unittest
from varasto import Varasto

#test comment

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    
    def test_konstruktori_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_nolla_tilavuus(self):
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_alku_saldo_negatiivinen(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_konstruktori_alku_saldo_suurempi_kuin_tilavuus(self):
        varasto = Varasto(10, 20)
        self.assertAlmostEqual(varasto.saldo, 10)
        self.assertAlmostEqual(varasto.tilavuus, 10)

    def test_konstruktori_alku_saldo_yhtaa_kuin_tilavuus(self):
        varasto = Varasto(10, 10)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisaa_varastoon_yliksi(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisaa_varastoon_tasan_mahtuu(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.lisaa_varastoon(7)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(saatu, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_varastosta_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(3)
        saatu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu, 3)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ota_varastosta_tasan_paljonko_on(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ota_varastosta_vahan(self):
        self.varasto.lisaa_varastoon(10)
        saatu = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(saatu, 3)
        self.assertAlmostEqual(self.varasto.saldo, 7)

    def test_str_representation(self):
        self.varasto.lisaa_varastoon(5)
        result = str(self.varasto)
        self.assertIn("saldo = 5", result)
        self.assertIn("vielä tilaa 5", result)

    def test_paljonko_mahtuu(self):
        self.varasto.lisaa_varastoon(3)
        mahtuu = self.varasto.paljonko_mahtuu()
        self.assertAlmostEqual(mahtuu, 7)
