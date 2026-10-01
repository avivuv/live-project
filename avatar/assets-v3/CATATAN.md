# Catatan Asset V3

Arsip `ANEMO_VTUBER_LIVE2D_V3.psd` beserta hasil pemeriksaannya.

**Diperiksa:** 2026-09-16

---

## Isi Folder

| File | Keterangan |
|---|---|
| `ANEMO_VTUBER_LIVE2D_V3_original.psd` | File asli — **tidak bisa dibuka Cubism** |
| `ANEMO_VTUBER_LIVE2D_V3_fixed.psd` | Sudah diperbaiki — bisa dibuka |
| `v3_composite_preview.png` | Tampilan composite |
| `v3_layers_contact_sheet.png` | Semua 45 layer dalam satu lembar |

---

## Perbaikan yang Dilakukan

File asli ditolak Cubism dengan error:

```
com.live2d.graphics.psd.a: error signature :: @ 0x00000026
```

Dua masalah struktural ditemukan:

**1. Panjang LayerMask salah (3 byte).**

```
LayerMask menyatakan : 861787 byte  (berakhir di offset 861825)
LayerInfo sebenarnya : 861784 byte  (berakhir di offset 861822)
```

Tiga byte ImageData tercaplok ke dalam blok LayerMask. Diperbaiki dengan
mengoreksi nilai panjang di offset 34.

**2. ImageData preview terpotong.**

```
tersedia   : 1.966.061 byte
dibutuhkan : 4.194.304 byte
```

Gambar preview flatten tidak lengkap. Diganti dengan preview kosong yang valid
(ini hanya thumbnail, tidak memengaruhi data layer).

Hasil: `ANEMO_VTUBER_LIVE2D_V3_fixed.psd` — parse bersih, 45 layer utuh.

---

## Kenapa Tetap Belum Bisa Di-rig

File yang sudah diperbaiki **bisa dibuka**, tapi isinya belum layak untuk
produksi.

### Posisi part salah

Semua layer mulai di **x = 760**, dengan y berulang di **20, 215, 410, 605,
800** — lima slot yang berputar.

Itu koordinat grid pada sheet desain, bukan posisi anatomis. Di PSD Live2D yang
benar, mata harus berada di posisi mata pada wajah.

Bandingkan dengan `../practice/practice.psd`:

| | V3 | practice.psd |
|---|---|---|
| `EyeWhite_L` / iris | semua di x=760 | (784,640) |
| `Iris_L` | semua di x=760 | (833,655) — **di dalam** sclera |

Untuk memakai V3, rigger harus memindahkan 45 layer satu per satu ke posisi
yang benar — pekerjaan yang lebih lama daripada menggambar ulang.

### Ukuran part terlalu kecil

| | Ukuran |
|---|---|
| Terbesar | 222×180 px |
| **Median** | **85×70 px** |
| Terkecil | 30×38 px |

Target produksi: 512–2048 px per part. Bahkan lebih kecil dari V1.

### Ada teks dan border ikut terpotong

Hasil zoom pada beberapa layer:

- **L13** — berisi tulisan **"Highlight L"** (label sheet, bukan gambar highlight)
- **L45** — berisi caption **"Background (Separate)"** dan bingkai kartu
- **L1** — wajah dengan **pola checkerboard tergambar sebagai piksel**
- **L8, L25** — ada garis potong dan border cyan ikut terbawa

### Ada duplikasi

| Layer | Jumlah piksel |
|---|---|
| L39, L40, L41 | 6175 (identik) |
| L42, L43, L44 | 7600 (identik) |

Sama persis bentuknya, hanya beda warna.

### Penamaan generik

Semua layer bernama `L1`–`L45`. Tidak ada informasi part mana yang mana.

### Masih branded Genshin

Composite menampilkan teks **"GENSHIN IMPACT INSPIRED VTUBER CHARACTER"**.
Lihat [../01-character-design.md](../01-character-design.md) untuk keputusan
retheme.

---

## Yang Membaik dari V1

V3 menunjukkan kemajuan nyata:

| Aspek | V1 | V3 |
|---|---|---|
| Format | PNG terpisah | **PSD berlayer** ✅ |
| Transparansi | palsu (checkerboard) | **alpha asli** ✅ |
| Cakupan part | 23 file | **45 layer** ✅ |
| Telinga | tidak ada | **ada** ✅ |
| Badan utuh | tidak ada | **ada** ✅ |
| Background terpisah | ada | ada ✅ |

Layer inventory-nya benar — menunjukkan pemahaman struktur Live2D yang tepat.
Yang belum tercapai adalah resolusi dan penempatan.

---

## Batas Jalur "Generate Sheet lalu Potong"

V1 dan V3 sama-sama dibuat dengan cara ini, dan keduanya mentok di tempat yang
sama:

1. Part yang dihasilkan selalu **seukuran thumbnail** — karena sumbernya satu
   gambar dengan banyak kotak
2. **Tidak pernah ada area tersembunyi** — sheet hanya menampilkan tampilan
   depan yang sudah jadi
3. **Label dan border ikut terpotong** — karena ikut tergambar di sheet

Menaikkan resolusi sheet tidak menyelesaikan poin 2, dan itu yang paling
menentukan untuk Live2D.

---

## Cara Memakai V3

**Berguna untuk:**

- Referensi visual — arah desainnya sudah matang
- Acuan layer inventory saat brief ke artist
- Dibuka di Cubism untuk melihat sendiri kenapa belum bisa dipakai

**Tidak untuk:** di-rig langsung, atau di-upscale lalu dipakai.

Untuk latihan rigging, pakai [`../practice/practice.psd`](../practice/) yang
strukturnya benar.

---

Kembali ke: [../README.md](../README.md)
