# -*- coding: utf-8 -*-
# Gera o PDF vertical (135 x 240 mm) e a página para celular do Guia da Trilha.
import asyncio, os, re, random, html, sys
from content import P, TH, REFS

ROOT = os.path.abspath(os.path.dirname(__file__))
IMG_PDF = 'file://' + ROOT + '/out/web/img/'
IMG_WEB = 'img/'
YEL = '#fbce5d'; NAVY = '#082758'; BLUE = '#0c3c86'; INK = '#1b2a41'

def jpg(f): return os.path.splitext(f)[0] + ('.png' if f.endswith('.png') and f in LOGOS else '.jpg')
LOGOS = {'peam_horizontal.png', 'ufc.png', 'labomar.png', 'mec_gov.png'}

def md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[\[(.+?)\]\]', r'<span class="flag">\1</span>', s)
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return s

# ---------- formas desenhadas (sem elementos de banco de imagens)
def torn(seed, n=14, amp=2.2):
    """polígono de papel rasgado (clip-path em %)"""
    r = random.Random(seed)
    pts = []
    for i in range(n + 1):
        y = i * 100 / n
        pts.append(f'{r.uniform(0, amp):.1f}% {y:.1f}%')
    right = []
    for i in range(n + 1):
        y = 100 - i * 100 / n
        right.append(f'{100 - r.uniform(0, amp * 1.8):.1f}% {y:.1f}%')
    top = f'{r.uniform(0,1):.1f}% {r.uniform(0,6):.1f}%'
    return 'polygon(' + ','.join(pts + right) + ')'

def bg_svg(th, w=135, h=240):
    r = random.Random(th)
    T = TH[th]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><rect width="{w}" height="{h}" fill="{T["bg"]}"/>']
    if th in ('agua', 'trilha', 'fim'):
        for i in range(16):
            y = r.uniform(0, h); x = r.uniform(-20, w)
            o.append(f'<path d="M{x:.1f} {y:.1f}c6 -3 12 -3 18 0s12 3 18 0" fill="none" stroke="#fff" stroke-width="{r.uniform(.5,1.2):.2f}" opacity="{r.uniform(.35,.7):.2f}" stroke-linecap="round"/>')
        for i in range(10):
            o.append(f'<circle cx="{r.uniform(0,w):.1f}" cy="{r.uniform(0,h):.1f}" r="{r.uniform(3,12):.1f}" fill="#fff" opacity="{r.uniform(.12,.3):.2f}"/>')
    elif th == 'tab':
        for i in range(26):
            x, y = r.uniform(0, w), r.uniform(0, h)
            d = f'M{x:.1f} {y:.1f}'
            for k in range(r.randint(2, 4)):
                x += r.uniform(-9, 9); y += r.uniform(-9, 9); d += f'L{x:.1f} {y:.1f}'
            o.append(f'<path d="{d}" fill="none" stroke="#a68b37" stroke-width=".55" opacity=".8"/>')
        for i, (cx, cy, rot, c) in enumerate([(128, 10, 205, '#53683d'), (120, 22, 235, '#7d960f'), (132, 34, 250, '#53683d'), (6, 228, 25, '#7d960f')]):
            o.append(f'<g transform="translate({cx} {cy}) rotate({rot})" fill="{c}" opacity=".85"><path d="M0 0q8 -3 28 0q-20 3 -28 0z"/>' + ''.join(f'<path d="M{3+j*3.2} 0q2 {(-1)**j*5} 5 {(-1)**j*8}" stroke="{c}" stroke-width="1.6" fill="none" stroke-linecap="round"/>' for j in range(7)) + '</g>')
    elif th == 'mang':
        for i in range(70):
            o.append(f'<circle cx="{r.uniform(0,w):.1f}" cy="{r.uniform(0,h):.1f}" r="{r.uniform(.3,1.1):.2f}" fill="#5c5148" opacity=".9"/>')
        o.append('<path d="M70 0h65v46c-10 4-18-2-24-10s-16-12-24-12-14-8-17-24z" fill="#1f8a63"/>')
        o.append('<path d="M70 0c3 16 9 24 17 24s18 4 24 12 14 14 24 10" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" opacity=".9"/>')
        for i in range(18):
            t = r.uniform(0, 1); x = 75 + t * 58; y = 6 + t * 36 + r.uniform(-3, 3)
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r.uniform(.5,1.6):.2f}" fill="#bfe8d6"/>')
    elif th == 'api':
        for i in range(9):
            x, y, a = r.uniform(5, w - 5), r.uniform(10, h - 10), r.uniform(0, 360)
            o.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})" stroke="#d2b896" stroke-width="1" stroke-linecap="round" fill="none"><path d="M0 0v-5M0 0l-3.6 -3.4M0 0l3.6 -3.4M0 0v2"/><g transform="translate(5 9)"><path d="M0 0v-5M0 0l-3.6 -3.4M0 0l3.6 -3.4M0 0v2"/></g></g>')
        for i in range(60):
            o.append(f'<circle cx="{r.uniform(0,w):.1f}" cy="{r.uniform(0,h):.1f}" r="{r.uniform(.2,.7):.2f}" fill="#d9c2a6"/>')
    o.append('</svg>')
    import base64
    return 'data:image/svg+xml;base64,' + base64.b64encode(''.join(o).encode()).decode()

