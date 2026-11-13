# Como atualizar o Guia da Trilha

Este ramo (`fonte`) guarda o código e as imagens que geram o site.
O site publicado fica no ramo `main` e vai ao ar em https://peamlabomar.github.io/trilha/.

## Onde está cada coisa

- `content.py`: todo o texto do guia (seções, espécies, referências). Quase toda atualização é aqui.
- `build.py`: visual (cores, layout) e geração do PDF.
- `site.py`: gera o site instalável e offline. Mude `VERSAO` e `DATA` a cada atualização.
- `assets/photos/` e `out/web/img/`: fotos (originais e versões web).

## Passo a passo

```bash
git clone -b fonte https://github.com/peamlabomar/trilha.git guia
cd guia
git clone -b main https://github.com/peamlabomar/trilha.git out/site
# edite content.py (e VERSAO/DATA em site.py)
python3 site.py
cd out/site && git add -A && git commit -m "Atualiza o guia" && git push
cd ../.. && git add -A && git commit -m "Atualiza o conteúdo" && git push
```

Para o PDF: `python3 build.py` (precisa do Playwright; gera o PDF em `out/`).

## Observações

- O site funciona offline: quem já instalou recebe a versão nova
  na primeira ou segunda vez que abrir o guia com internet.
- Foto nova: coloque o .jpg em `out/web/img/` com o nome `pNN_N.jpg`,
  gere a versão .webp em `out/site/img/` e cite o arquivo em `content.py`.
- Pendências de conteúdo aparecem como `[[a confirmar: ...]]` em `content.py`
  e ficam em amarelo no site até serem resolvidas.
