# Rigging Spec — Parameter Live2D

Spesifikasi untuk rigger. Nama parameter memakai **ID standar Cubism** supaya
langsung kompatibel dengan VTube Studio tanpa remapping.

---

## Parameter Wajib

### Kepala

| Parameter ID | Range | Default | Keterangan |
|---|---|---|---|
| `ParamAngleX` | -30 … 30 | 0 | Menoleh kiri/kanan |
| `ParamAngleY` | -30 … 30 | 0 | Menunduk/mendongak |
| `ParamAngleZ` | -30 … 30 | 0 | Memiringkan kepala |

> V1 menulis `ParamAngleY: -20…+20`. Direkomendasikan **±30** supaya gerak
> mendongak terasa natural. Ini butuh gambar leher yang utuh (sudah dicakup
> di layer spec).

### Mata

| Parameter ID | Range | Default | Keterangan |
|---|---|---|---|
| `ParamEyeLOpen` | 0 … 1 | 1 | Buka/tutup mata kiri |
| `ParamEyeROpen` | 0 … 1 | 1 | Buka/tutup mata kanan |
| `ParamEyeBallX` | -1 … 1 | 0 | Arah pandang horizontal |
| `ParamEyeBallY` | -1 … 1 | 0 | Arah pandang vertikal |
| `ParamEyeLSmile` | 0 … 1 | 0 | Mata melengkung (senyum) |
| `ParamEyeRSmile` | 0 … 1 | 0 | Mata melengkung (senyum) |

### Alis

| Parameter ID | Range | Default | Keterangan |
|---|---|---|---|
| `ParamBrowLY` | -1 … 1 | 0 | Alis kiri naik/turun |
| `ParamBrowRY` | -1 … 1 | 0 | Alis kanan naik/turun |
| `ParamBrowLForm` | -1 … 1 | 0 | Bentuk alis kiri (marah ↔ sedih) |
| `ParamBrowRForm` | -1 … 1 | 0 | Bentuk alis kanan |

### Mulut

| Parameter ID | Range | Default | Keterangan |
|---|---|---|---|
| `ParamMouthOpenY` | 0 … 1 | 0 | Buka/tutup — dipakai lip sync |
| `ParamMouthForm` | -1 … 1 | 0 | Bentuk: -1 cemberut, +1 senyum |

**Lip sync A/I/U/E/O** dibentuk dari kombinasi dua parameter di atas:

| Vokal | `MouthOpenY` | `MouthForm` |
|---|---|---|
| A | 1.0 | 0.0 |
| I | 0.3 | 1.0 |
| U | 0.4 | -1.0 |
| E | 0.6 | 0.5 |
| O | 0.8 | -0.5 |
| (diam) | 0.0 | 0.0 |

### Badan

| Parameter ID | Range | Default | Keterangan |
|---|---|---|---|
| `ParamBodyAngleX` | -10 … 10 | 0 | Badan miring kiri/kanan |
| `ParamBodyAngleY` | -10 … 10 | 0 | Badan maju/mundur |
| `ParamBodyAngleZ` | -10 … 10 | 0 | Badan berputar |
| `ParamBreath` | 0 … 1 | 0 | Napas — otomatis, siklus ~3.5 detik |

### Tambahan

| Parameter ID | Range | Default | Keterangan |
|---|---|---|---|
| `ParamCheek` | 0 … 1 | 0 | Blush pipi |
| `ParamHairFront` | -1 … 1 | 0 | Physics poni |
| `ParamHairSide` | -1 … 1 | 0 | Physics rambut samping |
| `ParamHairBack` | -1 … 1 | 0 | Physics rambut belakang |
| `ParamAccessory` | -1 … 1 | 0 | Physics liontin |
| `ParamFXWind` | 0 … 1 | 0 | Intensitas efek angin |
| `ParamFXGlow` | 0 … 1 | 0.5 | Intensitas glow cyan |

---

## Ekspresi (`.exp3.json`)

