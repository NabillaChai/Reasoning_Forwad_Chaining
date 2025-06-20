# ===============================
# SISTEM DIAGNOSA PENYAKIT SEDERHANA
# DENGAN FORWARD CHAINING 
# ===============================

# 1. Fakta awal (semua premis akan terpenuhi)
fakta = ["demam", "batuk", "pilek", "nyeri otot", "sakit kepala", "mual", "sakit tenggorokan"]
print("=== INPUT: Gejala awal pasien ===")
for f in fakta:
    print(f"- {f}")

# 2. Aturan produksi (semua akan aktif)
aturan = [
    (["demam", "batuk"], "flu"),
    (["flu", "pilek"], "flu_berat"),
    (["mual", "sakit kepala"], "tipes"),
    (["sakit tenggorokan", "batuk"], "infeksi_tenggorokan"),
    (["demam", "nyeri otot"], "DBD"),
    (["flu_berat", "tipes"], "komplikasi_ringan"),
    (["DBD", "komplikasi_ringan"], "perlu_rawat_inap")
]

# 3. Variabel hasil diagnosis
hasil = []

# 4. Fungsi forward chaining
def forward_chaining(fakta, aturan):
    tahap = 1
    while True:
        triggered = False
        print(f"\n=== TAHAP {tahap}: Evaluasi Aturan ===")
        for index, (premis, kesimpulan) in enumerate(aturan):
            print(f"> Rule {index+1}: IF {premis} THEN {kesimpulan}")
            if all(p in fakta for p in premis):
                if kesimpulan not in fakta:
                    print(f"  ✔ Rule dipicu. {premis} terpenuhi → {kesimpulan} ditambahkan ke fakta.")
                    fakta.append(kesimpulan)
                    hasil.append(kesimpulan)
                    triggered = True
                else:
                    print(f"  ⟳ Rule sudah dipicu sebelumnya.")
            else:
                print(f"  ✘ Premis belum terpenuhi.")
        print(f"\nFakta saat ini: {fakta}")
        if not triggered:
            print("\n✓ Tidak ada rule yang bisa dipicu lagi. Proses forward chaining selesai.")
            break
        tahap += 1
    return hasil

# 5. Jalankan algoritma (langsung pakai fakta asli)=
print("\n=== MULAI PROSES FORWARD CHAINING ===")
hasil_akhir = forward_chaining(fakta, aturan)

# 6. Hasil akhir diagnosis
print("\n=== HASIL AKHIR DIAGNOSIS ===")
if hasil_akhir:
    for h in hasil_akhir:
        print(f"- {h.replace('_', ' ').capitalize()}")
else:
    print("Tidak ditemukan diagnosis berdasarkan gejala.")

# 7. Cetak fakta akhir untuk validasi
print("\n=== FAKTA AKHIR ===")
for f in fakta:
    print(f"- {f}")


