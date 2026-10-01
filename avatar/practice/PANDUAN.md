# Panduan Latihan Rigging — practice.psd

File latihan untuk belajar rigging di **Live2D Cubism 5.3** yang sudah terpasang
di PC kamu.

Gambarnya sengaja dibuat sederhana (bentuk geometris). Yang penting di sini
bukan seninya, tapi **strukturnya** — persis seperti PSD produksi yang benar.
Setelah paham alurnya di file ini, kamu akan tahu apa yang harus dicek saat
menerima PSD dari artist nanti.

---

## Isi Folder

| File | Keterangan |
|---|---|
| `practice.psd` | PSD latihan — 2048×2048, 45 layer |
| `_preview.png` | Tampilan hasil composite |
| `build_practice.py` | Script pembuatnya — bisa diubah & dijalankan ulang |

Untuk mengubah gambar (warna, bentuk, posisi), edit `build_practice.py` lalu:

```
python build_practice.py
```

---

## Kenapa PSD Ini Benar

Tiga hal yang membedakannya dari `assets-v3`:

**1. Posisi anatomis.** `Iris_L` berada di (833, 655), tepat di dalam
`EyeWhite_L` di (784, 640). Di V3, semua part berjejer di kolom x=760 —
koordinat grid sheet, bukan posisi wajah.

**2. Area tersembunyi digambar utuh.**

- `EyeWhite_L/R` = elips penuh, bukan bentuk mata yang terlihat
- `Face_Base` = wajah + dahi utuh, tidak berlubang di balik poni
- `Ear_L/R` = telinga utuh, walau tertutup rambut
- `Neck` = leher sampai pangkal, bukan cuma yang terlihat di atas kerah
- `Shirt` = kemeja utuh di balik jaket
- `Mouth_Inside`, `Teeth_Upper/Lower`, `Tongue` = ada semua di balik `Mouth_Line`

**3. Poni terpecah 3 helai** — `HairFront_01/02/03`. Satu layer poni utuh
tidak bisa diberi physics yang natural.

Untuk membuktikan sendiri: buka `practice.psd` di Photoshop/Photopea, matikan
layer `HairFront_*` → dahi tetap utuh. Matikan `EyeLid_Upper_L` → mata lengkap.
Coba hal yang sama pada `assets-v3` — tidak ada yang tersisa di baliknya.

---

## Langkah Rigging

### 1. Impor

Buka Cubism → **File → New** → tarik `practice.psd` ke kanvas.

Cubism akan memuat 45 layer jadi ArtMesh. Kalau ada dialog resolusi tekstur,
pilih **2048×2048**.

> Kalau gagal impor, kemungkinan file rusak. `practice.psd` sudah diverifikasi
> parse bersih, jadi seharusnya aman.

### 2. Atur Mesh

Klik satu ArtMesh → panel **Mesh** → **Auto Mesh Generation**.

| Jenis part | Preset | Alasan |
|---|---|---|
| Wajah, badan | Standard | Deformasi luas |
| Mata, mulut | Detail | Butuh presisi |
| Rambut | Standard | Physics |
| Ornamen logam | Rough | Hampir tidak berubah bentuk |

**Urutan kerja yang benar:** mesh dulu untuk semua part, baru masuk parameter.
Mengubah mesh setelah membuat deformasi akan merusak hasil kerja.

### 3. Deformer

Buat **Warp Deformer** berlapis, dari luar ke dalam:

```
D_Root                    seluruh karakter
└── D_Body                badan, jaket, ornamen
    └── D_Head            semua bagian kepala
        ├── D_Face        wajah, mata, alis, mulut, hidung
        │   ├── D_Eye_L   EyeWhite/Iris/Pupil/Highlight/Lid/Lash kiri
        │   ├── D_Eye_R   yang kanan
        │   └── D_Mouth   semua layer mulut
        ├── D_HairFront   3 helai poni
        ├── D_HairSide    rambut samping
        └── D_HairBack    rambut belakang
```

Cara: pilih beberapa ArtMesh → klik kanan → **Create Warp Deformer**.

Kenapa berlapis: menggerakkan `D_Head` otomatis menggerakkan semua isinya.
Tanpa ini, kamu harus menganimasikan 40+ part satu per satu.

### 4. Parameter

Buka panel **Parameter**. Mulai dari yang paling mudah:

#### ParamEyeLOpen (latihan pertama — paling sederhana)

1. Pilih parameter `ParamEyeLOpen`, set nilai ke **1** (mata terbuka)
2. Klik **Add Key** (ikon kunci)
3. Geser nilai ke **0**
4. Klik **Add Key** lagi
5. Dalam keadaan nilai 0, turunkan `EyeLid_Upper_L` sampai menutupi mata
6. Geser slider 0↔1 → mata berkedip

Ulangi untuk `ParamEyeROpen`.

#### ParamEyeBallX / Y

Nilai -1 / 0 / +1. Geser `Iris_L`, `Pupil_L`, `EyeHighlight_L` (dan yang R)
ke arah yang sesuai.