SQUIG = '<svg class="sq" viewBox="0 0 100 6" preserveAspectRatio="none"><path d="M1 4C18 1 30 5 48 3s32-2 51 0" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/></svg>'
RIB = {th: torn(th + 'r') for th in TH}
TAGC = 'polygon(0 6%,100% 0,97% 50%,100% 100%,2% 94%,4% 50%)'
LABC = 'polygon(0 0,100% 0,95% 50%,100% 100%,0 100%,5% 50%)'

# ---------- blocos
import unicodedata
def slug(t):
    t=unicodedata.normalize('NFKD',re.sub(r'\*','',t)).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',t).strip('-')
SPX = []  # índice de espécies: (nome, sci, id, ambiente)
USED = set()
def uid(t):
    b = slug(t); k = b; i = 2
    while k in USED: k = f'{b}-{i}'; i += 1
    USED.add(k); return k
CUR_TH = ['']
def fig_lab(name, sci):
    return f'<figcaption class="fl"><span>{md(name)}</span><em>{md(sci)}</em></figcaption>'

def block(b, I):
    t = b[0]
    if t == 'card':
        _, lab, ps = b
        return f'<div class="card"><div class="lb">{md(lab)}</div>' + ''.join(f'<p>{md(p)}</p>' for p in ps) + '</div>'
    if t == 'list':
        _, lab, items = b
        return f'<div class="card"><div class="lb">{md(lab)}</div><ul>' + ''.join(f'<li>{md(x)}</li>' for x in items) + '</ul></div>'
    if t == 'note':
        return f'<div class="note">{md(b[1])}</div>'
    if t == 'img':
        st = ' style="height:calc(74mm * var(--s,1));object-fit:contain;background:#fff"' if b[1] in ('p16_1.jpg','p12_1.jpg','p78_5.jpg') else ''
        return f'<figure class="wide"><img src="{I}{jpg(b[1])}"{st} alt=""><figcaption>{md(b[2])}</figcaption></figure>'
    if t == 'pair':
        return '<div class="pair">' + ''.join(f'<figure class="wide"><img src="{I}{jpg(f)}" alt=""><figcaption>{md(c)}</figcaption></figure>' for f, c in b[1]) + '</div>'
    if t == 'gal':
        _, lab, items = b
        cls = 'gal g%d' % len(items)
        ids = [uid(n) for n, s_, f in items]
        for (n, s_, f), k in zip(items, ids): SPX.append((n, s_, k, CUR_TH[0]))
        return f'<div class="{cls}">' + ''.join(f'<figure class="ph" id="{k}"><img src="{I}{jpg(f)}" alt="{html.escape(n)} ({html.escape(s)})">{fig_lab(n, s)}</figure>' for (n, s, f), k in zip(items, ids)) + '</div>'
    if t == 'legend':
        _, name, ps, src = b
        return f'<div class="card leg"><div class="lb">Lenda</div><h3>{md(name)}</h3>' + ''.join(f'<p>{md(p)}</p>' for p in ps) + f'<p class="src">{md(src)}</p></div>'
    if t == 'sp':
        d = b[1]
        k = uid(d['name']); SPX.append((d['name'], d['sci'], k, CUR_TH[0]))
        o = f'<div class="sp" id="{k}"><figure class="ph hero"><img src="{I}{jpg(d["img"])}" style="object-position:{d["pos"]}" alt="{html.escape(d["name"])}">{fig_lab(d["name"], d["sci"])}</figure>'
        o += '<div class="card"><ul>' + ''.join(f'<li>{md(x)}</li>' for x in d['items']) + '</ul>'
        if d.get('flag'): o += f'<p><span class="flag">{md(d["flag"])}</span></p>'
        o += '</div>'
        if d.get('note'): o += f'<div class="note">{md(d["note"])}</div>'
        if d['extra']:
            o += '<div class="pair">' + ''.join(f'<figure class="wide sm"><img src="{I}{jpg(f)}" alt=""><figcaption>{md(c)}</figcaption></figure>' for f, c in d['extra']) + '</div>'
        return o + '</div>'
    raise ValueError(t)

# ---------- seções
SECS = [
 ('apresentacao', 'agua', 'Apresentação', 'Quem somos: o PEAM, o CEAC e a APA do Rio Pacoti.', 'p03_4.jpg'),
 ('trilha', 'trilha', 'A trilha', 'O percurso e os cuidados antes de começar.', 'p16_1.jpg'),
 ('tabuleiro', 'tab', 'Mata de tabuleiro', 'O primeiro ambiente da trilha: uma mata de transição entre Caatinga, Cerrado e Mata Atlântica.', 'p23_6.jpg'),
 ('manguezal', 'mang', 'Manguezal', 'O berçário da vida marinha: formação, carbono azul, plantas, animais e lendas.', 'p44_5.jpg'),
 ('apicum', 'api', 'Apicum', 'A planície salgada na borda do mangue.', 'p84_10.jpg'),
 ('encerramento', 'fim', 'Encerramento', 'Por que conservar o estuário do Rio Pacoti.', 'p25_10.jpg'),
]
SECIDX = {s[0]: i for i, s in enumerate(SECS)}

