#!/usr/bin/env python3
"""Codec GIM PSP INDEX8 (sg_chaname / sg_title) — decode y encode.

Estructura GIM (verificada en sg_chaname.gim, 197840 B):
- 0x00: cabecera 16 B "MIG.00.1PSP".
- 0x10: chunk ROOT tipo 2.
- 0x20: chunk PICTURE tipo 3.
- 0x30: chunk IMAGE tipo 4, tamaño 196688; cabecera de chunk 16 B;
  cabecera de imagen 64 B (0x40-0x7F) con ancho/alto u16 en 0x48;
  píxeles swizzled INDEX8 en 0x80..0x3007F (512*384 = 196608 B).
- 0x30080: chunk PALETTE tipo 5, tamaño 1104; cabecera de chunk 16 B;
  cabecera de paleta 64 B (0x30090-0x300CF); 256 colores RGBA8888 en
  0x300D0..0x304CF (1024 B).

Swizzle PSP 8 bits: bloques de 16x8 px.
  swizzle(x, y, w) = ((y//8)*(w//16) + (x//16)) * 128 + (y%8)*16 + (x%16)
"""
import struct

from PIL import Image

FILE_HDR = 16
IMG_CHUNK_OFF = 0x30
IMG_PIX_OFF = 0x80          # píxeles dentro del .gim
PAL_CHUNK_OFF = None         # se calcula: IMG_CHUNK_OFF + tamaño chunk IMAGE


def parse_gim(path):
    d = open(path, "rb").read()
    assert d[:11] == b"MIG.00.1PSP", d[:11]
    img_size = struct.unpack_from("<I", d, IMG_CHUNK_OFF + 4)[0]
    img_hdr = IMG_CHUNK_OFF + 16
    w, h = struct.unpack_from("<HH", d, img_hdr + 8)
    pix_off = img_hdr + 64
    pix_len = w * h
    pal_off = IMG_CHUNK_OFF + img_size
    pal_size = struct.unpack_from("<I", d, pal_off + 4)[0]
    pal_data_off = pal_off + 16 + 64
    pal = []
    for i in range(256):
        r, g, b, a = d[pal_data_off + i * 4: pal_data_off + i * 4 + 4]
        pal.append((r, g, b, a))
    return {
        "raw": d,
        "width": w,
        "height": h,
        "pix_off": pix_off,
        "pix_len": pix_len,
        "pal_off": pal_off,
        "pal_data_off": pal_data_off,
        "palette": pal,
        "img_size": img_size,
        "pal_size": pal_size,
    }


def swizzle_off(x, y, w):
    return ((y // 8) * (w // 16) + (x // 16)) * 128 + (y % 8) * 16 + (x % 16)


def unswizzle(pix, w, h):
    """pix: bytes swizzled (len w*h). Devuelve bytes lineales (índices)."""
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            out[y * w + x] = pix[swizzle_off(x, y, w)]
    return bytes(out)


def swizzle(linear, w, h):
    """linear: bytes lineales (índices). Devuelve bytes swizzled."""
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            out[swizzle_off(x, y, w)] = linear[y * w + x]
    return bytes(out)


def gim_to_png(gim_path, png_path):
    g = parse_gim(gim_path)
    pix = g["raw"][g["pix_off"]: g["pix_off"] + g["pix_len"]]
    lin = unswizzle(pix, g["width"], g["height"])
    img = Image.new("RGBA", (g["width"], g["height"]))
    pal = g["palette"]
    px = img.load()
    for y in range(g["height"]):
        for x in range(g["width"]):
            px[x, y] = pal[lin[y * g["width"] + x]]
    img.save(png_path)
    return g


def png_to_gim_indices(png_path, w, h, palette):
    """Redimensiona el PNG a (w,h), lo cuantiza a la paleta dada (lista de
    256 RGBA) y devuelve los índices lineales. Usa distancia RGBA."""
    img = Image.open(png_path).convert("RGBA").resize((w, h), Image.LANCZOS)
    # mapa color->índice (redondeo a RGB, alpha como está)
    # Construir tabla de búsqueda por color exacto primero, luego nearest.
    pal_rgb = [(r, g, b) for (r, g, b, a) in palette]
    # Usar PIL quantize con paleta personalizada es más rápido: crear imagen P
    pal_img = Image.new("P", (16, 16))
    flat = []
    for (r, g, b, a) in palette:
        flat.extend([r, g, b])
    pal_img.putpalette(flat)
    # quantize necesita imagen RGB; convertir y cuantizar con dithering off
    rgb = img.convert("RGB")
    q = rgb.quantize(palette=pal_img, dither=Image.NONE)
    return bytes(q.tobytes()), img


if __name__ == "__main__":
    import sys
    g = gim_to_png("gim/sg_chaname.gim", "/tmp/sg_chaname-decode.png")
    print("decode OK:", g["width"], "x", g["height"],
          "pix_off", hex(g["pix_off"]), "pal_data_off", hex(g["pal_data_off"]))
