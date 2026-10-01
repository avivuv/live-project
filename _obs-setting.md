# Setting OBS — YouTube 1440p

Referensi setting streaming utama: **YouTube**.
Section SE Live (Facebook / TikTok / Instagram) disimpan sebagai arsip di bawah —
saat ini **tidak dipakai**.

---

## Spec PC

| Komponen | Detail |
|---|---|
| CPU | AMD Ryzen 5 7600 (6-core / 12-thread) |
| GPU | ASUS Dual GeForce RTX 5060 8GB OC Edition |
| RAM | G.Skill Trident Z5 Neo RGB DDR5 6000MHz 32GB (2x16GB) AMD EXPO |
| Upload | ~108 Mbps simetris (Upaznet / Telkom Surabaya) |

Bandwidth bukan kendala — 30 Mbps hanya memakai ~28% dari upload.
Karena sekarang single-output ke YouTube saja, beban GPU jauh lebih ringan
dibanding era multistream. Itu yang membuat preset P7 terjangkau.

---

## 1. Profil OBS

Profil bernama **`Multistream`** ada di:
`%APPDATA%\obs-studio\basic\profiles\Multistream\`

Pilih lewat menu **Profile → Multistream**. Profil `Untitled` tetap utuh sebagai cadangan.

> Nama profil masih `Multistream` dari setup lama, walaupun sekarang hanya YouTube.

---

## 2. Settings → Output (Advanced) — AKTIF

Setting terkini, tab **Streaming**:

```
Output Mode    : Advanced
Audio Track    : 1
Audio Encoder  : FFmpeg AAC
Video Encoder  : NVIDIA NVENC AV1
Rescale Output : Disabled

Rate Control   : CBR
Bitrate        : 30000 Kbps
Keyframe       : 2 s
Preset         : P7 (Slowest / Best Quality)
Tuning         : High Quality
Multipass      : Two Passes (Quarter Resolution)
Profile        : main
Look-ahead     : off
Adaptive Quant : ON
B-Frames       : 0
B-Frame as Ref : Disabled
```

**Audio:** AAC 192 kbps

### Alasan tiap pilihan

| Setting | Kenapa |
|---|---|
| **AV1** | Efisiensi codec terbaik. ⚠️ perlu diverifikasi — lihat section 6 |
| **30000 Kbps** | 1440p60 butuh ~1.8× bit dibanding 1080p. Upload 108 Mbps, jadi aman |
| **P7** | Sumber kualitas terbesar. Terjangkau karena single-output |
| **Multipass Quarter** | Full Resolution hampir tidak menambah kualitas tapi menambah latensi & beban GPU |
| **Look-ahead off** | Menahan frame di buffer → penambah delay signifikan |
| **Adaptive Quant ON** | Ini yang memperbaiki blur saat game ramai. Kebalikan dari era multistream |
| **B-Frames 0** | Penghilang delay struktural. Encoder tidak perlu menahan frame untuk referensi masa depan |

> **Catatan perubahan dari setup lama:** Adaptive Quantization dulu dimatikan
> (lihat arsip) karena GPU jadi bottleneck saat meng-encode 4 output sekaligus.
> Dengan single-output ke YouTube, GPU punya ruang — dan AQ justru jadi kunci
> mengatasi blur di adegan padat. Rekomendasinya berbalik.

---

## 3. Settings → Video

```
Base Resolution   : 2560x1440
Output Resolution : 2560x1440
FPS               : 60
Downscale Filter  : Bicubic
Color Format      : NV12
Color Space       : 709
Color Range       : Partial
```

> `Rescale Output` di tab Streaming = **Disabled**, jadi resolusi yang dikirim
> ditentukan sepenuhnya di sini.

---

## 4. Masalah delay — sumber sebenarnya

Ini bagian yang paling sering salah sasaran. **Encoder settings hanya menyumbang
milidetik sampai ~1 detik.** Kalau delay terasa puluhan detik, sumbernya bukan OBS.

### Urutan penyebab, dari yang terbesar

**a. YouTube Latency setting ← penyumbang 90%+**

| Mode | Delay |
|---|---|
| Normal | 30–60 detik |
| **Low latency** | **10–20 detik** ← rekomendasi |
| Ultra-low latency | 2–5 detik, tapi dibatasi maks 1080p |

⚠️ **Ultra-low latency akan memaksa stream turun ke 1080p.** Karena prioritasnya
kualitas 1440p, pilih **Low latency**.

**Letak menunya** (tidak intuitif, bukan di Settings channel):

```
studio.youtube.com
  → Create (ikon kamera +) → Go live
  → tab Stream
  → tombol Edit pada kartu detail stream
  → tab Customization        ← bukan tab Details
  → scroll ke bawah, satu area dengan pengaturan Live chat
  → Stream latency
