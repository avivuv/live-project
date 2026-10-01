# Avatar — VTuber Live2D

Dokumentasi untuk membuat model VTuber Live2D channel
[@avivuv](https://www.youtube.com/@avivuv).

**Status:** siap komisi — dokumen lengkap, artwork belum dibuat
**Terakhir diperbarui:** 2026-09-16

---

## Mulai dari Mana

| Kalau kamu... | Baca |
|---|---|
| Mau tahu kondisi sekarang | [05-status-assets-v1.md](05-status-assets-v1.md) |
| Mau cari artist | [06-budget.md](06-budget.md) |
| Sudah dapat artist | [02-commission-brief.md](02-commission-brief.md) |
| Menerima hasil dari artist | [07-qa-checklist.md](07-qa-checklist.md) |
| Mau belajar rigging sendiri | [practice/PANDUAN.md](practice/PANDUAN.md) |

---

## Isi Folder

| File | Untuk siapa | Isi |
|---|---|---|
| [01-character-design.md](01-character-design.md) | Semua pihak | Palet warna terkunci, desain karakter, emblem original |
| [02-commission-brief.md](02-commission-brief.md) | **Dikirim ke artist** | Lingkup kerja, spek teknis, lisensi, termin bayar |
| [03-layer-spec.md](03-layer-spec.md) | Ilustrator | Struktur PSD, penamaan layer, area tersembunyi |
| [04-rigging-spec.md](04-rigging-spec.md) | Rigger | Parameter Live2D, ekspresi, physics, target performa |
| [05-status-assets-v1.md](05-status-assets-v1.md) | Internal | Hasil audit pack V1 — kenapa belum bisa dipakai |
| [06-budget.md](06-budget.md) | Internal | Estimasi biaya, cara memilih artist |
| [07-qa-checklist.md](07-qa-checklist.md) | Internal | Cek sebelum melunasi pembayaran |
| [practice/](practice/) | **Latihan** | PSD latihan + panduan rigging Cubism |
| [assets-v1/](assets-v1/) | Referensi | Arsip pack V1 — referensi visual saja |
| [assets-v3/](assets-v3/) | Referensi | Arsip pack V3 + versi yang sudah diperbaiki |

---

## Ringkasan Situasi

Sudah ada dua percobaan asset — **V1** (PNG terpisah) dan **V3** (PSD berlayer).
Keduanya punya **arah desain yang bagus**, dan V3 jelas lebih maju. Yang belum
ada adalah artwork pada resolusi produksi dengan penempatan anatomis.

### V1 — 24 file PNG

| Temuan | Detail |
|---|---|
| Resolusi | **3–13× di bawah** kebutuhan Live2D (mata cuma 135×75 px) |
| Transparansi | **18 dari 23 file** tanpa alpha asli — checkerboard-nya digambar |
| Pemisahan layer | Belum — 2 alis masih dalam 1 file, 9 bentuk mulut dalam 1 file |
| Area tersembunyi | Tidak ada — wajib untuk Live2D |
| Konsistensi ekspresi | 7 gambar terpisah, bukan deformasi 1 model |

README pack V1 sendiri sudah menyatakan ini apa adanya
(*"NOT yet a production-ready, fully separated PSD"*).

### V3 — PSD 45 layer

| Temuan | Detail |
|---|---|
| Format | **PSD berlayer dengan alpha asli** — perbaikan besar dari V1 |
| Cakupan | **45 layer**, sudah ada telinga & badan utuh |
| Resolusi | median part **85×70 px** — masih terlalu kecil |
| Posisi | semua part di **x=760**, koordinat grid sheet bukan anatomis |
| Artefak | teks label (*"Highlight L"*) & border kartu ikut terpotong |
| File | **korup 3 byte** — Cubism menolak membukanya (sudah diperbaiki) |

**Artinya:** tidak ada jalan teknis dari V1 maupun V3 ke model yang bisa di-rig.
Artwork harus digambar baru. Tapi seluruh kerja desainnya tetap terpakai —
sudah diserap ke dokumen di folder ini.

Detail: [05-status-assets-v1.md](05-status-assets-v1.md) ·
[assets-v3/CATATAN.md](assets-v3/CATATAN.md)

---

## Retheme Original

Desain V1 memakai branding **Genshin Impact / simbol Anemo**. Karena channel
ini monetized (Saweria aktif), desain diubah jadi orisinal:

**Dipertahankan** — tidak dimiliki siapa pun:
rambut hitam ujung cyan · jaket hitam trim emas · glow cyan · tema angin

**Diganti:**
simbol Anemo → emblem original · nama "ANEMO VTUBER" → nama sendiri ·
motif kostum → variasi orisinal

Hasilnya terasa sama secara visual, tanpa risiko takedown.

Detail: [01-character-design.md](01-character-design.md)

---

## Warna Identitas

Diekstrak dari asset V1, hue konsisten 180–200 lintas rambut, iris, dan efek:

| | Hex | Peran |
|---|---|---|
| Cyan utama | `#3FC5DB` | **Warna identitas channel** |
| Cyan terang | `#7FE9F5` | Glow, highlight |
| Emas | `#B8935A` | Trim, ornamen |
| Hitam rambut | `#12131A` | Base (undertone biru) |

Pakai warna yang sama untuk [banner/](../banner/) ·
[thumbnail/](../thumbnail/) · [watermark/](../watermark/) supaya branding
channel konsisten.

Palet lengkap: [01-character-design.md](01-character-design.md)

---

## Cubism Sudah Terpasang

**Live2D Cubism Editor 5.3.04** terpasang di PC dan berfungsi normal (GPU
RTX 5060 terdeteksi benar).

Tersedia PSD latihan dengan struktur yang benar supaya bisa mulai belajar
rigging sekarang, tanpa menunggu artwork dari artist:

- [practice/practice.psd](practice/) — 2048×2048, 45 layer, posisi anatomis,
  area tersembunyi lengkap
- [practice/PANDUAN.md](practice/PANDUAN.md) — langkah rigging dari nol

> Catatan dari log Cubism: dukungan **pen tablet tidak aktif**
> (`jpen couldn't be loaded`). Untuk rigging tidak masalah — mayoritas pakai
> mouse.

---

## Langkah Berikutnya

1. **Tentukan nama karakter** — cek dulu belum dipakai VTuber lain
2. **Desain emblem original** — pengganti simbol Anemo
3. **Minta penawaran ke 3+ artist** — lihat [06-budget.md](06-budget.md)
4. **Kirim brief** — [02-commission-brief.md](02-commission-brief.md) +
   [01-character-design.md](01-character-design.md) +
   [03-layer-spec.md](03-layer-spec.md)
5. **QA sebelum lunas** — [07-qa-checklist.md](07-qa-checklist.md)

**Perkiraan:** 7–12 minggu · Rp 5 – 11 juta (tier menengah lokal)

Sambil menunggu, **VRoid Studio** (gratis, 3D) atau **PNGTuber** bisa dipakai
supaya streaming tetap jalan.

---

## Terkait

- [_obs-setting.md](../_obs-setting.md) — setelan OBS
- [deskripsi-channel.md](../deskripsi-channel.md) — deskripsi channel
- [_common.md](../_common.md) — blok deskripsi yang dipakai ulang