> Di sinilah `EyeWhite` elips penuh terbukti berguna — iris bisa bergeser tanpa
> keluar dari sclera.

#### ParamMouthOpenY

Nilai 0 → 1. Pada nilai 1, buka `Mouth_Line` sehingga
`Mouth_Inside`, gigi, dan lidah terlihat.

#### ParamAngleX (kepala menoleh — paling sulit)

Nilai -30 / 0 / +30. Pada -30 dan +30, geser `D_Head` ke samping **dan**
sesuaikan perspektifnya: bagian yang menjauh menyempit, yang mendekat melebar.

Ini bagian tersulit dan wajar kalau butuh beberapa kali percobaan. Mulai dengan
gerakan kecil dulu (±10), setelah terbiasa baru perbesar.

**Urutan yang disarankan:**

```
EyeOpen → EyeBall → Brow → MouthOpen → MouthForm
→ AngleZ (miring) → AngleX (menoleh) → AngleY (angguk)
→ BodyAngle → Breath
```

Dari yang paling gampang ke paling sulit. Jangan mulai dari AngleX.

### 5. Physics

Menu **Modeling → Physics & Scene Blend Settings**.

Buat grup physics:

| Grup | Input | Output | Sifat |
|---|---|---|---|
| Poni | `ParamAngleX`, `ParamAngleZ` | `ParamHairFront` | gerak kecil, redam tinggi |
| Rambut samping | `ParamAngleX`, `ParamAngleZ` | `ParamHairSide` | gerak sedang |
| Rambut belakang | `ParamAngleX`, `ParamBodyAngleX` | `ParamHairBack` | gerak besar, lambat |

Beri **delay sedikit berbeda** tiap grup — rambut yang bergerak serempak
terlihat artifisial.

### 6. Ekspresi

Panel **Expression** → buat 7 ekspresi sesuai
[../04-rigging-spec.md](../04-rigging-spec.md):

Normal · Senyum · Tertawa · Kaget · Marah · Sedih · Malu

Nilai parameter tiap ekspresi sudah tertulis di dokumen itu.

### 7. Ekspor

**File → Export → Export for Runtime → moc3**

Centang: `.moc3`, `.model3.json`, texture, `.physics3.json`, `.exp3.json`

Simpan ke folder sendiri, lalu muat di VTube Studio untuk diuji.

---

## Kesalahan Umum

| Kesalahan | Akibat | Cara hindari |
|---|---|---|
| Mengubah mesh setelah bikin deformasi | Deformasi rusak | Selesaikan semua mesh dulu |
| Deformer tidak berlapis | Harus animasi part satu-satu | Buat hirarki dari awal |
| Langsung kerjakan AngleX | Frustrasi | Mulai dari EyeOpen |
| Physics terlalu kuat | Rambut bergetar terus | Naikkan redaman |
| Lupa simpan `.cmo3` | Kerja hilang | Ctrl+S sering |
| Kelopak mata transparan | Mata hilang saat kedip | Kelopak harus warna kulit |

---

## Catatan Setup Cubism

Dari log Cubism di PC kamu:

**Pen tablet tidak aktif.**

```
jpen-2-3-64 couldn't be loaded
no suitable JNI library found
```

Kalau punya tablet (Wacom/Huion), tekanan pen tidak terbaca. Untuk rigging ini
tidak masalah — mayoritas rigger pakai mouse. Kalau mau diperbaiki, install
driver tablet lalu jalankan ulang Cubism.

**GPU terdeteksi benar:** NVIDIA RTX 5060 (driver 616.64). Tidak ada masalah
performa.

**Versi:** Cubism Editor 5.3.04

---

## Setelah Selesai Latihan

Kamu akan paham:

- Kenapa area tersembunyi wajib digambar
- Kenapa poni harus dipecah
- Kenapa `EyeWhite` harus elips penuh
- Berapa lama rigging sebenarnya memakan waktu

Itu semua berguna saat:

1. **Menilai penawaran artist** — kamu tahu apa yang wajar
2. **QA hasil komisi** — pakai [../07-qa-checklist.md](../07-qa-checklist.md)
3. **Memutuskan** apakah mau rigging sendiri atau komisi

> Beberapa orang memutuskan rigging sendiri setelah latihan ini, dan hanya
> mengomisikan ilustrasinya. Itu memangkas biaya 40–50%. Tapi rigging yang
> bagus butuh latihan berminggu-minggu — pertimbangkan waktu kamu juga.

---

## Referensi

- Manual resmi: https://docs.live2d.com/cubism-editor-manual/top/
- Tutorial video: cari "Live2D rigging tutorial" di YouTube
- [../03-layer-spec.md](../03-layer-spec.md) — struktur layer produksi
- [../04-rigging-spec.md](../04-rigging-spec.md) — parameter lengkap
- [../07-qa-checklist.md](../07-qa-checklist.md) — checklist QA

---

Kembali ke: [../README.md](../README.md)
