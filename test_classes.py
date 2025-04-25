from src.classes import SiswaSIJA

def test_inisialisasi_siswa():
    siswa = SiswaSIJA("Rakha", 27)
    assert siswa.nama == "Rakha"
    assert siswa.jurusan == "SIJA"
    assert siswa.sekolah == "SMKN 7 Semarang"
    assert siswa.angkatan == 27

def test_output_perkenalan(capfd):
    siswa = SiswaSIJA("Rakha", 27)
    siswa.perkenalan()
    out, _ = capfd.readouterr()
    assert out.strip() == "Halo, saya Rakha dari jurusan SIJA angkatan 27 di SMKN 7 Semarang."
