class SiswaSIJA:
    def __init__(self, nama, angkatan):
        self.nama = nama
        self.jurusan = "SIJA"
        self.sekolah = "SMKN 7 Semarang"
        self.angkatan = angkatan

    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari jurusan {self.jurusan} angkatan {self.angkatan} di {self.sekolah}.")
