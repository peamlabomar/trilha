# -*- coding: utf-8 -*-
# Gera o site instalável (PWA) do Guia da Trilha, pronto para hospedagem estática (GitHub Pages).
import os, re, json, hashlib, html
import build
from content import TH

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = ROOT + '/out/site'
VERSAO = '1.0-rascunho'
DATA = '13/11/2026'
BASE_URL = 'https://peamlabomar.github.io/trilha/'

doc = build.web()

# 1. fontes próprias (funcionam offline)
FONTS = """@font-face{font-family:'Inter';src:url(fonts/inter-regular.woff) format('woff');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url(fonts/inter-italic.woff) format('woff');font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:'Inter';src:url(fonts/inter-medium.woff) format('woff');font-weight:500 600;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url(fonts/inter-bold.woff) format('woff');font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url(fonts/inter-extrabold.woff) format('woff');font-weight:800;font-style:normal;font-display:swap}
"""
doc = re.sub(r'<link rel="preconnect"[^>]+>\s*<link rel="preconnect"[^>]+>\s*<link href="https://fonts.googleapis.com[^>]+>', '', doc)
doc = doc.replace('<style>', '<style>' + FONTS, 1)

# 2. fotos em WebP
doc = re.sub(r'img/(p\d\d_\d+)\.jpg', r'img/\1.webp', doc)

# 3. cabeçalho: app instalável e prévia de link
desc = 'Guia educacional da Trilha Ecológica do Estuário do Rio Pacoti (PEAM/LABOMAR/UFC): mata de tabuleiro, manguezal e apicum, com plantas, animais e lendas.'
og_img = (BASE_URL + 'img/og.jpg') if BASE_URL else 'img/og.jpg'
HEAD = f'''<meta name="description" content="{desc}">
<meta name="theme-color" content="#275db1">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Trilha PEAM">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="Guia da Trilha Ecológica do Rio Pacoti">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
{f'<meta property="og:url" content="{BASE_URL}">' if BASE_URL else ''}'''
doc = doc.replace('<title>', HEAD + '\n<title>', 1)

# 4. busca no topo
CSS_ADD = """
.skip{position:absolute;left:-999px;top:0;background:#fff;padding:8px 12px;z-index:50}.skip:focus{left:8px}
.find{position:relative;max-width:620px;margin:0 auto;padding:0 14px 10px}
.find input{width:100%;font:inherit;font-size:15px;padding:9px 12px 9px 36px;border:2px solid #cfe0e0;border-radius:99px;background:#f4f9f9 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23275db1' stroke-width='2.4' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='M20 20l-3.5-3.5'/%3E%3C/svg%3E") no-repeat 11px center/17px;color:#14315f}
.find input:focus{outline:none;border-color:#275db1;background-color:#fff}
.res{position:absolute;left:14px;right:14px;top:100%;margin-top:-4px;background:#fff;border-radius:12px;box-shadow:0 10px 30px rgba(8,39,88,.22);max-height:60vh;overflow:auto;display:none;z-index:30}
.res a{display:flex;justify-content:space-between;gap:10px;padding:11px 14px;text-decoration:none;color:#14315f;border-bottom:1px solid #eef3f3}
.res a i{color:#5a6a7a;font-size:13px}.res a small{flex:none;font-size:11.5px;font-weight:700;color:#fff;padding:2px 8px;border-radius:99px;align-self:center}
.res .none{padding:12px 14px;color:#5a6a7a;font-size:14px}
.off{display:flex;gap:12px;align-items:flex-start;background:#fff;border-radius:12px;padding:13px 15px;margin:4px 0 18px;border-left:6px solid var(--sun);font-size:14.5px;line-height:1.45;color:#14315f}
.off .ico{flex:none;width:30px;height:30px;border-radius:50%;background:#fff3c4;display:flex;align-items:center;justify-content:center;font-weight:800;color:#8a6a00}
.off.ok{border-left-color:#2e9e6b}.off.ok .ico{background:#d8f2e5;color:#1f7a50}
.off button{margin-top:8px;font:inherit;font-weight:700;font-size:14px;background:#275db1;color:#fff;border:0;border-radius:99px;padding:8px 16px}
.idx h3{font-size:15px;margin:18px 0 6px;color:var(--rib)}
.idx ul{list-style:none;margin:0;padding:0;columns:2;column-gap:14px}
.idx li{break-inside:avoid;margin:0 0 7px;font-size:14.5px;line-height:1.25}.idx li a{color:#14315f;text-decoration:none;font-weight:600}
.idx li i{display:block;font-size:12px;color:#5a6a7a;font-weight:400}
.ver{opacity:.75;font-size:12px;margin-top:8px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
:target{scroll-margin-top:140px}
.sp,.ph{scroll-margin-top:140px}
.gal .fl{white-space:normal;width:94%;min-width:0}.gal .fl span{font-size:11px;line-height:1.15;word-break:break-word}
"""
doc = doc.replace('</style>', CSS_ADD + '</style>', 1)
doc = doc.replace('<body>', '<body><a class="skip" href="#inicio">Pular para o conteúdo</a>', 1)
doc = doc.replace('<nav class="nav">', '<nav class="nav" aria-label="Ambientes da trilha">', 1)
doc = doc.replace('</nav></header>', '</nav><div class="find"><label for="q" class="skip">Buscar espécie</label><input id="q" type="search" placeholder="Buscar espécie: uçá, carnaúba, guaiamum…" autocomplete="off"><div class="res" id="res" role="listbox"></div></div></header>', 1)