# ====================== PDF
CSS_PDF = """
@page{size:135mm 240mm;margin:0}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{font-family:'Inter',sans-serif;color:#1b2a41;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:135mm;height:240mm;position:relative;overflow:hidden;page-break-after:always;background-size:cover}
.hd{position:absolute;left:0;right:0;top:7mm;height:24mm}
.rib{position:absolute;z-index:1;left:7mm;top:0;padding:3mm 7mm 4.2mm 5mm;color:#fff;font-family:'Inter Display','Inter';font-weight:800;font-size:19pt;letter-spacing:-.01em;line-height:1;white-space:nowrap}
.rib::before{content:'';position:absolute;inset:0;background:var(--rib);clip-path:var(--clip);z-index:-1}
.rib::after{content:'';position:absolute;left:2.4mm;right:-2.4mm;top:2.2mm;bottom:-1.8mm;background:var(--lab);opacity:.55;clip-path:var(--clip);z-index:-2}
.rib .sq{position:absolute;left:5mm;right:7mm;bottom:1.6mm;height:2.2mm;width:auto}
.tag{position:absolute;right:7mm;top:15.5mm;background:var(--lab);color:#fff;font-weight:700;font-size:7.6pt;letter-spacing:.09em;text-transform:uppercase;padding:1.4mm 4mm;clip-path:""" + TAGC + """}
.body{position:absolute;left:7mm;right:7mm;top:33mm;bottom:15mm;font-size:calc(9.6pt * var(--s,1));line-height:1.42;display:flex;flex-direction:column;justify-content:flex-start}
.ft{position:absolute;left:7mm;right:7mm;bottom:5.5mm;display:flex;align-items:center;justify-content:space-between;font-size:6.6pt;color:var(--fink)}
.ft .n{width:7.4mm;height:7.4mm;border-radius:50%;background:#fff;color:var(--rib);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:7.4pt}
.card{background:#fff;border:.6mm solid var(--lab);border-radius:2.2mm;padding:5.4mm 4.2mm 2.6mm;position:relative;margin:5mm 0 2.8mm}
.card:first-child{margin-top:3mm}
.lb{position:absolute;top:-3.4mm;left:50%;transform:translateX(-50%);background:var(--lab);color:#fff;font-weight:700;font-size:7.6pt;letter-spacing:.08em;text-transform:uppercase;padding:1.1mm 5mm;white-space:nowrap;clip-path:""" + LABC + """}
.card p{margin:0 0 2.2mm;hyphens:auto}
.card ul{margin:0;padding:0 0 0 4mm}.card li{margin:0 0 1.9mm;padding-left:.6mm;hyphens:auto}.card li::marker{color:var(--lab)}
.sp .card{margin-top:3mm}.sp .card ul{padding-top:.4mm}
.note{background:var(--lab);color:#fff;border-radius:2.2mm;padding:3mm 4mm;margin:2mm 0 2.6mm;font-size:.93em;line-height:1.38}
.note b{color:#fff}
.ph{margin:0;position:relative;border:.7mm solid var(--lab);border-radius:2mm;background:#fff;padding:0 0 4mm}
.ph img{display:block;width:100%;height:calc(30mm * var(--s,1));object-fit:cover;border-radius:1.4mm 1.4mm 0 0}
.ph.hero img{height:calc(70mm * var(--s,1))}
.fl{position:absolute;left:50%;bottom:-3mm;transform:translateX(-50%);background:var(--lab);color:#fff;text-align:center;padding:.9mm 5mm 1mm;clip-path:""" + LABC + """;white-space:nowrap;line-height:1.05;min-width:62%}
.fl span{display:block;font-weight:700;font-size:7.8pt;letter-spacing:.05em;text-transform:uppercase}
.fl em{display:block;font-size:6.3pt;font-weight:400;opacity:.95}
.gal{display:grid;grid-template-columns:1fr 1fr;gap:6.4mm 3.4mm;margin:2mm 0 5mm}
.gal.g3>.ph:last-child,.gal.g5>.ph:last-child{grid-column:1/3;justify-self:center;width:calc(50% - 1.7mm)}
.gal .ph img{height:calc(34mm * var(--s,1))}
.wide{margin:2mm 0 3mm}.wide img{display:block;width:100%;height:calc(52mm * var(--s,1));object-fit:cover;border-radius:2mm;border:.7mm solid #fff}
.wide figcaption{font-size:6.8pt;margin-top:1mm;color:var(--fink);font-style:italic}
.pair{display:flex;gap:3mm}.pair .wide{flex:1}.pair .wide img{height:calc(36mm * var(--s,1))}
.pair .wide.sm img{height:calc(28mm * var(--s,1))}
.leg h3{font-family:'Inter Display';font-weight:800;font-size:1.25em;color:var(--rib);margin:0 0 2mm}
.leg p{text-indent:0}.leg .src{font-size:.86em;font-style:italic;color:#5a6472;margin-top:1mm}
.flag{background:#fff2b8;color:#6b4f00;border:1px dashed #c9a100;border-radius:1mm;padding:0 1mm;font-size:.82em;font-style:normal;font-weight:600}
b{font-weight:700;color:var(--ink)}
"""

def theme_vars(th):
    T = TH[th]
    fink = '#f2efe9' if T['dark'] else '#3f5168'
    return f"--rib:{T['rib']};--lab:{T['lab']};--ink:{T['ink']};--fink:{fink};--clip:{RIB[th]};background-image:url({bg_svg(th)})"

PAGES = []  # (html) ; numeração automática
def add(h): PAGES.append(h)

def foot(n, run):
    return f'<div class="ft"><span>Guia da Trilha Ecológica do Rio Pacoti · PEAM</span><span class="n">{n}</span></div>'

