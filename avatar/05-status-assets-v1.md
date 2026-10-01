# Status Asset Pack V1

Hasil pemeriksaan teknis terhadap `ANEMO_VTUBER_ASSET_PACK_V1` (diarsipkan di
[assets-v1/](assets-v1/)). Dokumen ini menjelaskan **kenapa pack itu tidak bisa
langsung di-rig**, supaya tidak ada yang mencoba memakainya dan kehilangan waktu.

**Diperiksa:** 2026-09-16 · 24 file PNG

---

## Kesimpulan Singkat

Pack V1 adalah **referensi desain yang bagus**, bukan asset produksi.
README aslinya sudah menyatakan ini dengan jujur:

> *"This V1 is a DESIGN/ASSET REFERENCE PACK... It is NOT yet a
> production-ready, fully separated PSD"*

Pemeriksaan teknis mengonfirmasi hal itu. Semua file adalah **hasil potong dari
satu gambar sheet 1536×1024**, bukan artwork yang digambar terpisah.

---

## Temuan 1 — Resolusi 3–13× di bawah kebutuhan

| File | Resolusi | Target | Kurang | Alpha asli |
|---|---|---|---|---|
| `01_master/character_front_reference.png` | 360×555 | 2048 | 4× | **tidak** |
| `02_expressions/expression_normal.png` | 161×213 | 2048 | 10× | ya |
| `02_expressions/expression_senyum.png` | 161×213 | 2048 | 10× | ya |
| `02_expressions/expression_tertawa.png` | 162×213 | 2048 | 10× | ya |
| `02_expressions/expression_kaget.png` | 161×213 | 2048 | 10× | ya |
| `02_expressions/expression_marah.png` | 162×213 | 2048 | 10× | ya |
| `02_expressions/expression_sedih.png` | 161×213 | 2048 | 10× | ya |
| `02_expressions/expression_malu.png` | 162×213 | 2048 | 10× | ya |
| `03_hair/hair_front.png` | 125×175 | 1024 | 6× | **tidak** |
| `03_hair/hair_back.png` | 125×175 | 1024 | 6× | **tidak** |
| `03_hair/hair_side_L.png` | 125×175 | 1024 | 6× | **tidak** |
| `03_hair/hair_side_R.png` | 130×175 | 1024 | 6× | **tidak** |
| `04_face/eye_L.png` | 135×75 | 1024 | 8× | **tidak** |
| `04_face/eye_R.png` | 140×75 | 1024 | 7× | **tidak** |
| `04_face/iris_pupil.png` | 275×65 | 1024 | 4× | **tidak** |
| `04_face/mouth_set.png` | 315×170 | 1024 | 3× | **tidak** |
| `04_face/brows.png` | 315×75 | 1024 | 3× | **tidak** |
| `05_clothing/jacket.png` | 150×155 | 2048 | 13× | **tidak** |
| `05_clothing/shirt.png` | 125×155 | 2048 | 13× | **tidak** |
| `05_clothing/neck.png` | 110×155 | 2048 | 13× | **tidak** |
| `05_clothing/ornaments.png` | 120×155 | 2048 | 13× | **tidak** |
| `06_effects/anemo_effects.png` | 360×240 | 2048 | 6× | **tidak** |
| `06_effects/background_optional.png` | 230×240 | 2048 | 9× | **tidak** |

Yang paling kritis: **mata 135×75 px**. Di stream 1080p, mata karakter akan
tampil sekitar 200–300 px. Sumbernya lebih kecil dari hasil akhirnya.

Upscale AI tidak menolong di sini — algoritma upscale menebak detail, dan pada
wajah anime tebakan itu terlihat jelas sebagai artefak (mata jadi blur, garis
lineart jadi bergelombang).

---

## Temuan 2 — Transparansi palsu

Kolom "Alpha asli" di atas: **18 dari 23 file tidak punya transparansi sama
sekali** (0% piksel beralpha nol).

Pola checkerboard abu-abu di sheet aslinya **digambar sebagai piksel**, bukan
area transparan. Saat dipotong, pola itu ikut terbawa sebagai background solid.

Pengukuran pada sheet asli:

```
alpha min/max : 1 – 253      (tidak ada 0, tidak ada 255)
piksel alpha=0 : 0 dari 1.572.864
area checkerboard : RGB 230–250  ← abu-abu terang, opaque
```

Tujuh file ekspresi punya alpha 26–29%, tapi itu artefak dari proses potong —
bukan masking yang mengikuti kontur karakter.

---

## Temuan 3 — Belum terpisah per-layer

Beberapa file masih berisi **banyak objek dalam satu gambar**:

| File | Isi | Seharusnya |
|---|---|---|
| `brows.png` | 2 alis | `Brow_L` + `Brow_R` terpisah |
| `iris_pupil.png` | 4 objek (iris ×2, pupil ×2) | 4 layer terpisah |
| `mouth_set.png` | 9 bentuk mulut | 5 layer struktural (lihat layer spec) |
| `eye_L` / `eye_R` | mata utuh | sclera, iris, pupil, kelopak, bulu mata |

---

## Temuan 4 — Tidak ada area tersembunyi

Ini yang paling menentukan. Live2D butuh part yang tertutup **digambar utuh**:
mata lengkap di balik poni, leher utuh di balik kerah, kemeja utuh di balik
jaket.

Pack V1 hanya berisi tampilan depan yang sudah "jadi" — bagian tersembunyi
memang tidak pernah ada, karena sumbernya satu gambar flat.

README V1 sendiri menyebut ini:

> *"hidden/occluded areas must be redrawn behind the moving layers"*

---

## Temuan 5 — Ekspresi tidak konsisten antar-file

Tujuh file ekspresi adalah tujuh hasil generate terpisah. Bentuk wajah, posisi
rambut, dan warna sedikit berbeda di tiap file.

Di Live2D, ekspresi dibuat dengan **mendeformasi satu model yang sama**, bukan
menukar gambar. Tujuh gambar berbeda tidak bisa jadi satu model konsisten.

---

## Yang Tetap Berguna dari V1

Nilainya nyata dan dipakai penuh di dokumen commission:

| Aset V1 | Dipakai sebagai |
|---|---|
| Sheet desain | Referensi visual untuk ilustrator |
| Struktur folder | Dasar organisasi asset |
| `layer_manifest.csv` | Dasar [03-layer-spec.md](03-layer-spec.md) |
| Daftar parameter di README | Dasar [04-rigging-spec.md](04-rigging-spec.md) |
| Warna yang terekstrak | Palet di [01-character-design.md](01-character-design.md) |
| 7 ekspresi | Daftar ekspresi yang dipesan |

Arah desainnya sudah bagus dan tidak perlu diubah — yang perlu adalah artwork
baru pada resolusi produksi.

---

## Cara Memakai V1 ke Depan

**Jangan:** pakai file `assets-v1/` sebagai asset untuk di-rig, atau upscale
lalu berharap cukup.

**Lakukan:** kirim sheet `07_references/character_design_sheet_v1.png` ke
ilustrator sebagai **referensi gaya**, bersama
[01-character-design.md](01-character-design.md) yang mengunci warna dan
[03-layer-spec.md](03-layer-spec.md) yang mengunci struktur.

---

Kembali ke: [README.md](README.md)
