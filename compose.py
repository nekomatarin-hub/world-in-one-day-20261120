#!/usr/bin/env python3
"""Compose the final entry image for make.fun's
"Sum up 20 November's world news in one image" (news-image-20261120).

Layout on a 1024x1024 canvas:
  - header band with the date (the judge is not told the day, so the
    image itself must name it),
  - the AI-drawn 3x2 editorial collage (no text in the artwork itself),
  - a caption bar at the bottom of each panel with a headline and one
    short factual line, set in a real font so nothing is garbled,
  - a footer ticker with the day's other stories for breadth.

Stories verified against Friday 20 November 2026 reporting (One Turn's
daily brief topic pages, crawled 21 November):
  * Russia fired 400+ drones and 110 missiles at Ukraine overnight,
    at least 8 killed in Kyiv; two missiles and a suspected drone came
    down in eastern Poland during European drills — PM Tusk called it
    a likely deliberate provocation, NATO a grave violation.
  * AI/chip sell-off: S&P 500 and Dow entered correction, Nasdaq fell
    more than 5% and erased its 2026 gains; Anthropic shares fell
    about 11% a day after their debut; gold fell about 4%.
  * The International Court of Justice ruled Myanmar's security forces
    committed state-sponsored genocide against the Rohingya.
  * UK PM Andy Burnham signed three UK-EU agreements in Brussels:
    food exports, carbon markets and youth mobility.
  * Trump, Xi and Putin's first trilateral summit in Shenzhen ended
    with few concrete results.
  * A magnitude 6.7 earthquake struck near Cerro de Pasco in central
    Peru; buildings were evacuated in Lima.
  Ticker: tanker fire near Hormuz as Trump says he is not rushing an
  Iran decision; student protests across 25 European countries and a
  general strike in Italy; LA jury convicts the Palisades Fire
  arsonist; Japan core inflation rises to a year high; Philippines and
  Chile sign a free-trade agreement at APEC.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BASE = HERE / "assets" / "media-generation-news-collage-base-20261120-0-7ddc7feb-0e13-460c-ad21-3363d76c0423.webp"
OUT = HERE / "entry.png"

W = 1024
HEADER_H = 88
FOOTER_H = 72
GRID_H = W - HEADER_H - FOOTER_H  # 864

NAVY = (11, 29, 51)
GOLD = (242, 193, 78)
WHITE = (255, 255, 255)
BAR = (10, 14, 20)

FONT_DIR = Path("/usr/share/fonts/truetype/noto")
BOLD = str(FONT_DIR / "NotoSans-Bold.ttf")
REG = str(FONT_DIR / "NotoSans-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


PANELS = [
    ("UKRAINE BARRAGE",
     "400+ drones & 110 missiles hit Kyiv — two missiles land in Poland"),
    ("AI PLUNGE",
     "S&P 500 & Dow in correction — Nasdaq falls 5%, erasing 2026 gains"),
    ("GENOCIDE RULING",
     "World Court: Myanmar committed genocide against the Rohingya"),
    ("UK–EU DEALS",
     "Burnham signs food, carbon & youth mobility pacts in Brussels"),
    ("SHENZHEN SUMMIT",
     "Trump, Xi & Putin's first trilateral ends with few concrete results"),
    ("PERU EARTHQUAKE",
     "Magnitude 6.7 quake strikes central Peru — Lima evacuates"),
]

TICKER = ("ALSO TODAY:  Hormuz tanker ablaze as Trump 'not rushing' Iran decision  ·  Students march in 25 "
          "European countries, Italy strikes  ·  LA jury convicts Palisades Fire arsonist  ·  Japan inflation at year high")


def main():
    base = Image.open(BASE).convert("RGB").resize((W, GRID_H), Image.LANCZOS)
    canvas = Image.new("RGB", (W, W), NAVY)
    canvas.paste(base, (0, HEADER_H))
    draw = ImageDraw.Draw(canvas, "RGBA")

    # Header: the date, big and unambiguous.
    title = "FRIDAY 20 NOVEMBER 2026"
    f_title = font(BOLD, 41)
    tw = draw.textlength(title, font=f_title)
    draw.text(((W - tw) / 2, 10), title, font=f_title, fill=WHITE)
    sub = "THE WORLD IN ONE DAY"
    f_sub = font(BOLD, 19)
    sw = draw.textlength(sub, font=f_sub)
    draw.text(((W - sw) / 2, 58), sub, font=f_sub, fill=GOLD)

    # Caption bars over the bottom of each panel.
    cell_w = W / 3
    cell_h = GRID_H / 2
    bar_h = 102
    f_head = font(BOLD, 24)
    f_body = font(REG, 17)
    for i, (head, body) in enumerate(PANELS):
        col, row = i % 3, i // 3
        x0 = col * cell_w
        y1 = HEADER_H + (row + 1) * cell_h
        draw.rectangle([x0, y1 - bar_h, x0 + cell_w, y1], fill=BAR + (222,))
        draw.text((x0 + 11, y1 - bar_h + 7), head, font=f_head, fill=GOLD)
        for j, line in enumerate(wrap(draw, body, f_body, cell_w - 22)):
            draw.text((x0 + 11, y1 - bar_h + 42 + j * 21), line, font=f_body, fill=WHITE)

    # Footer ticker.
    fy = HEADER_H + GRID_H
    draw.rectangle([0, fy, W, W], fill=NAVY)
    f_tick = font(REG, 16)
    for j, line in enumerate(wrap(draw, TICKER, f_tick, W - 28)):
        lw = draw.textlength(line, font=f_tick)
        draw.text(((W - lw) / 2, fy + 8 + j * 22), line, font=f_tick, fill=(225, 232, 240))

    canvas.save(OUT, optimize=True)
    print(OUT, OUT.stat().st_size, "bytes", canvas.size)


if __name__ == "__main__":
    main()