def content_page(p):
    n = len(PAGES) + 1
    body = ''.join(block(b, IMG_PDF) for b in p['blocks'])
    return f'<section class="pg" style="{theme_vars(p["th"])}"><div class="hd"><div class="rib">{md(p["title"])}{SQUIG}</div><div class="tag">{md(p["tag"])}</div></div><div class="body fit">{body}</div>{foot(n, p["title"])}</section>'

def divider(i, sec):
    sid, th, name, desc, img = sec
    T = TH[th]
    n = len(PAGES) + 1
    items = {
      'apresentacao': ['O PEAM', 'O CEAC', 'A APA do Rio Pacoti'],
      'trilha': ['Introdução', 'Recomendações'],
      'tabuleiro': ['Formação', 'Flora', 'Fauna'],
      'manguezal': ['Formação e ciclos', 'Flora', 'Moluscos, crustáceos e peixes', 'Lendas do mangue'],
      'apicum': ['Formação', 'Flora', 'Fauna'],
      'encerramento': ['Importância ecológica', 'Relevância socioeconômica'],
    }[sid]
    lst = ''.join(f'<li>{x}</li>' for x in items)
    return f'''<section class="pg" style="{theme_vars(th)}">
<div style="position:absolute;left:9mm;top:20mm;width:15mm;height:15mm;border-radius:50%;background:{YEL};color:{NAVY};display:flex;align-items:center;justify-content:center;font-family:'Inter Display';font-weight:800;font-size:19pt">{i+1}</div>
<div class="rib" style="top:44mm;left:7mm;font-size:27pt;padding:4mm 9mm 5.6mm 6mm">{name}{SQUIG}</div>
<div style="position:absolute;left:9mm;right:12mm;top:72mm;font-size:12pt;line-height:1.38;font-weight:600;color:{'#fff' if T['dark'] else T['ink']}">{desc}</div>
<figure class="ph" style="position:absolute;left:9mm;right:9mm;top:104mm;padding:0;border-width:1mm"><img src="{IMG_PDF}{jpg(img)}" style="height:80mm;border-radius:1.4mm"></figure>
<ul style="position:absolute;left:9mm;right:9mm;top:194mm;margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:2mm">{''.join(f'<li style="background:#fff;color:{T["rib"]};font-weight:700;font-size:7.8pt;padding:1.4mm 3mm;border-radius:9mm">{x}</li>' for x in items)}</ul>
{foot(n,name)}</section>'''

def cover():
    T = TH['agua']
    return f'''<section class="pg" style="{theme_vars('agua')}">
<div style="position:absolute;left:0;right:0;top:0;height:30mm;background:#fff;display:flex;align-items:center;justify-content:center"><img src="{IMG_PDF}peam_horizontal.png" style="height:15mm"></div>
<div style="position:absolute;left:9mm;right:9mm;top:42mm">
<div style="font-weight:700;font-size:8.4pt;letter-spacing:.14em;text-transform:uppercase;color:{T['lab']}">Guia educacional</div>
<div class="rib" style="position:relative;left:-2mm;top:3mm;display:inline-block;font-size:24pt;line-height:1.04;white-space:normal;padding:4.4mm 9mm 6.6mm 6mm">Trilha Ecológica do Estuário do Rio Pacoti{SQUIG}</div>
<div style="margin-top:9mm;font-size:10.5pt;line-height:1.4;color:{T['ink']}">Mata de tabuleiro, manguezal e apicum na APA do Rio Pacoti, em Eusébio (CE)</div>
<div style="margin-top:5mm;font-weight:700;font-size:10pt;color:{T['ink']}">Erick Souza da Rocha</div></div>
<div style="position:absolute;left:9mm;right:9mm;top:122mm;height:84mm;border-radius:50% 50% 3mm 3mm / 30% 30% 3mm 3mm;overflow:hidden;border:1.2mm solid #fff"><img src="{IMG_PDF}{jpg('p44_5.jpg')}" style="width:100%;height:100%;object-fit:cover"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:24mm;background:#fff;display:flex;align-items:center;justify-content:center;gap:7mm">
<img src="{IMG_PDF}ufc.png" style="height:12mm"><img src="{IMG_PDF}labomar.png" style="height:7mm"><img src="{IMG_PDF}mec_gov.png" style="height:9mm"></div></section>'''

def plain(title, inner, th='fim', tag=''):
    n = len(PAGES) + 1
    return f'<section class="pg" style="{theme_vars(th)}"><div class="hd"><div class="rib">{title}{SQUIG}</div>{f"<div class=tag>{tag}</div>" if tag else ""}</div><div class="body fit">{inner}</div>{foot(n,title)}</section>'

def ficha():
    T = TH['fim']
    return f'''<div class="card" style="font-size:.92em"><div class="lb">Expediente</div>
<p><b>Texto e projeto original</b><br>Erick Souza da Rocha</p>
<p><b>Coordenação</b><br>Ravena Sthefany Alves Nogueira</p>
<p><b>Revisão técnica</b><br>Ravena Sthefany Alves Nogueira</p>
<p><b>Fotografias</b><br>Ver a página de créditos das imagens.</p>
<p><b>Projeto gráfico desta edição</b><br>PEAM, a partir da identidade visual criada por Erick Souza da Rocha</p>
<p><b>Realização</b><br>Programa de Educação Ambiental Marinha (PEAM) · Instituto de Ciências do Mar (LABOMAR) · Universidade Federal do Ceará (UFC)</p></div>
<div class="card" style="font-size:.88em"><div class="lb">Licença</div>
<p><b>CC BY-NC-ND 4.0</b>. Você pode copiar e compartilhar este material, em qualquer formato, desde que dê o crédito ao autor, não o utilize para fins comerciais e não o modifique. <span class="flag">a confirmar com o autor</span></p></div>
<div class="card" style="font-size:.88em"><div class="lb">Como citar</div>
<p>ROCHA, Erick Souza da. <b>Guia educacional da Trilha Ecológica do Estuário do Rio Pacoti</b>. Fortaleza: PEAM/LABOMAR/UFC, 2026. E-book.</p></div>'''

