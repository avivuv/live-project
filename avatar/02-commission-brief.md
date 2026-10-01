# Commission Brief — Live2D VTuber Model

> **Cara pakai:** Dokumen ini ditulis untuk **dikirim ke ilustrator / rigger**.
> Isi bagian `{...}`, hapus baris catatan yang diawali `<!--`, lalu kirim
> bersama [01-character-design.md](01-character-design.md) dan
> [03-layer-spec.md](03-layer-spec.md).

---

## Ringkasan Proyek

| | |
|---|---|
| **Jenis** | Live2D VTuber model — bust-up, front facing |
| **Karakter** | Laki-laki, anime semi-realistis, tema angin |
| **Palet** | Hitam · cyan (`#3FC5DB`) · emas (`#B8935A`) |
| **Penggunaan** | Live streaming YouTube (gaming), monetized |
| **Budget** | `{ISI}` |
| **Deadline** | `{ISI}` |

**Referensi desain:** terlampir — `01-character-design.md` (palet & desain
terkunci) dan sheet visual di `assets-v1/07_references/`.

> **Penting:** file di folder `assets-v1/` adalah **referensi visual saja**
> (resolusi rendah, hasil AI, tanpa transparansi asli). Bukan asset untuk
> dipakai ulang. Semua artwork digambar baru.

---

## Lingkup Pekerjaan

Tandai yang dipesan:

- [ ] **A. Ilustrasi + PSD berlayer** (artwork saja, PSD siap rig)
- [ ] **B. Rigging Live2D** (dari PSD yang sudah ada → `.moc3`)
- [ ] **C. Paket lengkap** (A + B, satu vendor)

<!-- Paket lengkap biasanya lebih mahal tapi lebih aman: tidak ada saling
     lempar tanggung jawab kalau PSD-nya ternyata tidak bisa di-rig. -->

---

## Spesifikasi Teknis

### Kanvas & Resolusi

| Item | Nilai |
|---|---|
| Kanvas PSD | **4096 × 4096 px** |
| Resolusi | 350 DPI |
| Color mode | RGB, 8-bit |
| Format kirim | `.psd` (layer utuh, tidak di-flatten) |

Resolusi per bagian (minimum, pada kanvas penuh):

| Bagian | Minimum |
|---|---|
| Kepala keseluruhan | 2048 × 2048 |
| Mata (per sisi, termasuk sclera) | 1024 × 768 |
| Iris / pupil | 512 × 512 |
| Mulut (area penuh) | 1024 × 768 |
| Tiap grup helai rambut | 1024 × 1024 |
| Badan (leher–dada) | 2048 × 1536 |

### Aturan Layer

1. **Setiap part = satu layer terpisah.** Tidak boleh ada dua objek dalam satu
   layer (contoh: alis kiri dan kanan harus terpisah).
2. **Transparansi asli** — alpha channel sungguhan, bukan background putih
   atau pola checkerboard yang digambar.
3. **Tanpa layer effect** — semua efek di-rasterize. Layer style, adjustment
   layer, dan smart object tidak terbaca Cubism.
4. **Penamaan** mengikuti [03-layer-spec.md](03-layer-spec.md) persis.
5. **Tanpa clipping mask** yang belum di-apply.

### Area Tersembunyi — paling sering terlewat

Bagian yang tertutup di tampilan depan **tetap harus digambar utuh**, karena
akan terlihat saat model bergerak:

| Yang tertutup | Harus digambar |
|---|---|
| Mata di balik poni | Mata utuh + kelopak lengkap |
| Dahi di balik poni | Dahi utuh |
| Telinga di balik rambut | Telinga utuh kiri & kanan |
| Leher di balik kerah | Leher utuh sampai pangkal |
| Badan di balik jaket | Kemeja utuh |
| Rambut belakang | Utuh, tidak terpotong siluet depan |
| Gigi & lidah | Terpisah, di belakang layer mulut |

> Ini bukan detail opsional. Tanpa ini model tidak bisa menoleh atau berkedip
> dengan benar, dan perbaikan di tahap rigging jauh lebih mahal.

---

## Spesifikasi Rigging

<!-- Bagian ini untuk lingkup B atau C. Hapus kalau hanya pesan ilustrasi. -->

Detail lengkap di [04-rigging-spec.md](04-rigging-spec.md). Ringkasnya:

**Gerakan wajib:**

- Kepala: X ±30°, Y ±30°, Z ±30°
- Mata: buka/tutup, arah pandang X/Y, kedip otomatis
- Alis: naik/turun, bentuk ekspresi
- Mulut: buka/tutup, bentuk (lip sync A/I/U/E/O)
- Badan: X/Y halus, napas otomatis
- Physics: rambut, aksesori, ornamen

**Ekspresi (7):** Normal, Senyum, Tertawa, Kaget, Marah, Sedih, Malu

**Output yang diharapkan:**

- File `.cmo3` (project Cubism, bisa diedit lagi)
- File `.moc3` + `.model3.json` + texture atlas
- File `.exp3.json` untuk tiap ekspresi
- File `.physics3.json`
- Kompatibel: **VTube Studio**

---

## Deliverables

- [ ] PSD berlayer, kanvas 4096², layer sesuai spec
- [ ] File Cubism (`.cmo3`) — sumber yang bisa diedit
- [ ] Model siap pakai (`.moc3`, `.model3.json`, texture)
- [ ] File ekspresi (`.exp3.json`) — 7 ekspresi
- [ ] File physics (`.physics3.json`)
- [ ] Emblem original (lihat §Emblem di design spec) — PNG transparan + SVG
- [ ] Video demo singkat model bergerak (opsional, untuk QA)

---

## Hak & Lisensi

Perlu disepakati tertulis **sebelum** pekerjaan dimulai:

| Hal | Kesepakatan |
|---|---|
| Hak komersial | **Ya** — model dipakai untuk stream monetized (YouTube + Saweria) |
| Hak merchandise | `{Ya / Tidak / Nego terpisah}` |
| Kepemilikan desain | `{Klien / Artist / Bersama}` |
| Kredit artist | **Ya** — dicantumkan di deskripsi channel |
| Modifikasi di masa depan | `{Boleh oleh pihak lain / Harus artist asli}` |
| File sumber (PSD/cmo3) | **Diserahkan ke klien** |

> Poin "file sumber diserahkan" penting. Tanpa itu, update kostum atau
> perbaikan di masa depan harus selalu lewat artist yang sama.

**Catatan orisinalitas:** desain ini original. Tidak boleh memakai aset,
logo, atau elemen desain milik IP lain (termasuk Genshin Impact / HoYoverse).

---

## Termin Pembayaran

Umum di pasar:

| Termin | Porsi | Saat |
|---|---|---|
| DP | 30–50% | Sebelum mulai |
| Progress | 20–30% | Setelah sketsa/lineart disetujui |
| Pelunasan | 30–40% | Setelah QA lolos, sebelum file final diserahkan |

Revisi yang termasuk: `{jumlah}` kali pada tahap sketsa, `{jumlah}` kali pada
tahap rigging. Revisi di luar itu dikenakan biaya tambahan `{nominal}`.

---

## Kontak

| | |
|---|---|
| Nama | `{ISI}` |
| Channel | https://www.youtube.com/@avivuv |
| Email | `{ISI}` |
| Kontak cepat | `{Discord / WhatsApp / Twitter}` |

---

Lanjut ke: [03-layer-spec.md](03-layer-spec.md) · [06-budget.md](06-budget.md)