# 5. aviso de uso offline, logo após o autor na capa
OFF = '''<div class="off" id="off"><div class="ico">!</div><div><b>Vai fazer a trilha?</b> Abra este guia uma vez com internet (no Wi-Fi ou antes de sair de casa). Depois ele funciona <b>sem sinal</b>, inclusive no meio do mangue.<div id="offmsg"></div><button id="inst" hidden>Instalar no celular</button><div id="ios" hidden style="margin-top:6px;font-size:13.5px">No iPhone: toque em <b>Compartilhar</b> e depois em <b>Adicionar à Tela de Início</b>.</div></div></div>'''
doc = doc.replace('<div class="secimg"', OFF + '<div class="secimg"', 1)

# 6. índice de espécies antes dos créditos
grupos = {}
for n, s, k, amb in build.SPX:
    if k.endswith('-2') and k[:-2] in [x[2] for x in build.SPX]: continue
    grupos.setdefault(amb, []).append((n, s, k))
cor = {TH[t]['name']: TH[t]['rib'] for t in TH}
IDX = '<section class="sec" id="especies" style="' + build.theme_vars('fim') + ';--hd:#14315f"><div class="wrap"><div class="rib">Todas as espécies' + build.SQUIG + '</div><p class="desc">Toque no nome para ir direto à espécie.</p><div class="card idx"><div class="lb">Índice</div>'
for amb in ['Mata de tabuleiro', 'Manguezal', 'Apicum']:
    if amb not in grupos: continue
    IDX += f'<h3 style="color:{cor[amb]}">{amb}</h3><ul>' + ''.join(f'<li><a href="#{k}">{html.escape(n)}<i>{html.escape(s)}</i></a></li>' for n, s, k in sorted(grupos[amb], key=lambda x: x[0])) + '</ul>'
IDX += '</div></div></section>'
doc = doc.replace('<section class="sec" id="sobre"', IDX + '<section class="sec" id="sobre"', 1)
doc = doc.replace('<a href="#sobre" style="background:', '<a href="#especies" style="background:#14315f">Espécies</a><a href="#sobre" style="background:', 1)

# 7. rodapé com versão
doc = doc.replace('CEAC · APA do Rio Pacoti · Eusébio, Ceará</footer>', f'CEAC · APA do Rio Pacoti · Eusébio, Ceará<div class="ver">Versão {VERSAO} · atualizado em {DATA}</div></footer>')

