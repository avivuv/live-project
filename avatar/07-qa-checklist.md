# QA Checklist

Daftar pemeriksaan **sebelum melunasi pembayaran**. Sekali dilunasi, posisi
tawar untuk minta revisi hilang.

Cetak atau buka dokumen ini saat menerima file dari artist.

---

## Tahap 1 — Cek PSD

Buka di Photoshop / Krita / Photopea (gratis, berbasis browser).

### Format

- [ ] Kanvas **4096 × 4096 px**
- [ ] RGB, 8-bit
- [ ] File `.psd` — layer utuh, tidak di-flatten
- [ ] Ukuran file wajar (100 MB – 1 GB untuk model berlayar penuh)

### Transparansi

- [ ] Matikan semua layer → **kanvas benar-benar kosong** (bukan putih, bukan
      checkerboard yang digambar)
- [ ] Tidak ada layer berisi background solid tersembunyi

> **Cara cek cepat:** buat layer baru paling bawah, isi merah terang. Kalau ada
> area putih/abu yang menutupi merah, berarti ada background palsu.

### Struktur Layer

- [ ] Nama layer persis sesuai [03-layer-spec.md](03-layer-spec.md)
- [ ] Tidak ada layer berisi lebih dari satu objek
- [ ] `Brow_L` dan `Brow_R` **terpisah**
- [ ] `Iris_L`, `Iris_R`, `Pupil_L`, `Pupil_R` masing-masing sendiri
- [ ] Poni terpecah **minimal 3** grup helai
- [ ] Tidak ada layer style / adjustment layer / smart object
- [ ] Tidak ada clipping mask yang belum di-apply

### Area Tersembunyi — cek satu per satu

Matikan layer yang menutupi, pastikan yang di bawahnya **utuh**:

- [ ] Matikan poni → **dahi utuh**, tidak berlubang
- [ ] Matikan kelopak → **mata utuh**, sclera berbentuk elips penuh
- [ ] Matikan rambut samping → **telinga utuh** kiri & kanan
- [ ] Matikan kerah jaket → **leher utuh** sampai pangkal
- [ ] Matikan jaket → **kemeja utuh**, bukan potongan
- [ ] Matikan layer mulut → **gigi & lidah ada** dan terpisah
- [ ] Rambut belakang utuh, tidak terpotong mengikuti siluet depan

### Kualitas Gambar

- [ ] Zoom 100% pada mata → **tajam**, tidak blur atau ada artefak
- [ ] Lineart bersih, tidak bergelombang
- [ ] Tepi part halus, tidak ada sisa piksel putih (*fringing*)
- [ ] Warna sesuai [01-character-design.md](01-character-design.md)
- [ ] Emblem **original** — tidak ada elemen IP pihak lain

---

## Tahap 2 — Cek Model di VTube Studio

Muat model, lalu uji satu per satu.

### Gerakan Kepala

- [ ] Menoleh kiri–kanan penuh (±30°) — **tidak ada bagian yang hilang atau
      robek**
- [ ] Menunduk–mendongak penuh — leher tetap natural, tidak terlihat celah
- [ ] Memiringkan kepala — rambut mengikuti dengan wajar
- [ ] Saat menoleh, **telinga di sisi berlawanan terlihat** dan bentuknya benar

### Mata

- [ ] Kedip mulus — kelopak turun menutupi, bukan mata yang menghilang
- [ ] Kedip kiri & kanan bisa terpisah (wink)
- [ ] Arah pandang bergerak ke 4 arah — **iris tidak keluar dari sclera**
- [ ] Highlight mata ikut bergerak bersama iris
- [ ] Mata melengkung saat ekspresi senyum

### Mulut & Lip Sync

- [ ] Buka–tutup mulus
- [ ] Bicara → mulut mengikuti suara dengan delay wajar
- [ ] Vokal A/I/U/E/O terlihat berbeda
- [ ] Saat terbuka lebar, **rongga mulut + gigi + lidah terlihat**, tidak bolong

### Ekspresi

Uji ketujuh hotkey:

