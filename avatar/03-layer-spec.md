# Layer Spec — Struktur PSD

Struktur layer yang harus diikuti ilustrator. Penamaan ini dipakai persis
supaya rigger tidak perlu menebak.

**Kanvas:** 4096 × 4096 px · RGB 8-bit · 350 DPI

---

## Aturan Umum

1. Urutan di bawah ditulis dari **paling depan ke paling belakang** — sama
   seperti urutan layer di Photoshop (atas = depan).
2. Satu part = satu layer. **Tidak ada penggabungan.**
3. Semua layer sudah di-rasterize, alpha asli, tanpa layer effect.
4. Nama layer **persis** seperti tertulis (case-sensitive, pakai underscore).
5. Part yang tertutup tetap digambar utuh — lihat kolom "Occlusion".

---

## Struktur Lengkap

```
ROOT
│
├── 06_FX/                          efek, paling depan
│   ├── FX_Glow_Front
│   ├── FX_Particle_01
│   ├── FX_Particle_02
│   └── FX_Wind_Front
│
├── 01_HAIR_FRONT/                  poni — WAJIB dipecah per helai
│   ├── HairFront_01               (helai paling kiri)
│   ├── HairFront_02
│   ├── HairFront_03               (tengah)
│   ├── HairFront_04
│   └── HairFront_05               (helai paling kanan)
│
├── 02_FACE/
│   │
│   ├── BROW/
│   │   ├── Brow_L
│   │   └── Brow_R
│   │
│   ├── EYE_L/                      urutan dalam grup: depan → belakang
│   │   ├── EyeLash_L              bulu mata atas
│   │   ├── EyeLid_Upper_L         kelopak atas (warna kulit)
│   │   ├── EyeLid_Lower_L         kelopak bawah
│   │   ├── EyeHighlight_L         highlight putih
│   │   ├── Pupil_L
│   │   ├── Iris_L
│   │   └── EyeWhite_L             sclera — digambar UTUH
│   │
│   ├── EYE_R/                      cermin dari EYE_L
│   │   ├── EyeLash_R
│   │   ├── EyeLid_Upper_R
│   │   ├── EyeLid_Lower_R
│   │   ├── EyeHighlight_R
│   │   ├── Pupil_R
│   │   ├── Iris_R
│   │   └── EyeWhite_R
│   │
│   ├── MOUTH/
│   │   ├── Mouth_Line             garis bibir / outline
│   │   ├── Teeth_Upper
│   │   ├── Tongue
│   │   ├── Teeth_Lower
│   │   └── Mouth_Inside           rongga mulut (gelap)
│   │
│   ├── Nose
│   ├── Blush                      untuk ekspresi malu (default hidden)
│   └── Face_Base                  wajah + dahi UTUH
│
├── 03_HEAD/
│   ├── Ear_L                      digambar UTUH
│   ├── Ear_R                      digambar UTUH
│   ├── HairSide_L
│   ├── HairSide_R
│   └── Head_Base                  bentuk kepala di balik wajah
│
├── 04_BODY/
│   ├── Accessory_Chest            liontin/kalung, kristal cyan
│   ├── Ornament_Shoulder_L
│   ├── Ornament_Shoulder_R
│   ├── Jacket_Collar
│   ├── Jacket_L
│   ├── Jacket_R
│   ├── Shirt                      digambar UTUH di balik jaket
│   ├── Neck                       digambar UTUH sampai pangkal
│   └── Body_Base                  bahu & dada
│
├── 05_HAIR_BACK/
│   ├── HairBack_01
│   ├── HairBack_02
│   └── HairBack_03
│
└── 07_BG/                         opsional, paling belakang
    └── BG_Atmosphere
```

---

## Catatan Per-Bagian

### Rambut depan (`01_HAIR_FRONT`)

Pemecahan per helai **wajib**, bukan opsional. Satu layer poni utuh tidak bisa
diberi physics yang natural — hasilnya bergerak kaku seperti papan.

Tiap helai punya titik jangkar di kulit kepala, ujungnya bebas bergerak.
Helai tengah (`HairFront_03`) biasanya paling pendek geraknya.

### Mata (`EYE_L` / `EYE_R`)

`EyeWhite` harus **elips penuh**, bukan bentuk mata yang terlihat. Saat mata
bergerak ke samping, bagian sclera yang tadinya tertutup jadi terlihat.

`Iris` dan `Pupil` dipisah supaya bisa ada efek pupil membesar/mengecil pada
ekspresi kaget.

`EyeLid_Upper` diwarnai **kulit**, bukan transparan — saat berkedip, kelopak
ini turun menutupi mata.

### Mulut (`MOUTH`)

Lima layer ini cukup untuk lip sync penuh A/I/U/E/O. Rigger membentuk vokal
lewat deformasi, bukan lewat mengganti gambar.

`Mouth_Inside` adalah rongga gelap yang terlihat saat mulut terbuka — warnanya
gelap kemerahan, bukan hitam murni.

### Telinga (`Ear_L` / `Ear_R`)

Sering terlewat karena tertutup rambut di tampilan depan. Tapi saat kepala
menoleh ±30°, telinga di sisi yang berlawanan jadi terlihat.

### Leher (`Neck`)

Digambar sampai pangkal (tulang selangka), bukan hanya bagian yang terlihat di
atas kerah. Saat kepala mendongak, leher yang tadinya tertutup akan terlihat.

---

## Checklist Ilustrator

Sebelum menyerahkan PSD:

- [ ] Kanvas 4096 × 4096, RGB 8-bit, 350 DPI
- [ ] Semua nama layer persis sesuai spec
- [ ] Tidak ada layer yang berisi lebih dari satu objek
- [ ] Alpha channel asli (cek: matikan semua layer → kanvas benar-benar kosong)
- [ ] Tidak ada layer style / adjustment layer / smart object
- [ ] Tidak ada clipping mask yang belum di-apply
- [ ] Semua part occluded digambar utuh (mata, dahi, telinga, leher, kemeja)
- [ ] Poni terpecah minimal 3 grup helai
- [ ] `EyeWhite` berbentuk elips penuh
- [ ] Gigi & lidah terpisah di belakang mulut
- [ ] Palet warna sesuai [01-character-design.md](01-character-design.md)
- [ ] Emblem original — tidak ada elemen IP pihak lain

---

Lanjut ke: [04-rigging-spec.md](04-rigging-spec.md)