```

Tidak bisa diubah di tengah stream — harus stop dulu.

Kalau bagian Latency tidak muncul di tab Customization:
- Matikan **DVR** dulu, kadang mengunci opsi ini
- Atau penyebabnya **codec AV1** — lihat section 6

**b. Batas arsitektural YouTube**

Delay YouTube tidak akan pernah di bawah ~2 detik. Itu batas platformnya
(segmented HTTP delivery). Target realistis: **~40 detik → ~15 detik**.
Kalau butuh hampir real-time seperti Twitch, YouTube bukan platformnya.

**c. Setting OBS yang sudah dioptimalkan**

Sudah selesai semua — B-Frames 0, Look-ahead off, Multipass Quarter.
Tidak ada lagi yang bisa diperas dari sini tanpa mengorbankan kualitas.

**d. Bandwidth — bukan penyebab**

30 Mbps dari 108 Mbps upload. Headroom besar, tidak ada buffering jaringan.

---

## 5. Kalau blur muncul lagi di adegan ramai

Urutan yang dicoba, dari yang paling berpengaruh:

1. **Naikkan bitrate** 30000 → 35000 Kbps. Paling langsung dampaknya, dan
   bandwidth masih sangat lega
2. Pastikan **Adaptive Quantization tetap ON** — ini yang menangani area padat
3. **Kembalikan B-Frames ke 2**. B-frame menghemat bit, jadi membantu di adegan
   kompleks. Konsekuensinya delay naik sedikit — trade-off nyata di 1440p
4. **Multipass → Full Resolution**. Hanya kalau bitrate sudah tidak bisa dinaikkan.
   Efeknya <1 dB PSNR, praktis tidak terlihat

> Jangan naikkan bitrate melewati ~35000. YouTube tetap mentranscode ke bitrate
> distribusi mereka sendiri, jadi kelebihannya terbuang.

---

## 6. ⚠️ AV1 — perlu diverifikasi

Kalau YouTube tidak menerima AV1 sebagai ingest langsung untuk channel ini,
server mereka harus **transcode** dulu. Itu menambah delay beberapa detik
**dan** menurunkan kualitas — dua hal yang justru sedang dihindari.

**Cara cek:** saat live, buka Live Control Room → **Stream health**. Lihat apakah
ada peringatan soal codec.

**Kalau ternyata di-transcode**, ganti Video Encoder ke **NVENC HEVC** atau
**H.264**. Di 30000 Kbps untuk 1440p, keunggulan efisiensi AV1 tidak banyak
terpakai — bitratenya sudah di atas titik jenuh.

AV1 juga kandidat penyebab kalau menu Stream latency tidak muncul.

---

## 7. Pantau Stats

**View → Stats** saat live. Target semua mendekati **0%**.

| Metrik | Artinya | Solusi |
|---|---|---|
| Frames missed due to **rendering lag** | GPU kewalahan | kunci FPS game ke 60, turunkan P7 → P6 |
| Skipped frames due to **encoding lag** | encoder kewalahan | turunkan preset |
| Dropped frames (**network**) | koneksi | turunkan bitrate |

Cek juga **Task Manager → Performance → GPU → Video Encode**. Kalau mendekati
100%, encoder jenuh dan P7 terlalu berat.

### Kunci FPS game ke 60 ← tetap paling berpengaruh

Kalau game berjalan tanpa batas FPS (bisa 150–200), GPU terpakai habis untuk
render dan tidak menyisakan ruang untuk encoder. Frame di atas 60 **tidak pernah
sampai ke penonton** karena OBS cuma mengambil 60 per detik — murni terbuang
sambil merugikan encoder.

Set lewat setting in-game, atau NVIDIA Control Panel → Manage 3D Settings →
Max Frame Rate → 60.

---

## 8. Catatan keamanan

⚠️ File `%APPDATA%\obs-studio\basic\profiles\Untitled\basic.ini` menyimpan
**token akses YouTube dalam bentuk plaintext** (`RefreshToken` & `Token`).

Refresh token tidak kedaluwarsa sampai dicabut manual — siapa pun yang punya
file itu bisa mengakses akun YouTube.

- Jangan pernah share file `basic.ini`
- Kalau folder `Live` di-`git init`, jangan pernah commit folder OBS
- Cabut akses lewat https://myaccount.google.com/permissions kalau pernah bocor

---
---

# ARSIP — Setup Multistream (tidak dipakai)

Section di bawah ini dari era multistream lewat **Streamelements SE Live**
(https://streamelements.com/selive) ke Facebook, TikTok, dan Instagram.
Disimpan kalau suatu saat mau dipakai lagi.

> ⚠️ **Setting AV1 + 1440p di atas tidak kompatibel** dengan Facebook / TikTok /
> Instagram. Kalau multistream diaktifkan lagi, semua platform itu wajib pakai
> override H.264 1080p — dan tiap override menambah satu encoding pass di GPU.
> Kemungkinan besar P7 harus diturunkan ke P4/P5.

> Encoder utama saat itu: **H.264, 8000 Kbps, 1080p60, P5, B-frames 2,
> Adaptive Quantization OFF.**

---

## A1. SE Live — Output per platform

Dashboard SE Live → tab **Outputs** → pilih platform → **Encoding**.

### YouTube — platform utama

```
Override Settings : OFF
```

Biarkan pakai encoder utama OBS (8000 Kbps, P5). Menghemat satu encoding pass
dan YouTube dapat kualitas penuh.

### Facebook

```
Override Settings : ON
Video Encoding    : NVIDIA NVENC H.264
Scale Video Frame : Do Not Scale (1920x1080)
Rate Control      : Constant Bitrate
Bitrate           : 4000 Kbps
Keyframe interval : 2
Preset            : P4 Medium
Tuning            : High Quality
Multipass Mode    : Single Pass
Profile           : high
Adaptive Quant.   : OFF
Look-ahead        : OFF
```

> Facebook membatasi 4000 Kbps. Mengirim lebih tinggi tidak menambah kualitas
> yang sampai ke penonton.

### TikTok

Identik dengan Facebook — semua angka sama.

```
Override Settings : ON
Video Encoding    : NVIDIA NVENC H.264
Scale Video Frame : Do Not Scale (1920x1080)
Rate Control      : Constant Bitrate
Bitrate           : 4000 Kbps
Keyframe interval : 2
Preset            : P4 Medium
Tuning            : High Quality
Multipass Mode    : Single Pass
Profile           : high
Adaptive Quant.   : OFF
Look-ahead        : OFF
```

> TikTok Live mendukung 60fps. Tidak perlu diturunkan.

### Instagram — vertikal 9:16

Sudah pakai **canvas vertikal khusus** (bukan default canvas), jadi
`Scale Video Frame` biarkan `Do Not Scale` — canvas-nya sendiri sudah vertikal.

```
Override Settings : ON
Video Encoding    : NVIDIA NVENC H.264
Scale Video Frame : Do Not Scale       ← canvas sudah vertikal
Rate Control      : Constant Bitrate
Bitrate           : 4000 Kbps
Keyframe interval : 2
Preset            : P4 Medium
Tuning            : High Quality
Multipass Mode    : Single Pass
Profile           : high
Adaptive Quant.   : OFF
```

> Instagram lebih ketat soal bitrate. Kalau sering putus, turunkan ke 3500.
>
> ⚠️ **Instagram tidak menyediakan RTMP key resmi** dan key-nya berumur pendek.
> Kalau tidak sedang live IG, **matikan target ini** supaya tidak ada percobaan
> reconnect sia-sia yang memakan resource. Lihat section A6d.

---

## A2. Kenapa Look-ahead & Adaptive Quantization dimatikan (konteks multistream)

Keduanya punya pola yang sama: **menukar beban GPU untuk efisiensi bit**.
Masalah di setup ini justru GPU kewalahan sementara bit berlimpah — jadi
pertukarannya merugikan.

### Look-ahead

Encoder "mengintip" beberapa frame ke depan sebelum memutuskan alokasi bit dan
penempatan B-frame. Kalau tahu adegan berikutnya ramai, ia menyiapkan bit lebih dulu.

- **Biaya:** menambah latensi (frame ditahan dulu) + beban VRAM & GPU
- **Manfaat:** nyata di bitrate rendah. Di 8000 Kbps untuk 1080p, bit sudah
  berlimpah — tidak ada yang perlu "dihemat"
- **Berguna kalau:** streaming di bawah 3000 Kbps, atau GPU sangat lega

### Adaptive Quantization (Psycho Visual Tuning)

Mendistribusikan bit berdasarkan cara mata memandang — area fokus dapat bit lebih
banyak, area yang kurang diperhatikan dikurangi. Di OBS kadang dipecah jadi
Spatial AQ dan Temporal AQ.

- **Biaya:** paling berat di antara semua opsi NVENC. Penyebab umum encoding lag
  pada kartu yang juga merender game
- **Manfaat:** menyusut di bitrate tinggi
- **Berguna kalau:** bitrate terbatas, atau konten dengan area gelap luas &
  gradasi halus (game horor, ruang gelap) di mana banding paling kelihatan

### Kalau mau coba nyalakan

Setelah FPS game dikunci dan Stats bersih 0%:

1. Nyalakan **Psycho Visual / AQ** dulu — dampak kualitasnya lebih terasa
2. Pantau Stats beberapa menit
3. Kalau rendering lag naik, matikan lagi
4. Look-ahead terakhir, dan hanya kalau AQ aman

Satu per satu, jangan sekaligus — biar ketahuan mana yang bikin lag.

---

## A3. Profile: `high`, bukan `high10`

Ini penting dan gampang terlewat.

`high10` = H.264 High 10-bit. Facebook, TikTok, dan Instagram mengharapkan **8-bit**.
10-bit bisa ditolak, atau diterima tapi dipaksa transcode ulang — dan itu justru
menurunkan kualitas.

Pastikan **semua** output pakai `high`.

---

## A4. Kondisi aktual (hasil cek 31 Juli 2026)

Dibaca dari `destinations.json` di
`%APPDATA%\obs-studio\plugin_config\obs-streamelements-core\scoped_config_storage\streamelements_multi-streaming\`

| Setting | Facebook | TikTok | Instagram |
|---|---|---|---|
| Bitrate | 4000 ✅ | 4000 ✅ | 4000 ✅ |
| Keyframe | 2 ✅ | 2 ✅ | 2 ✅ |
| Preset | P4 ✅ | P4 ✅ | P4 ✅ |
| Profile | high ✅ | high ✅ | high ✅ |
| **Adaptive Quantization** | **ON** ⚠️ | **ON** ⚠️ | **ON** ⚠️ |
| Look-ahead | off ✅ | *(default)* | *(default)* |
| Canvas | default | default | vertikal ✅ |

**Yang perlu diubah: matikan Adaptive Quantization di ketiganya.**

Ini kemungkinan besar penyebab utama gambar pecah. Deskripsi resminya sendiri
menyebut *"at the cost of increased GPU utilization"* — dan GPU sudah jadi
bottleneck (rendering lag 1.1%). Di 4000 Kbps manfaatnya kecil, apalagi hasilnya
di-transcode ulang oleh platform.

Sisanya sudah benar semua.

---

## A5. Ringkasan beban

| Output | Bitrate | Preset | Encoding pass |
|---|---|---|---|
| YouTube | 8000 | P5 | encoder utama |
| Facebook | 4000 | P4 | override |
| TikTok | 4000 | P4 | override |
| Instagram | 4000 | P4 | override |

Total upload: **~20 Mbps** dari 108 Mbps tersedia — sangat aman.

> Tiap override = satu encoding pass tambahan di GPU. Peringatan
> *"will require more resources from your device"* di SE Live itu benar adanya.

---

## A6. Kalau gambar pecah / patah-patah

Penyebab paling sering, urut dari yang paling berpengaruh:

### a. Kunci FPS game ke 60 ← paling berpengaruh

Kalau game berjalan tanpa batas FPS (bisa 150–200), GPU terpakai habis untuk
render dan tidak menyisakan ruang untuk encoder. Frame di atas 60 **tidak pernah
sampai ke penonton** karena OBS cuma mengambil 60 per detik — jadi murni terbuang
sambil merugikan encoder.

Set lewat setting in-game, atau NVIDIA Control Panel → Manage 3D Settings →
Max Frame Rate → 60.

### b. Pantau Stats

**View → Stats** saat live. Yang diperhatikan:

| Metrik | Artinya | Solusi |
|---|---|---|
| Frames missed due to **rendering lag** | GPU kewalahan | kunci FPS game, turunkan preset |
| Skipped frames due to **encoding lag** | encoder kewalahan | turunkan preset atau bitrate |
| Dropped frames (**network**) | koneksi | turunkan bitrate |

Target: semua mendekati **0%**.

### c. Kalau rendering lag masih >1%

Urutan yang dicoba:

1. Kunci FPS game ke 60 (kalau belum)
2. Matikan override **TikTok** — biarkan ikut encoder utama
3. Turunkan YouTube dari P5 ke **P4**
4. Turunkan bitrate YouTube 8000 → 6000

### d. Matikan target Instagram kalau tidak dipakai

Log menunjukkan target **Instagram** (`edgetee-upload-cgk1-2.xx.fbcdn.net`) gagal
connect berulang kali dengan jeda makin panjang:

```
Reconnecting in 2.00s → 3.02s → 4.55s → 6.86s → 10.35s → 15.62s → 23.56s → 35.54s
```

Penyebabnya **stream key kedaluwarsa**. Instagram tidak menyediakan RTMP key resmi
dan key-nya berumur pendek — tidak seperti Facebook yang bisa pakai persistent key.

Percobaan reconnect terus-menerus memakan resource tanpa hasil apa pun.

**Solusi:** matikan (disable) target Instagram di SE Live kalau tidak sedang live
di IG. Ambil key baru tiap kali mau dipakai.

> Catatan: Facebook (`live-api-s.facebook.com`) berjalan normal — bukan ini
> masalahnya.

Cek log di: `%APPDATA%\obs-studio\logs\`

---

## A7. Referensi bitrate per platform

| Platform | Rekomendasi 1080p60 | Batas |
|---|---|---|
| YouTube | 6000–9000 Kbps | — |
| Facebook | 4000 Kbps | 4000 (hard limit) |
| TikTok | 4000–6000 Kbps | — |
| Instagram | 3500–4000 Kbps | lebih ketat |

Keyframe **2 detik wajib** di semua platform. Tanpa itu, YouTube bisa memaksa
transcode ulang dan Facebook menolak stream.