# 8. script: busca, modo offline e instalação
idx_json = json.dumps([[n, s, k, amb, cor.get(amb, '#275db1')] for n, s, k, amb in build.SPX if not (k.endswith('-2'))], ensure_ascii=False)
JS = '''<script>
(function(){
var SP=%s;
function norm(t){return t.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}
var q=document.getElementById('q'),res=document.getElementById('res');
function show(){var v=norm(q.value.trim());if(!v){res.style.display='none';return;}
 var m=SP.filter(function(s){return norm(s[0]+' '+s[1]).indexOf(v)>-1;}).slice(0,10);
 res.innerHTML=m.length?m.map(function(s){return '<a href="#'+s[2]+'"><span>'+s[0]+'<br><i>'+s[1]+'</i></span><small style="background:'+s[4]+'">'+s[3]+'</small></a>';}).join(''):'<div class="none">Nenhuma espécie encontrada.</div>';
 res.style.display='block';}
q.addEventListener('input',show);q.addEventListener('focus',show);
res.addEventListener('click',function(e){if(e.target.closest('a')){res.style.display='none';q.value='';q.blur();}});
document.addEventListener('click',function(e){if(!e.target.closest('.find'))res.style.display='none';});
var off=document.getElementById('off'),msg=document.getElementById('offmsg');
function ready(){off.classList.add('ok');off.querySelector('.ico').textContent='\\u2713';msg.innerHTML='<b>Pronto:</b> este guia já está salvo neste celular e funciona sem internet.';}
try{if(localStorage.getItem('trilha-offline')==='%s')ready();}catch(e){}
if('serviceWorker' in navigator && location.protocol!=='file:'){
 navigator.serviceWorker.register('sw.js').then(function(){return navigator.serviceWorker.ready;}).then(function(){
  navigator.serviceWorker.addEventListener('message',function(ev){if(ev.data==='cached'){try{localStorage.setItem('trilha-offline','%s');}catch(e){}ready();}});
  if(navigator.serviceWorker.controller)navigator.serviceWorker.controller.postMessage('check');
 }).catch(function(){});
 navigator.serviceWorker.addEventListener('controllerchange',function(){if(navigator.serviceWorker.controller)navigator.serviceWorker.controller.postMessage('check');});
}
function goHash(){if(location.hash.length>1){var t=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(t)t.scrollIntoView({block:'start'});}}
window.addEventListener('load',function(){setTimeout(goHash,60);});
var dp;window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();dp=e;var b=document.getElementById('inst');b.hidden=false;b.onclick=function(){dp.prompt();};});
if(/iphone|ipad|ipod/i.test(navigator.userAgent)&&!navigator.standalone)document.getElementById('ios').hidden=false;
})();
</script>''' % (idx_json, VERSAO, VERSAO)
doc = doc.replace('</body>', JS + '</body>')

open(OUT + '/index.html', 'w').write(doc)

# 9. imagem de prévia (1200x630) para WhatsApp
from PIL import Image, ImageDraw, ImageFont
og = Image.new('RGB', (1200, 630), '#dfeeee')
ph = Image.open(ROOT + '/assets/photos/p44_5.jpg').convert('RGB')
ph = ph.resize((int(630 * ph.width / ph.height), 630)); og.paste(ph.crop((0, 0, min(520, ph.width), 630)), (680, 0))
d = ImageDraw.Draw(og)
d.polygon([(40, 210), (650, 200), (640, 300), (655, 400), (45, 410)], fill='#275db1')
fb = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf', 52)
fr = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Medium.otf', 28)
d.text((70, 225), 'Trilha Ecológica do', font=fb, fill='white'); d.text((70, 300), 'Estuário do Rio Pacoti', font=fb, fill='white')
d.text((48, 150), 'GUIA EDUCACIONAL · PEAM', font=fr, fill='#2280b8')
d.text((48, 440), 'Mata de tabuleiro, manguezal e apicum', font=fr, fill='#14315f')
lg = Image.open(ROOT + '/out/site/img/peam_horizontal.png').convert('RGBA'); lg.thumbnail((360, 90))
og.paste(lg, (48, 520), lg)
og.save(OUT + '/img/og.jpg', quality=85)

# 10. manifesto
man = {"name": "Guia da Trilha Ecológica do Rio Pacoti", "short_name": "Trilha PEAM", "lang": "pt-BR",
       "description": desc, "start_url": "./", "scope": "./", "display": "standalone",
       "background_color": "#dfeeee", "theme_color": "#275db1",
       "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                 {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                 {"src": "icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
json.dump(man, open(OUT + '/manifest.webmanifest', 'w'), ensure_ascii=False, indent=1)

# 11. service worker: guarda tudo no primeiro acesso
files = ['./', 'index.html', 'manifest.webmanifest']
for sub in ['fonts', 'icons', 'img']:
    files += [f'{sub}/{f}' for f in sorted(os.listdir(OUT + '/' + sub))]
h = hashlib.md5(open(OUT + '/index.html', 'rb').read()).hexdigest()[:8]
SW = '''const CACHE='trilha-%s-%s';
const FILES=%s;
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
 e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(r=>r||fetch(e.request).catch(()=>caches.match('index.html'))));});
self.addEventListener('message',e=>{if(e.data==='check'){caches.open(CACHE).then(c=>c.keys()).then(ks=>{if(ks.length>=FILES.length-1)e.source.postMessage('cached');});}});
''' % (VERSAO, h, json.dumps(files))
open(OUT + '/sw.js', 'w').write(SW)
open(OUT + '/.nojekyll', 'w').write('')
tot = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
print('arquivos', len(files), 'total', round(tot / 1024 / 1024, 2), 'MB')
