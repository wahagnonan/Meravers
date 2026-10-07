#!/usr/bin/env python3
"""Convertit un rapport Markdown du dépôt Docs en article PDF (reportlab)."""
import sys, re, html, glob
from html.parser import HTMLParser

try:
    import markdown
    from reportlab.lib.pagesizes import A4
except ImportError:  # dépendances installées dans l'environnement Termux
    sys.path.extend(glob.glob("/data/data/com.termux/files/usr/lib/python3*/site-packages"))
    import markdown
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
)

FDIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJ", f"{FDIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJ-Bold", f"{FDIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJ-Mono", f"{FDIR}/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DJ-Mono-Bold", f"{FDIR}/DejaVuSansMono-Bold.ttf"))
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJ-Bold",
                              italic="DJ", boldItalic="DJ-Bold")
pdfmetrics.registerFontFamily("DJ-Mono", normal="DJ-Mono", bold="DJ-Mono-Bold",
                              italic="DJ-Mono", boldItalic="DJ-Mono-Bold")

EMOJI = {"✅": "[OK]", "🔮": "[PROJ.]", "⚠": "[!]", "🔵": "[Q]",
         "🟠": "[R]", "📝": "[*]", "📨": "", "✔": "[OK]", "👉": ">"}

def esc(t):
    for k, v in EMOJI.items():
        t = t.replace(k, v)
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

S = {
    "body": ParagraphStyle("body", fontName="DJ", fontSize=9.3, leading=13.2,
                           spaceAfter=5, alignment=TA_JUSTIFY, splitLongWords=1),
    "h1": ParagraphStyle("h1", fontName="DJ-Bold", fontSize=16.5, leading=21,
                         spaceBefore=6, spaceAfter=9, textColor=colors.HexColor("#10263f")),
    "h2": ParagraphStyle("h2", fontName="DJ-Bold", fontSize=13, leading=16.5,
                         spaceBefore=13, spaceAfter=6, textColor=colors.HexColor("#10263f")),
    "h3": ParagraphStyle("h3", fontName="DJ-Bold", fontSize=10.8, leading=14,
                         spaceBefore=10, spaceAfter=4, textColor=colors.HexColor("#27476b")),
    "h4": ParagraphStyle("h4", fontName="DJ-Bold", fontSize=9.8, leading=13,
                         spaceBefore=8, spaceAfter=3),
    "quote": ParagraphStyle("quote", fontName="DJ", fontSize=9.3, leading=13,
                            leftIndent=14, rightIndent=8, spaceBefore=4, spaceAfter=6,
                            textColor=colors.HexColor("#333333")),
    "mono": ParagraphStyle("mono", fontName="DJ-Mono", fontSize=8.2, leading=11,
                           backColor=colors.HexColor("#f3f3f3"), spaceAfter=5),
    "li": ParagraphStyle("li", fontName="DJ", fontSize=9.3, leading=13,
                         spaceAfter=2.5, splitLongWords=1),
    "cell": ParagraphStyle("cell", fontName="DJ", fontSize=7.1, leading=9.2,
                           spaceAfter=0, splitLongWords=1),
    "cellb": ParagraphStyle("cellb", fontName="DJ-Bold", fontSize=7.1, leading=9.2,
                            spaceAfter=0, splitLongWords=1),
}

BLOCKS = ("p", "h", "li", "quote", "pre", "td", "th", "table", "tr")
INLINE_END = {"strong": "<b>", "b": "<b>", "em": "<i>", "i": "<i>",
              "code": '<font face="DJ-Mono">', "sup": "<super>", "sub": "<sub>"}

def plain(txt):
    return re.sub(r"<[^>]+>", "", html.unescape(txt))

class Conv(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.flow = []
        self.stack = [{"c": "body", "b": ""}]
        self.lists = []
        self.tbl = None
        self.row = None

    @property
    def top(self):
        return self.stack[-1]

    def add(self, s):
        if self.top["c"] in ("p", "h", "li", "quote", "pre", "td", "th"):
            self.top["b"] += s

    # ---------- start ----------
    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.stack.append({"c": "h", "lvl": int(tag[1]), "b": ""})
        elif tag == "p":
            if self.top["c"] in ("td", "th"):
                return
            self.stack.append({"c": "p", "b": ""})
        elif tag in ("ul", "ol"):
            self.lists.append([tag, 0])
        elif tag == "li":
            n = 0
            if self.lists:
                self.lists[-1][1] += 1
                n = self.lists[-1][1]
            self.stack.append({"c": "li", "lvl": len(self.lists), "n": n,
                               "ol": bool(self.lists and self.lists[-1][0] == "ol"),
                               "b": ""})
        elif tag == "table":
            self.stack.append({"c": "table", "b": ""})
            self.tbl = []
        elif tag == "tr":
            self.stack.append({"c": "tr", "b": ""})
            self.row = []
        elif tag in ("td", "th"):
            self.stack.append({"c": tag, "b": ""})
        elif tag == "blockquote":
            self.stack.append({"c": "quote", "b": ""})
        elif tag == "pre":
            self.stack.append({"c": "pre", "b": ""})
        elif tag in ("strong", "b"):
            self.add(INLINE_END["strong"])
        elif tag in ("em", "i"):
            self.add(INLINE_END["em"])
        elif tag == "code":
            self.add(INLINE_END["code"])
        elif tag == "br":
            self.add("<br/>")
        elif tag == "sup":
            self.add("<super>")
        elif tag == "sub":
            self.add("<sub>")
        elif tag == "hr":
            self.flow.append(HRFlowable(width="100%", thickness=0.6,
                                        color=colors.HexColor("#999999"),
                                        spaceBefore=6, spaceAfter=6))

    # ---------- end ----------
    def handle_endtag(self, tag):
        if tag == "blockquote":   # la frame est poussée sous le nom « quote »
            tag = "quote"
        if tag in ("strong", "b", "em", "i", "code", "sup", "sub"):
            closer = {"strong": "</b>", "b": "</b>", "em": "</i>", "i": "</i>",
                      "code": "</font>", "sup": "</super>", "sub": "</sub>"}[tag]
            self.add(closer)
            return
        if tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            return
        if tag == "hr":
            return
        # les balises de titre arrivent sous forme h1..h6 (BLOCKS ne contient que "h")
        if tag not in BLOCKS and not (len(tag) == 2 and tag[0] == "h" and tag[1].isdigit()):
            return
        # trouver et émettre la frame correspondante
        idx = None
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i]["c"] == tag or \
               (tag.startswith("h") and self.stack[i]["c"] == "h" and
                    self.stack[i].get("lvl") == int(tag[1])):
                idx = i
                break
        if idx is None:
            return
        while len(self.stack) - 1 >= idx:
            f = self.stack.pop()
            self.emit(f)

    def handle_data(self, data):
        self.add(esc(data))

    # ---------- émission ----------
    def emit(self, f):
        c, b = f["c"], f["b"].strip()
        if c == "tr":
            if self.row is not None:
                if self.tbl is not None:
                    self.tbl.append(self.row)
                self.row = None
            return
        if c == "table":
            self.build_table()
            return
        if c in ("td", "th"):
            if self.row is not None:
                self.row.append((c, b))
            return
        if not b:
            return
        tgt = self.top
        if c in ("p", "quote", "pre") and tgt["c"] in ("li", "quote", "p"):
            if tgt["b"]:
                tgt["b"] += "<br/><br/>"
            tgt["b"] += b
            return
        if c == "p":
            self.flow.append(Paragraph(b, S["body"]))
        elif c == "h":
            st = S.get(f"h{f['lvl']}", S["h4"])
            self.flow.append(Paragraph(b, st))
            if f["lvl"] == 1 and len(self.flow) <= 2:
                self.flow.append(HRFlowable(width="100%", thickness=1.2,
                                            color=colors.HexColor("#10263f"),
                                            spaceBefore=2, spaceAfter=8))
        elif c == "li":
            bullet = f"{f['n']}." if f["ol"] else "•"
            st = ParagraphStyle(f"li{len(self.flow)}", parent=S["li"],
                                leftIndent=10 + 13 * max(f["lvl"] - 1, 0),
                                bulletIndent=1 + 13 * max(f["lvl"] - 1, 0))
            self.flow.append(Paragraph(b, st, bulletText=bullet))
        elif c == "quote":
            self.flow.append(Paragraph(b, S["quote"]))
        elif c == "pre":
            self.flow.append(Paragraph(b.replace(" ", "&#160;").replace("\n", "<br/>"),
                                       S["mono"]))

    # ---------- fin de table ----------

    def close(self):
        super().close()
        while len(self.stack) > 1:
            self.emit(self.stack.pop())
        if self.row is not None and self.tbl is not None:
            self.tbl.append(self.row)
            self.row = None
        self.build_table()

    def build_table(self):
        rows = self.tbl
        self.tbl = None
        if not rows:
            return
        ncols = max(len(r) for r in rows)
        for r in rows:
            while len(r) < ncols:
                r.append(("td", ""))
        avail = A4[0] - 36 * mm
        maxlen = []
        for j in range(ncols):
            m = max((len(plain(r[j][1])) for r in rows), default=1)
            maxlen.append(max(m, 4))
        total = sum(maxlen)
        w = []
        for j in range(ncols):
            cw = avail * maxlen[j] / total
            w.append(min(max(cw, avail * 0.08), avail * 0.45))
        scale = avail / sum(w)
        w = [x * scale for x in w]
        data = []
        for i, r in enumerate(rows):
            data.append([Paragraph(txt or "&#160;",
                                   S["cellb"] if i == 0 else S["cell"])
                         for _k, txt in r])
        t = Table(data, colWidths=w, repeatRows=1, hAlign="LEFT")
        t.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b0b0b0")),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dde4ec")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 2.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ]))
        self.flow.append(Spacer(1, 4))
        self.flow.append(t)
        self.flow.append(Spacer(1, 7))


def convert(md_path, pdf_path, footer_label):
    src = open(md_path, encoding="utf-8").read()
    h = markdown.markdown(src, extensions=["tables", "sane_lists"])
    c = Conv()
    c.feed(h)
    c.close()

    def deco(canvas, doc):
        canvas.saveState()
        canvas.setFont("DJ", 7.5)
        canvas.setFillColor(colors.HexColor("#666666"))
        canvas.drawString(18 * mm, 11 * mm, footer_label)
        canvas.drawRightString(A4[0] - 18 * mm, 11 * mm, f"page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        pdf_path, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=16 * mm, bottomMargin=18 * mm,
        title=footer_label, author="Dossier de recherche Docs",
    )
    doc.build(c.flow, onFirstPage=deco, onLaterPages=deco)
    print(f"{pdf_path}: {doc.page} pages")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2], sys.argv[3])