def build_pdf_pages():
    PAGES.clear()
    add(cover())
    add(plain('Ficha técnica', ficha(), 'agua'))
    add('__SUMARIO__')
    add(plain('Este guia', f'''<div class="card"><div class="lb">Para quem é</div>
<p>Este guia acompanha a <b>Trilha Ecológica do Estuário do Rio Pacoti</b>, realizada pelo PEAM no CEAC, em Eusébio. Ele foi pensado para <b>monitores, professores e visitantes</b> que querem conhecer os ambientes da trilha antes, durante ou depois da visita.</p>
<p>O percurso passa por três ambientes: a <b>mata de tabuleiro</b>, o <b>manguezal</b> e o <b>apicum</b>. Cada um tem uma cor neste guia, para facilitar a navegação.</p></div>
<div class="card"><div class="lb">Cores dos ambientes</div><ul>
<li><b style="color:{TH['tab']['lab']}">Mata de tabuleiro</b>: verde-oliva sobre o chão rachado da mata.</li>
<li><b style="color:{TH['mang']['rib']}">Manguezal</b>: verde-mangue sobre a lama.</li>
<li><b style="color:{TH['api']['rib']}">Apicum</b>: laranja sobre a areia salgada.</li>
<li><b style="color:{TH['agua']['rib']}">Apresentação e encerramento</b>: azul da água do estuário.</li></ul></div>
<div class="note">As espécies ameaçadas citadas seguem as listas nacionais atualizadas em 2026 (Portarias GM/MMA nº 1.667/2026 e MMA nº 1.704/2026) e as listas vermelhas do Ceará.</div>''', 'agua', 'Como usar'))
    starts = {}
    cur = None
    for p in P:
        if p.get('sec') in SECIDX and p['sec'] != cur and p['sec'] not in ('lendas',):
            s = SECS[SECIDX[p['sec']]]
            starts[s[0]] = len(PAGES) + 1
            add(divider(SECIDX[p['sec']], s)); cur = p['sec']
        if p.get('sec') == 'lendas': starts['lendas'] = len(PAGES) + 1
        add(content_page(p))
    starts['autor'] = len(PAGES) + 1
    add(plain('Sobre o autor', f'''<div style="display:flex;gap:4mm;align-items:center;margin:3mm 0 4mm"><div style="flex:none;width:30mm;height:36mm;border-radius:3mm;border:.8mm dashed {TH['fim']['lab']};background:#fff;display:flex;align-items:center;justify-content:center;text-align:center;font-size:7pt;color:#6b7a90;padding:2mm">[foto do autor]</div>
<div style="font-family:'Inter Display';font-weight:800;font-size:15pt;color:{TH['fim']['rib']};line-height:1.1">Erick Souza da Rocha</div></div>
<div class="card"><div class="lb">Quem escreveu</div><p><span class="flag">a confirmar: formação, vínculo com o PEAM e o LABOMAR e uma breve apresentação, em 3 a 5 linhas</span></p>
<p>Erick criou este guia e a sua identidade visual a partir da experiência como monitor da Trilha Ecológica do Estuário do Rio Pacoti. <span class="flag">a confirmar</span></p></div>''', 'fim'))
    starts['refs'] = len(PAGES) + 1
    half = (len(REFS) + 1) // 2
    for i, chunk in enumerate([REFS[:half], REFS[half:]]):
        add(plain('Referências', '<div class="card refs" style="font-size:.86em;line-height:1.34"><div class="lb">' + ('Bibliografia' if i == 0 else 'Bibliografia (cont.)') + '</div>' + ''.join(f'<p style="margin:0 0 2.2mm;text-align:left;hyphens:none">{md(r)}</p>' for r in chunk) + '</div>', 'fim'))
    starts['cred'] = len(PAGES) + 1
    # créditos
    rows = []
    for idx, h in enumerate(PAGES, 1):
        for f in re.findall(r'/out/web/img/(p\d\d_\d+)\.jpg', h):
            rows.append((idx, f))
    seen = []; lines = []
    for idx, f in rows:
        if f in seen: continue
        seen.append(f); lines.append(idx)
    pg_list = sorted(set(lines))
    add(plain('Créditos das imagens', f'''<div class="card"><div class="lb">Fotografias</div>
<p>As fotografias desta edição vêm do material original do guia. A autoria e a licença de cada imagem ainda precisam ser confirmadas e indicadas aqui, no formato "Página: autor (licença)".</p>
<p><span class="flag">a confirmar: créditos das fotos das páginas {', '.join(str(x) for x in pg_list)}</span></p>
<p>Algumas fotos de caranguejos trazem a marca d'água de outro site e devem ser <b>substituídas ou autorizadas</b> antes da publicação.</p></div>
<div class="card"><div class="lb">Ilustrações</div><p>Fundos, faixas e ícones desenhados para esta edição, inspirados na identidade visual criada por Erick Souza da Rocha.</p></div>''', 'fim'))
    add(f'''<section class="pg" style="{theme_vars('agua')}"><div style="position:absolute;left:12mm;right:12mm;top:70mm;text-align:center;color:{TH['agua']['ink']}">
<div style="background:#fff;border-radius:4mm;padding:6mm 6mm;display:inline-block"><img src="{IMG_PDF}peam_horizontal.png" style="height:16mm;display:block"></div>
<p style="font-size:10pt;line-height:1.45;margin-top:8mm">Programa de Educação Ambiental Marinha<br>Instituto de Ciências do Mar · LABOMAR<br>Universidade Federal do Ceará</p>
<p style="font-size:8.6pt;margin-top:6mm">Centro de Estudos Ambientais Costeiros (CEAC)<br>APA do Rio Pacoti · Eusébio, Ceará</p></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:24mm;background:#fff;display:flex;align-items:center;justify-content:center;gap:7mm"><img src="{IMG_PDF}ufc.png" style="height:12mm"><img src="{IMG_PDF}labomar.png" style="height:7mm"><img src="{IMG_PDF}mec_gov.png" style="height:9mm"></div></section>''')
    # sumário
    rows = [(str(i+1), s[2], starts[s[0]]) for i, s in enumerate(SECS)]
    rows.insert(4, ('', 'Lendas do mangue', starts['lendas']))
    rows += [('', 'Sobre o autor', starts['autor']), ('', 'Referências', starts['refs']), ('', 'Créditos das imagens', starts['cred'])]
    li = ''.join(f'<div style="display:flex;align-items:center;gap:3mm;padding:2.4mm 0;border-bottom:1px solid #e3ecec"><span style="flex:none;width:7mm;height:7mm;border-radius:50%;background:{YEL if n else "transparent"};color:{NAVY};font-weight:800;font-size:8pt;display:flex;align-items:center;justify-content:center">{n}</span><span style="flex:1;font-weight:{700 if n else 500};font-size:{10 if n else 9}pt;padding-left:{0 if n else 2}mm">{t}</span><span style="font-weight:700;color:{TH["agua"]["rib"]};font-size:9pt">{pnum}</span></div>' for n, t, pnum in rows)
    PAGES[2] = plain('Sumário', f'<div class="card" style="padding-top:4mm">{li}</div>', 'agua')
    return PAGES

