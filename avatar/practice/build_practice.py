"""
Membuat practice.psd - karakter sederhana dengan struktur layer BENAR untuk Live2D.

Tujuan: latihan rigging di Cubism. Gambarnya sederhana (bentuk geometris),
tapi strukturnya persis seperti PSD produksi:
  - posisi anatomis (mata di posisi mata, bukan berjejer di grid)
  - area tersembunyi digambar utuh (sclera elips penuh, dahi utuh, telinga utuh)
  - poni terpecah 3 helai untuk physics
  - penamaan sesuai ../03-layer-spec.md

Jalankan: python build_practice.py
"""
from PIL import Image, ImageDraw
import struct, io

W = H = 2048
CX = W // 2

# Palet dari ../01-character-design.md
HAIR     = (0x12, 0x13, 0x1A, 255)
HAIR_TIP = (0x3F, 0xC5, 0xDB, 255)
SKIN     = (0xEF, 0xC3, 0xA8, 255)
SKIN_SH  = (0xC9, 0x90, 0x79, 255)
SCLERA   = (0xF4, 0xF6, 0xF8, 255)
IRIS     = (0x2A, 0x8C, 0xA3, 255)
IRIS_IN  = (0x7F, 0xE9, 0xF5, 255)
PUPIL    = (0x0E, 0x14, 0x18, 255)
WHITE    = (255, 255, 255, 255)
BROW     = (0x1A, 0x1B, 0x22, 255)
MOUTH_IN = (0x5A, 0x2A, 0x2E, 255)
TEETH    = (0xF8, 0xF4, 0xF0, 255)
TONGUE   = (0xD4, 0x6A, 0x72, 255)
SHIRT    = (0x15, 0x16, 0x1C, 255)
JACKET   = (0x0B, 0x0C, 0x11, 255)
GOLD     = (0xB8, 0x93, 0x5A, 255)
CYAN     = (0x3F, 0xC5, 0xDB, 255)
BLUSH    = (0xE0, 0x8A, 0x80, 160)

layers = []   # urutan: BELAKANG -> DEPAN


def new():
    return Image.new('RGBA', (W, H), (0, 0, 0, 0))


def add(name, im):
    layers.append((name, im))


