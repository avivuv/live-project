# Character Design Spec

Dokumen ini **mengunci** desain karakter. Semua pihak (ilustrator, rigger,
thumbnail designer) mengacu ke sini supaya hasilnya konsisten.

**Status:** v2 — retheme original (lepas dari branding Genshin)
**Channel:** https://www.youtube.com/@avivuv
**Terakhir diperbarui:** 2026-09-16

---

## Ringkasan Konsep

Streamer bergaya *anime semi-realistis*, laki-laki, remaja akhir–dewasa muda.
Tema **angin / wind** dengan palet **hitam · cyan · emas**. Kesan yang dituju:
tenang tapi berenergi, cocok untuk stream santai (Ragnarok & Genshin) tanpa
terlihat terlalu "edgy".

Framing: **bust-up front-facing** (kepala sampai dada) — standar untuk overlay
pojok layar saat streaming gameplay.

---

## Perubahan dari V1 — Retheme Original

Pack V1 memakai branding **Genshin Impact / simbol Anemo** eksplisit. Karena
channel ini sudah monetized (Saweria aktif), desain diubah jadi orisinal.

| Elemen | V1 (lama) | v2 (dipakai) |
|---|---|---|
| Nama | "ANEMO VTUBER" | Nama sendiri — lihat catatan di bawah |
| Simbol dada/bahu | Lambang Anemo Genshin | **Lambang original** (lihat §Emblem) |
| Motif kostum | Turunan desain Genshin | Variasi orisinal, siluet dipertahankan |
| Efek angin | "Anemo" | Wind FX generik |

**Yang dipertahankan** (tidak dimiliki siapa pun, aman dipakai):

- Rambut hitam dengan ujung/tip cyan
- Jaket hitam dengan trim emas
- Aksen glow cyan
- Tema angin dan partikel

> **Nama karakter** belum ditentukan. Sampai diputuskan, dokumen memakai
> placeholder `{NAMA}`. Saran: nama pendek 2–3 suku kata yang mudah diucap di
> chat dan belum dipakai VTuber lain — cek dulu di YouTube/Twitch/TikTok.

---

## Palet Warna

Nilai di bawah adalah **hasil ekstraksi dari asset V1** yang sudah dinormalisasi
(sampel V1 beresolusi rendah sehingga warnanya ter-antialias jadi lebih gelap).

### Primer

| Peran | Hex | Catatan |
|---|---|---|
| Hitam rambut (base) | `#12131A` | Bukan hitam murni — ada undertone biru |
| Hitam rambut (shadow) | `#0A0B10` | |
| Hitam rambut (highlight) | `#2A2D3A` | |
| Hitam kostum (base) | `#15161C` | Sedikit lebih hangat dari rambut |
| Hitam kostum (shadow) | `#0B0C11` | |

### Aksen Cyan — warna signature

Hue terukur konsisten di **180–200** lintas rambut, iris, efek, dan ornamen.

| Peran | Hex | Catatan |
|---|---|---|
| Cyan terang (glow core) | `#7FE9F5` | Ujung rambut, highlight mata |
| Cyan utama | `#3FC5DB` | **Warna identitas** — pakai di thumbnail & banner |
| Cyan sedang | `#2A8CA3` | Gradasi, efek angin |
| Cyan gelap | `#17505E` | Bayangan pada area cyan |

### Aksen Emas

| Peran | Hex | Catatan |
|---|---|---|
| Emas terang | `#E3C07A` | Highlight trim |
| Emas utama | `#B8935A` | Trim jaket, ornamen |
| Emas gelap | `#6E5436` | Bayangan ornamen |

### Kulit

| Peran | Hex |
|---|---|
| Base | `#EFC3A8` |
| Shadow | `#C99079` |
| Shadow dalam | `#9C6C60` |
| Blush (untuk ekspresi malu) | `#E08A80` |

### Mata

| Peran | Hex |
|---|---|
| Sclera | `#F4F6F8` (bukan putih murni) |
| Iris luar | `#2A8CA3` |
| Iris dalam | `#7FE9F5` |
| Pupil | `#0E1418` |
| Highlight utama | `#FFFFFF` |

---

## Rambut

- **Warna:** hitam undertone biru, **ujung/tip cyan** — gradasi, bukan potongan tegas
- **Gaya:** pendek–medium, berantakan natural (messy), tidak rapi tersisir
- **Poni:** menutupi sebagian dahi, terbelah tidak simetris
- **Panjang:** belakang sampai tengkuk, samping sampai rahang

**Penting untuk rigging** — poni harus dipisah **3–5 grup helai** agar physics
bisa bergerak natural. Ini sering terlewat dan mahal untuk diperbaiki belakangan.

---

## Wajah

- Struktur *anime semi-realistis* — bukan chibi, bukan realis penuh
- Mata tajam, kelopak atas tebal, alis tegas
- Rahang ramping, dagu lancip halus
- **Telinga harus digambar** — dibutuhkan saat kepala menoleh

---

## Kostum

Struktur berlapis (penting untuk pemisahan layer):

1. **Leher** — kulit leher, digambar utuh sampai bawah
2. **Kemeja dalam** — hitam, kerah berdiri
3. **Jaket luar** — hitam dengan trim emas, kerah tinggi asimetris
4. **Ornamen bahu** — logam emas dengan inlay cyan
5. **Aksesori dada** — liontin/kalung dengan kristal cyan yang glow

---

## Emblem Original

Pengganti simbol Anemo. Arahan desain:

- Bentuk dasar: **spiral angin** atau **empat sudut mata angin** yang bergaya
- Warna: emas `#B8935A` dengan core cyan `#3FC5DB`
- Harus terbaca jelas di ukuran kecil (favicon 32px, watermark stream)
- Hindari: bentuk segi enam berputar (terlalu mirip Anemo), lambang elemen game manapun

Emblem ini nantinya dipakai ulang untuk:
[banner/](../banner/) · [watermark/](../watermark/) · [thumbnail/](../thumbnail/)

---

## Ekspresi

Tujuh ekspresi dari V1 dipertahankan:

| Ekspresi | Ciri utama |
|---|---|
| Normal | Netral, mata terbuka normal |
| Senyum | Mulut melengkung, mata sedikit menyipit |
| Tertawa | Mulut terbuka lebar, mata tertutup melengkung |
| Kaget | Mata melebar, alis naik, mulut terbuka bulat |
| Marah | Alis turun tajam, mulut mengerut |
| Sedih | Alis naik di tengah, mata sayu |
| Malu | Blush di pipi, mata memalingkan pandangan |

Tambahan opsional: mata tertutup, wink, menatap kanan/kiri, menunduk, mendongak.

---

## Referensi Visual

Sheet V1 disimpan di [assets-v1/07_references/](assets-v1/07_references/) sebagai
acuan visual. **Catatan:** file di `assets-v1/` adalah referensi desain, bukan
asset produksi — resolusinya 4–16× di bawah kebutuhan Live2D dan tidak punya
transparansi asli. Lihat [05-status-assets-v1.md](05-status-assets-v1.md).

---

Lanjut ke: [02-commission-brief.md](02-commission-brief.md)
