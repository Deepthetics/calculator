import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_kassapäätteen_rahamäärä_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisten_lounaiden_määrä_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_lounaiden_määrä_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_käteisellä_kasvattaa_kassapäätteen_rahamäärää_oikein_jos_maksu_on_riittävä(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaan_lounaan_osto_käteisellä_kasvattaa_kassapäätteen_rahamäärää_oikein_jos_maksu_on_riittävä(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_edullisen_lounaan_osto_käteisellä_kasvattaa_edullisten_lounaiden_määrää_oikein_jos_maksu_on_riittävä(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_osto_käteisellä_kasvattaa_maukkaiden_lounaiden_määrää_oikein_jos_maksu_on_riittävä(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_lounaan_osto_käteisellä_palauttaa_vaihtorahat_oikein_jos_maksu_on_riittävä(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_maukkaan_lounaan_osto_käteisellä_palauttaa_vaihtorahat_oikein_jos_maksu_on_riittävä(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_edullisen_lounaan_osto_ei_muuta_kassapäätteen_rahamäärää_jos_maksu_ei_ole_riittävä(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
 
    def test_maukkaan_lounaan_osto_käteisellä_ei_muuta_kassapäätteen_rahamäärää_jos_maksu_ei_ole_riittävä(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_osto_käteisellä_ei_muuta_lounaiden_määrää_jos_maksu_ei_ole_riittävä(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_osto_käteisellä_ei_muuta_lounaiden_määrää_jos_maksu_ei_ole_riittävä(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_käteisellä_palauttaa_kaikki_rahat_jos_maksu_ei_ole_riittävä(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_maukkaan_lounaan_osto_käteisellä_palauttaa_kaikki_rahat_jos_maksu_ei_ole_riittävä(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_edullisen_lounaan_osto_kortilla_vähentää_kortin_saldoa_oikein_jos_kortilla_on_tarpeeksi_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_maukkaan_lounaan_osto_kortilla_vähentää_kortin_saldoa_oikein_jos_kortilla_on_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_edullisen_lounaan_osto_kortilla_kasvattaa_edullisten_lounaiden_määrää_oikein_jos_kortilla_on_tarpeeksi_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_osto_kortilla_kasvattaa_maukkaiden_lounaiden_määrää_oikein_jos_kortilla_on_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisen_lounaan_osto_kortilla_palauttaa_true_jos_kortilla_on_tarpeeksi_saldoa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaan_lounaan_osto_kortilla_palauttaa_true_jos_kortilla_on_tarpeeksi_saldoa(self):
         self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_edullisen_lounaan_osto_kortilla_ei_vähennä_kortin_saldoa_jos_kortilla_ei_ole_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_maukkaan_lounaan_osto_kortilla_ei_vähennä_kortin_saldoa_jos_kortilla_ei_ole_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_edullisen_lounaan_osto_kortilla_ei_muuta_edullisten_lounaiden_määrää_jos_kortilla_ei_ole_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_osto_kortilla_ei_muuta_maukkaiden_lounaiden_määrää_jos_kortilla_ei_ole_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)
    
    def test_edullisen_lounaan_osto_kortilla_palauttaa_false_jos_kortilla_ei_ole_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_maukkaan_lounaan_osto_kortilla_palauttaa_false_jos_kortilla_ei_ole_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_rahan_lataaminen_kortille_kasvattaa_kassapäätteen_rahamäärää_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_rahan_lataaminen_kortille_kasvattaa_kortin_saldoa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")        

    def test_negatiivisen_rahamäärän_lataaminen_ei_muuta_kassapääteen_rahamäärää(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_negatiivisen_rahamäärän_lataaminen_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")     