# ---------- 05_HAIR_BACK (paling belakang) ----------
for i, (dx, wd) in enumerate([(-190, 300), (0, 340), (190, 300)], 1):
    im = new(); d = ImageDraw.Draw(im)
    d.ellipse([CX + dx - wd // 2, 380, CX + dx + wd // 2, 1180], fill=HAIR)
    add('HairBack_0%d' % i, im)

# ---------- 04_BODY ----------
im = new(); d = ImageDraw.Draw(im)
d.ellipse([CX - 520, 1320, CX + 520, 2100], fill=SKIN_SH)
add('Body_Base', im)

im = new(); d = ImageDraw.Draw(im)                       # leher UTUH sampai pangkal
d.rounded_rectangle([CX - 105, 1090, CX + 105, 1460], 40, fill=SKIN)
d.ellipse([CX - 105, 1400, CX + 105, 1500], fill=SKIN_SH)
add('Neck', im)

im = new(); d = ImageDraw.Draw(im)                       # kemeja UTUH di balik jaket
d.polygon([(CX - 330, 1430), (CX + 330, 1430), (CX + 390, 2048), (CX - 390, 2048)], fill=SHIRT)
for y in range(1520, 2000, 120):
    d.ellipse([CX - 14, y, CX + 14, y + 28], fill=(0x30, 0x32, 0x3A, 255))
add('Shirt', im)

for side, sx in (('L', -1), ('R', 1)):
    im = new(); d = ImageDraw.Draw(im)
    x0 = CX + sx * 150
    d.polygon([(x0, 1440), (CX + sx * 470, 1500), (CX + sx * 520, 2048), (x0 + sx * 60, 2048)], fill=JACKET)
    d.line([(x0, 1450), (CX + sx * 460, 1510)], fill=GOLD, width=14)
    add('Jacket_%s' % side, im)

im = new(); d = ImageDraw.Draw(im)
d.polygon([(CX - 200, 1400), (CX - 110, 1430), (CX - 160, 1620)], fill=JACKET)
d.polygon([(CX + 200, 1400), (CX + 110, 1430), (CX + 160, 1620)], fill=JACKET)
d.line([(CX - 200, 1400), (CX - 160, 1620)], fill=GOLD, width=10)
d.line([(CX + 200, 1400), (CX + 160, 1620)], fill=GOLD, width=10)
add('Jacket_Collar', im)

for side, sx in (('L', -1), ('R', 1)):
    im = new(); d = ImageDraw.Draw(im)
    cx = CX + sx * 400
    d.regular_polygon((cx, 1560, 52), 4, rotation=45, fill=GOLD)
    d.regular_polygon((cx, 1560, 22), 4, rotation=45, fill=CYAN)
    add('Ornament_Shoulder_%s' % side, im)

im = new(); d = ImageDraw.Draw(im)
d.line([(CX, 1460), (CX, 1680)], fill=GOLD, width=8)
d.regular_polygon((CX, 1720, 46), 4, rotation=0, fill=GOLD)
d.regular_polygon((CX, 1720, 24), 4, rotation=0, fill=CYAN)
add('Accessory_Chest', im)

# ---------- 03_HEAD ----------
im = new(); d = ImageDraw.Draw(im)
d.ellipse([CX - 330, 330, CX + 330, 1180], fill=SKIN_SH)
add('Head_Base', im)

for side, sx in (('L', -1), ('R', 1)):                   # telinga UTUH
    im = new(); d = ImageDraw.Draw(im)
    cx = CX + sx * 320
    d.ellipse([cx - 48, 700, cx + 48, 880], fill=SKIN)
    d.ellipse([cx - 24, 740, cx + 24, 840], fill=SKIN_SH)
    add('Ear_%s' % side, im)

for side, sx in (('L', -1), ('R', 1)):
    im = new(); d = ImageDraw.Draw(im)
    x = CX + sx * 300
    d.polygon([(x - sx * 40, 420), (x + sx * 90, 520), (x + sx * 70, 980), (x - sx * 30, 900)], fill=HAIR)
    d.polygon([(x + sx * 70, 900), (x + sx * 72, 980), (x + sx * 40, 960)], fill=HAIR_TIP)
    add('HairSide_%s' % side, im)

# ---------- 02_FACE ----------
im = new(); d = ImageDraw.Draw(im)                       # wajah + DAHI UTUH
d.ellipse([CX - 290, 380, CX + 290, 1140], fill=SKIN)
d.polygon([(CX - 180, 950), (CX + 180, 950), (CX, 1150)], fill=SKIN)
add('Face_Base', im)

im = new(); d = ImageDraw.Draw(im)
d.ellipse([CX - 230, 820, CX - 110, 880], fill=BLUSH)
d.ellipse([CX + 110, 820, CX + 230, 880], fill=BLUSH)
add('Blush', im)

im = new(); d = ImageDraw.Draw(im)
d.line([(CX, 760), (CX - 18, 830)], fill=SKIN_SH, width=9)
add('Nose', im)

# MOUTH - urutan belakang ke depan
im = new(); d = ImageDraw.Draw(im)
d.ellipse([CX - 105, 920, CX + 105, 1000], fill=MOUTH_IN)
add('Mouth_Inside', im)

im = new(); d = ImageDraw.Draw(im)
d.rounded_rectangle([CX - 72, 968, CX + 72, 998], 14, fill=TEETH)
add('Teeth_Lower', im)

im = new(); d = ImageDraw.Draw(im)
d.ellipse([CX - 52, 958, CX + 52, 1000], fill=TONGUE)
add('Tongue', im)

im = new(); d = ImageDraw.Draw(im)
d.rounded_rectangle([CX - 80, 922, CX + 80, 952], 14, fill=TEETH)
add('Teeth_Upper', im)

im = new(); d = ImageDraw.Draw(im)
d.ellipse([CX - 108, 905, CX + 108, 1008], fill=SKIN)
d.arc([CX - 78, 938, CX + 78, 982], 0, 180, fill=(0x8A, 0x4A, 0x4E, 255), width=11)
add('Mouth_Line', im)

# EYES - sclera ELIPS PENUH (wajib supaya iris bisa bergerak)
for side, sx in (('L', -1), ('R', 1)):
    ex = CX + sx * 135

    im = new(); d = ImageDraw.Draw(im)
    d.ellipse([ex - 105, 640, ex + 105, 790], fill=SCLERA)
    add('EyeWhite_%s' % side, im)

    im = new(); d = ImageDraw.Draw(im)
    d.ellipse([ex - 56, 655, ex + 56, 775], fill=IRIS)
    d.ellipse([ex - 34, 680, ex + 34, 760], fill=IRIS_IN)
    add('Iris_%s' % side, im)

    im = new(); d = ImageDraw.Draw(im)
    d.ellipse([ex - 24, 685, ex + 24, 750], fill=PUPIL)
    add('Pupil_%s' % side, im)

    im = new(); d = ImageDraw.Draw(im)
    d.ellipse([ex - 40, 655, ex - 10, 692], fill=WHITE)
    d.ellipse([ex + 18, 735, ex + 34, 754], fill=(255, 255, 255, 170))
    add('EyeHighlight_%s' % side, im)

    im = new(); d = ImageDraw.Draw(im)                   # kelopak WARNA KULIT
    d.ellipse([ex - 110, 745, ex + 110, 810], fill=SKIN)
    add('EyeLid_Lower_%s' % side, im)

    im = new(); d = ImageDraw.Draw(im)
    d.ellipse([ex - 110, 600, ex + 110, 672], fill=SKIN)
    add('EyeLid_Upper_%s' % side, im)

    im = new(); d = ImageDraw.Draw(im)
    d.arc([ex - 108, 618, ex + 108, 760], 180, 360, fill=(0x10, 0x12, 0x18, 255), width=16)
    add('EyeLash_%s' % side, im)

for side, sx in (('L', -1), ('R', 1)):
    im = new(); d = ImageDraw.Draw(im)
    bx = CX + sx * 135
    d.rounded_rectangle([bx - 92, 598, bx + 92, 628], 15, fill=BROW)
    add('Brow_%s' % side, im)

# ---------- 01_HAIR_FRONT: poni 3 helai (WAJIB untuk physics) ----------
poni = [(-175, 360, 200, 520, 585), (0, 330, 180, 545, 610), (175, 360, 200, 520, 585)]
for i, (dx, wd, hw, y1, tip) in enumerate(poni, 1):
    im = new(); d = ImageDraw.Draw(im)
    x = CX + dx
    d.polygon([(x - wd // 2, 360), (x + wd // 2, 360), (x + hw // 2, y1), (x - hw // 2, y1)], fill=HAIR)
    d.polygon([(x - hw // 2, y1 - 30), (x + hw // 2, y1 - 30), (x, tip)], fill=HAIR)
    d.polygon([(x - 26, tip - 46), (x + 26, tip - 46), (x, tip)], fill=HAIR_TIP)
    add('HairFront_0%d' % i, im)

# ---------- 06_FX ----------
im = new(); d = ImageDraw.Draw(im)
for (x, y, r) in [(300, 620, 26), (1760, 700, 22), (400, 1300, 18), (1680, 1250, 24), (250, 900, 14)]:
    d.ellipse([x - r, y - r, x + r, y + r], fill=(0x7F, 0xE9, 0xF5, 110))
add('FX_Particle_01', im)


# =================== penulis PSD ===================

def rle_encode(data, h, w):
    """PackBits per baris - format RLE yang dipakai PSD."""
    out = bytearray()
    counts = []
    for r in range(h):
        row = data[r * w:(r + 1) * w]
        enc = bytearray()
        i = 0
        while i < len(row):
            run = 1
            while i + run < len(row) and run < 128 and row[i + run] == row[i]:
                run += 1
            if run > 1:
                enc += bytes([257 - run, row[i]])
                i += run
            else:
                s = i
                while i < len(row) and (i + 1 >= len(row) or row[i + 1] != row[i]) and i - s < 128:
                    i += 1
                enc += bytes([i - s - 1]) + row[s:i]
        counts.append(len(enc))
        out += enc
    return bytes(out), counts


def write_psd(path, layers, w, h):
    buf = io.BytesIO()
    buf.write(b'8BPS' + struct.pack('>H', 1) + b'\0' * 6)
    buf.write(struct.pack('>HIIHH', 4, h, w, 8, 3))
    buf.write(struct.pack('>I', 0))
    buf.write(struct.pack('>I', 0))

    li = io.BytesIO()
    li.write(struct.pack('>h', -len(layers)))
    blobs = []
    for name, im in layers:
        bands = im.split()
        chans = []
        for cid, band in ((-1, bands[3]), (0, bands[0]), (1, bands[1]), (2, bands[2])):
            enc, counts = rle_encode(band.tobytes(), h, w)
            blob = struct.pack('>H', 1) + b''.join(struct.pack('>H', c) for c in counts) + enc
            chans.append((cid, blob))
        blobs.append(chans)

        li.write(struct.pack('>iiii', 0, 0, h, w))
        li.write(struct.pack('>H', 4))
        for cid, blob in chans:
            li.write(struct.pack('>hI', cid, len(blob)))
        li.write(b'8BIM' + b'norm' + struct.pack('>BBBB', 255, 0, 0, 0))

        nb = name.encode('latin1')
        pas = bytes([len(nb)]) + nb
        pas += b'\0' * ((4 - len(pas) % 4) % 4)
        uni = name.encode('utf-16-be')
        luni = b'8BIM' + b'luni' + struct.pack('>I', 4 + len(uni)) + struct.pack('>I', len(name)) + uni
        if len(luni) % 2:
            luni += b'\0'
        extra = struct.pack('>I', 0) + struct.pack('>I', 0) + pas + luni
        li.write(struct.pack('>I', len(extra)) + extra)

    for chans in blobs:
        for cid, blob in chans:
            li.write(blob)

    lid = li.getvalue()
    if len(lid) % 2:
        lid += b'\0'
    lm = struct.pack('>I', len(lid)) + lid + struct.pack('>I', 0)
    buf.write(struct.pack('>I', len(lm)) + lm)

    flat = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    for _, im in layers:
        flat.alpha_composite(im)
    buf.write(struct.pack('>H', 0))
    fb = flat.split()
    for band in (fb[0], fb[1], fb[2], fb[3]):
        buf.write(band.tobytes())

    with open(path, 'wb') as f:
        f.write(buf.getvalue())


if __name__ == '__main__':
    write_psd('practice.psd', layers, W, H)
    print('practice.psd dibuat: %dx%d, %d layer' % (W, H, len(layers)))
    for i, (n, _) in enumerate(layers):
        print('  %2d  %s' % (i, n))