def write_pdf_html():
    pages = build_pdf_pages()
    doc = f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS_PDF}</style></head><body>{"".join(pages)}</body></html>'
    open(ROOT + '/out/guia_pdf.html', 'w').write(doc)
    return len(pages)

FIT_JS = """() => {
 const out=[];
 document.querySelectorAll('.pg').forEach((pg,i)=>{
  const b=pg.querySelector('.body'); if(!b) return;
  let s=1; b.style.setProperty('--s',s);
  const over=()=>b.scrollHeight>b.clientHeight+1 || [...b.children].some(c=>c.getBoundingClientRect().bottom>b.getBoundingClientRect().bottom+1);
  while(over() && s>0.7){ s=Math.round((s-0.02)*100)/100; b.style.setProperty('--s',s); }
  if(over()) out.push([i+1,'OVERFLOW',s]); else if(s<0.86) out.push([i+1,'small',s]);
 });
 return out;}"""

async def render_pdf(n):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page()
        await pg.goto('file://' + ROOT + '/out/guia_pdf.html', wait_until='networkidle')
        rep = await pg.evaluate(FIT_JS)
        await pg.pdf(path=ROOT + '/out/Guia_Trilha_Rio_Pacoti_PEAM_rascunho.pdf', width='135mm', height='240mm', print_background=True, prefer_css_page_size=True)
        await br.close()
        return rep

if __name__ == '__main__':
    n = write_pdf_html()
    rep = asyncio.run(render_pdf(n))
    print(n, 'páginas'); print(rep)