Tujuh file ekspresi. Nilai di bawah adalah titik awal — rigger boleh
menyesuaikan selama karakternya terbaca.

| Ekspresi | File | Parameter utama |
|---|---|---|
| Normal | `exp_normal.exp3.json` | semua default |
| Senyum | `exp_senyum.exp3.json` | `MouthForm` 0.7 · `EyeLSmile`/`EyeRSmile` 0.4 |
| Tertawa | `exp_tertawa.exp3.json` | `MouthOpenY` 0.9 · `MouthForm` 1.0 · `EyeLSmile`/`EyeRSmile` 1.0 |
| Kaget | `exp_kaget.exp3.json` | `EyeLOpen`/`EyeROpen` 1.0 · `BrowLY`/`BrowRY` 1.0 · `MouthOpenY` 0.7 |
| Marah | `exp_marah.exp3.json` | `BrowLForm`/`BrowRForm` -1.0 · `BrowLY`/`BrowRY` -0.6 · `MouthForm` -0.7 |
| Sedih | `exp_sedih.exp3.json` | `BrowLForm`/`BrowRForm` 1.0 · `EyeLOpen`/`EyeROpen` 0.6 · `MouthForm` -0.5 |
| Malu | `exp_malu.exp3.json` | `Cheek` 1.0 · `EyeBallX` -0.5 · `MouthForm` -0.2 |

---

## Physics (`.physics3.json`)

### Rambut

| Grup | Input | Kekuatan | Redam | Catatan |
|---|---|---|---|---|
| Poni | `ParamAngleX`, `ParamAngleZ` | sedang | tinggi | Gerak kecil — jangan berlebihan |
| Rambut samping | `ParamAngleX`, `ParamAngleZ` | tinggi | sedang | Paling terlihat saat menoleh |
| Rambut belakang | `ParamAngleX`, `ParamBodyAngleX` | tinggi | rendah | Gerak paling lambat & luas |

Delay antar grup dibuat sedikit berbeda supaya tidak bergerak serempak —
rambut yang bergerak barengan terlihat artifisial.

### Aksesori

| Grup | Input | Kekuatan | Redam |
|---|---|---|---|
| Liontin dada | `ParamBodyAngleX`, `ParamBodyAngleZ` | sedang | tinggi |
| Ornamen bahu | `ParamBodyAngleX` | rendah | tinggi |

> Ornamen logam harus bergerak **sedikit saja** — logam kaku, bukan kain.
> Ini detail kecil yang membedakan rig bagus dan rig medioker.

---

## Auto-Motion

Gerakan idle yang berjalan otomatis tanpa input tracking:

| Gerakan | Siklus | Amplitudo |
|---|---|---|
| Napas | ~3.5 detik | `ParamBreath` 0 → 1 |
| Kedip | acak 2–6 detik | `EyeLOpen`/`EyeROpen` 1 → 0 → 1 (~0.15s) |
| Sway idle | ~8 detik | `BodyAngleX` ±2 |

---

## Target Performa

| Item | Target |
|---|---|
| Jumlah ArtMesh | < 150 |
| Texture atlas | 2048² × 2 atau 4096² × 1 |
| Frame rate | 60 fps stabil |
| Beban GPU | Ringan — harus jalan bareng game |

> Konteks: PC memakai RTX 5060 8GB dan streaming game berat (Genshin,
> Ragnarok). Model harus efisien supaya tidak memakan budget GPU yang
> dibutuhkan game dan encoder.

---

## Kompatibilitas

Target utama: **VTube Studio**

- Face tracking: webcam, atau iPhone (ARKit) kalau tersedia
- Hotkey ekspresi: 7 ekspresi di-bind ke F1–F7
- Output: transparan, untuk OBS Game Capture / Window Capture

Setelan OBS terkait ada di [_obs-setting.md](../_obs-setting.md).

---

Lanjut ke: [05-status-assets-v1.md](05-status-assets-v1.md) · [07-qa-checklist.md](07-qa-checklist.md)