- [ ] Normal
- [ ] Senyum
- [ ] Tertawa
- [ ] Kaget
- [ ] Marah
- [ ] Sedih
- [ ] Malu — blush muncul
- [ ] Transisi antar ekspresi mulus, tidak patah
- [ ] Kembali ke Normal bersih, tidak ada sisa ekspresi sebelumnya

### Physics

- [ ] Gerakkan kepala cepat → rambut mengikuti dengan **jeda natural**
- [ ] Rambut berhenti bergoyang dalam waktu wajar (tidak bergetar terus)
- [ ] Poni bergerak **lebih sedikit** dari rambut belakang
- [ ] Grup rambut **tidak bergerak serempak** — ada beda fase
- [ ] Liontin berayun wajar
- [ ] Ornamen bahu (logam) bergerak **sedikit saja**
- [ ] Tidak ada part yang saling menembus saat bergerak ekstrem

### Idle

- [ ] Napas terlihat halus saat diam
- [ ] Kedip otomatis dengan jeda acak, terasa natural
- [ ] Sway idle halus, tidak mengganggu

---

## Tahap 3 — Cek Performa

Jalankan bersama game, kondisi sebenarnya.

- [ ] VTube Studio 60 fps stabil
- [ ] Jalan bersamaan dengan Genshin Impact → **frame rate game tidak turun
      signifikan**
- [ ] Jalan bersamaan dengan OBS + encoding → aman
- [ ] Penggunaan GPU wajar (cek Task Manager)
- [ ] Jumlah ArtMesh < 150 (terlihat di Cubism / info model)
- [ ] Tidak ada memory leak — biarkan 2 jam, cek RAM tidak terus naik

> PC memakai RTX 5060 8GB. VRAM 8GB harus dibagi dengan game dan encoder,
> jadi model yang boros akan terasa.

---

## Tahap 4 — Cek Integrasi OBS

- [ ] Ter-capture di OBS dengan **background transparan**
- [ ] Tidak ada watermark VTube Studio (kalau sudah beli lisensi)
- [ ] Ukuran & posisi pas di layout stream
- [ ] Tepi model bersih saat di atas gameplay, tidak ada garis aneh
- [ ] Hotkey ekspresi berfungsi saat OBS sedang fokus
- [ ] Uji rekam 5 menit → putar ulang, cek tidak ada glitch

Setelan OBS ada di [_obs-setting.md](../_obs-setting.md).

---

## Tahap 5 — Cek Kelengkapan File

- [ ] `.psd` — berlayer, siap diedit
- [ ] `.cmo3` — project Cubism, bisa diedit ulang
- [ ] `.moc3` — model
- [ ] `.model3.json` — konfigurasi
- [ ] Texture atlas (`.png`)
- [ ] `.physics3.json`
- [ ] 7 file `.exp3.json`
- [ ] Emblem — PNG transparan + SVG
- [ ] Kesepakatan hak komersial tertulis

> **File sumber (`.psd` dan `.cmo3`) wajib ada.** Tanpa itu, setiap perubahan
> di masa depan harus lewat artist yang sama, dan kalau artist tidak lagi aktif,
> model tidak bisa diperbaiki sama sekali.

---

## Kalau Ada yang Gagal

1. **Catat spesifik** — screenshot atau rekam layar, sebutkan langkah untuk
   memunculkan masalahnya
2. **Rujuk ke spec** — tunjuk baris di dokumen yang tidak terpenuhi
3. **Kirim sekaligus**, bukan satu per satu — lebih efisien untuk kedua pihak
4. **Tahan pelunasan** sampai perbaikan selesai

Masalah yang paling sering muncul:

| Masalah | Penyebab | Perbaikan |
|---|---|---|
| Bolong saat menoleh | Area tersembunyi tidak digambar | Ilustrator harus menggambar ulang bagian itu |
| Rambut kaku | Poni tidak dipecah / physics lemah | Bisa diperbaiki di rigging kalau layer sudah terpisah |
| Mata aneh saat melirik | Sclera tidak elips penuh | Ilustrator perbaiki layer `EyeWhite` |
| Mulut bolong saat terbuka | Tidak ada `Mouth_Inside` | Ilustrator tambah layer |
| Model berat | Terlalu banyak ArtMesh | Rigger optimasi mesh |

---

Kembali ke: [README.md](README.md)