# ====================== PÁGINA PARA CELULAR
CSS_WEB = """
:root{--water:#dfeeee;--deep:#14315f;--peam:#275db1;--sun:#fbce5d;--paper:#ffffff;--font-display:'Inter',system-ui,sans-serif;--font-body:'Inter',system-ui,sans-serif;color-scheme:light}
/* layout: uma coluna para celular; cada ambiente da trilha é uma faixa com o fundo e a cor da identidade do Erick */
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font-family:var(--font-body);color:#1b2a41;background:var(--water);font-size:16.5px;line-height:1.55}
img{max-width:100%}
.top{position:sticky;top:0;z-index:20;background:#fff;box-shadow:0 2px 10px rgba(8,39,88,.12)}
.top .row{display:flex;align-items:center;gap:10px;padding:8px 14px;max-width:620px;margin:0 auto}
.top img{height:30px;display:block}
.top .tt{font-weight:700;font-size:13px;color:#14315f;line-height:1.15}
.nav{display:flex;gap:6px;overflow-x:auto;padding:0 14px 9px;max-width:620px;margin:0 auto;scrollbar-width:none}
.nav::-webkit-scrollbar{display:none}
.nav a:focus-visible,summary:focus-visible{outline:3px solid var(--sun);outline-offset:2px}
.nav a{flex:none;text-decoration:none;font-size:13px;font-weight:700;padding:6px 12px;border-radius:99px;color:#fff;white-space:nowrap}
.wrap{max-width:620px;margin:0 auto;padding:0 16px}
.sec{background-size:100% auto;background-repeat:repeat-y;padding:30px 0 34px;scroll-margin-top:96px}
.rib{position:relative;z-index:1;display:inline-block;color:#fff;font-weight:800;font-size:27px;letter-spacing:-.015em;line-height:1.05;padding:10px 26px 15px 16px;margin:6px 0 10px}
.rib::before{content:'';position:absolute;inset:0;background:var(--rib);clip-path:var(--clip);z-index:-1}
.rib::after{content:'';position:absolute;left:8px;right:-8px;top:8px;bottom:-6px;background:var(--lab);opacity:.55;clip-path:var(--clip);z-index:-2}
.rib .sq{position:absolute;left:16px;right:26px;bottom:6px;height:8px;width:auto}
.num{width:46px;height:46px;border-radius:50%;background:#fbce5d;color:#082758;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px}
.desc{font-weight:600;font-size:18px;line-height:1.4;margin:4px 0 8px;color:var(--hd)}
.tag{display:inline-block;background:var(--lab);color:#fff;font-weight:700;font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;padding:6px 16px;margin:26px 0 4px;clip-path:""" + TAGC + """}
.card{background:#fff;border:2.5px solid var(--lab);border-radius:10px;padding:24px 17px 8px;position:relative;margin:24px 0 14px}
.lb{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--lab);color:#fff;font-weight:700;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;padding:5px 20px;white-space:nowrap;clip-path:""" + LABC + """}
.card p{margin:0 0 12px}
.card ul{margin:0 0 6px;padding-left:20px}.card li{margin:0 0 9px}.card li::marker{color:var(--lab)}
.sp{margin:22px 0 8px}.sp .card{margin-top:12px;padding-top:16px}
.note{background:var(--lab);color:#fff;border-radius:10px;padding:13px 16px;margin:12px 0 14px;font-size:15.5px;line-height:1.45}
.note b{color:#fff}
.ph{margin:0;position:relative;border:3px solid var(--lab);border-radius:9px;background:#fff;padding:0 0 20px}
.ph img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:6px 6px 0 0}
.ph.hero img{aspect-ratio:4/3.4}
.fl{position:absolute;left:50%;bottom:-14px;transform:translateX(-50%);background:var(--lab);color:#fff;text-align:center;padding:4px 22px 5px;clip-path:""" + LABC + """;white-space:nowrap;line-height:1.1;min-width:64%}
.fl span{display:block;font-weight:700;font-size:13.5px;letter-spacing:.05em;text-transform:uppercase}
.fl em{display:block;font-size:11.5px;opacity:.95}
.gal{display:grid;grid-template-columns:1fr 1fr;gap:30px 12px;margin:20px 0 26px}
.gal .fl{min-width:88%;padding:4px 10px 5px}.gal .fl span{font-size:11.5px}.gal .fl em{font-size:10px;white-space:normal}
.gal.g3>.ph:last-child,.gal.g5>.ph:last-child{grid-column:1/3;justify-self:center;width:calc(50% - 6px)}
.wide{margin:14px 0 16px}.wide img{display:block;width:100%;border-radius:9px;border:3px solid #fff;aspect-ratio:16/10;object-fit:cover}
.wide figcaption{font-size:13px;margin-top:5px;color:var(--fink);font-style:italic}
.pair{display:flex;gap:10px}.pair .wide{flex:1;margin-top:6px}.pair .wide img{aspect-ratio:1/1}
.leg h3{font-weight:800;font-size:21px;color:var(--rib);margin:0 0 8px;line-height:1.2}
.leg .src{font-size:13.5px;font-style:italic;color:#5a6472}
.flag{background:#fff2b8;color:#6b4f00;border:1px dashed #c9a100;border-radius:4px;padding:0 4px;font-size:.84em;font-weight:600}
b{font-weight:700;color:var(--ink)}
.hero-top{background:#fff;text-align:center;padding:18px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 18px}.chips a{background:#fff;color:var(--rib);font-weight:700;font-size:13px;padding:6px 12px;border-radius:99px;text-decoration:none}
.secimg{border:4px solid #fff;border-radius:12px;overflow:hidden;margin:10px 0 4px}.secimg img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
details{background:#fff;border-radius:10px;padding:12px 16px;margin:12px 0;border:2.5px solid var(--lab)}
summary{font-weight:700;color:var(--rib);cursor:pointer}
details p{font-size:14.5px;line-height:1.45;margin:10px 0}
.logos{background:#fff;display:flex;justify-content:center;align-items:center;gap:22px;padding:20px 12px}
.logos img{height:34px}
footer{background:#14315f;color:#dbe7f8;font-size:13px;text-align:center;padding:18px 16px 30px}
"""

def web():
    SPX.clear(); USED.clear()
    I = IMG_WEB
    secs_html = []
    nav = []
    # capa
    cov = f'''<section class="sec" id="inicio" style="{theme_vars('agua')};--hd:{TH['agua']['ink']}"><div class="wrap">
<div style="font-weight:700;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:{TH['agua']['lab']}">Guia educacional</div>
<div class="rib" style="font-size:32px;margin-top:10px">Trilha Ecológica do Estuário do Rio Pacoti{SQUIG}</div>
<p class="desc">Mata de tabuleiro, manguezal e apicum na APA do Rio Pacoti, em Eusébio (CE)</p>
<p style="font-weight:700;color:{TH['agua']['ink']};margin:0 0 14px">Erick Souza da Rocha</p>
<div class="secimg" style="border-radius:50% 50% 12px 12px / 22% 22% 12px 12px"><img src="{I}p44_5.jpg" alt="Manguezal do Rio Pacoti" style="aspect-ratio:4/3.6"></div>
<div class="card" style="margin-top:28px"><div class="lb">Como usar</div><p>Este guia acompanha a trilha do PEAM no CEAC. Use os botões no topo para ir direto a cada ambiente. Cada ambiente tem uma cor: <b style="color:{TH['tab']['lab']}">verde-oliva</b> para a mata de tabuleiro, <b style="color:{TH['mang']['rib']}">verde-mangue</b> para o manguezal e <b style="color:{TH['api']['rib']}">laranja</b> para o apicum.</p></div>
</div></section>'''
    secs_html.append(cov)
    cur = None; buf = ''; last_tag = None
    def close():
        nonlocal buf
        if buf: secs_html.append(buf + '</div></section>'); buf = ''
    for p in P:
        if p.get('sec') in SECIDX and p['sec'] != cur:
            close()
            i = SECIDX[p['sec']]; sid, th, name, desc, img = SECS[i]
            T = TH[th]; hd = '#fff' if T['dark'] else T['ink']
            nav.append(f'<a href="#{sid}" style="background:{T["rib"]}">{name}</a>')
            buf = f'<section class="sec" id="{sid}" style="{theme_vars(th)};--hd:{hd}"><div class="wrap"><div class="num">{i+1}</div><div class="rib">{name}{SQUIG}</div><p class="desc">{desc}</p>'
            cur = p['sec']; last_tag = None
        if p.get('sec') == 'lendas':
            buf += '<div id="lendas" style="scroll-margin-top:96px"></div>'
            nav.append(f'<a href="#lendas" style="background:{TH["mang"]["lab"]}">Lendas</a>')
        if p['tag'] != last_tag:
            first = p['blocks'][0]
            dup = first[0] in ('card','list') and first[1].lower() == p['tag'].lower()
            if not dup: buf += f'<div><span class="tag">{md(p["tag"])}</span></div>'
            last_tag = p['tag']
        CUR_TH[0] = TH[p['th']]['name']
        buf += ''.join(block(b, I) for b in p['blocks'])
    close()
    T = TH['fim']
    refs = ''.join(f'<p>{md(r)}</p>' for r in REFS)
    back = f'''<section class="sec" id="sobre" style="{theme_vars('fim')};--hd:{T['ink']}"><div class="wrap">
<div class="rib">Sobre o autor{SQUIG}</div>
<div class="card"><div class="lb">Erick Souza da Rocha</div><p><span class="flag">a confirmar: foto, formação, vínculo com o PEAM e o LABOMAR e uma breve apresentação</span></p><p>Erick criou este guia e a sua identidade visual a partir da experiência como monitor da Trilha Ecológica do Estuário do Rio Pacoti. <span class="flag">a confirmar</span></p></div>
<details><summary>Referências</summary>{refs}</details>
<details><summary>Créditos das imagens</summary><p>As fotografias vêm do material original do guia. A autoria e a licença de cada imagem ainda precisam ser confirmadas e indicadas aqui. Algumas fotos de caranguejos trazem a marca d'água de outro site e devem ser substituídas ou autorizadas antes da publicação. <span class="flag">a confirmar</span></p><p>Fundos, faixas e ícones foram desenhados para esta edição, inspirados na identidade visual criada por Erick Souza da Rocha.</p></details>
<details><summary>Ficha técnica, licença e como citar</summary>
<p><b>Texto e projeto original:</b> Erick Souza da Rocha<br><b>Coordenação e revisão técnica:</b> Ravena Sthefany Alves Nogueira<br><b>Projeto gráfico desta edição:</b> PEAM<br><b>Realização:</b> PEAM · LABOMAR · UFC</p>
<p><b>Licença:</b> CC BY-NC-ND 4.0. Pode copiar e compartilhar, com crédito ao autor, sem fins comerciais e sem modificar. <span class="flag">a confirmar com o autor</span></p>
<p><b>Como citar:</b> ROCHA, Erick Souza da. <b>Guia educacional da Trilha Ecológica do Estuário do Rio Pacoti</b>. Fortaleza: PEAM/LABOMAR/UFC, 2026.</p></details>
</div></section>'''
    secs_html.append(back)
    nav.append(f'<a href="#sobre" style="background:{T["rib"]}">Créditos</a>')
    head = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Guia da Trilha do Rio Pacoti</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&display=swap" rel="stylesheet">
<style>{CSS_WEB}</style></head><body>
<header class="top"><div class="row"><img src="{I}peam_horizontal.png" alt="PEAM"><div class="tt">Guia da Trilha Ecológica<br><span style="font-weight:500">Estuário do Rio Pacoti</span></div></div>
<nav class="nav">{''.join(nav)}</nav></header>'''
    foot_ = f'''<div class="logos"><img src="{I}ufc.png" alt="UFC" style="height:44px"><img src="{I}labomar.png" alt="LABOMAR" style="height:26px"><img src="{I}mec_gov.png" alt="MEC" style="height:32px"></div>
<footer>Programa de Educação Ambiental Marinha · LABOMAR · UFC<br>CEAC · APA do Rio Pacoti · Eusébio, Ceará</footer></body></html>'''
    doc = head + ''.join(secs_html) + foot_
    doc = doc.replace('<img src="img/p', '<img loading="lazy" src="img/p')
    return doc

if __name__ == '__main__':
    open(ROOT + '/out/web/index.html', 'w').write(web())
