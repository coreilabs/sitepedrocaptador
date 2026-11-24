"""Aplica a identidade aprovada; também usado após regenerar o site."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SLOGAN = 'Cuidando de vidas, restaurando sonhos'
COLORS = {
    '#166534': '#006b80', '#064e27': '#004563', '#f0f7f1': '#edf9fa',
    '#f7faf7': '#f5fbfc', '#c0ec79': '#7ce4e6', '#f2f9e8': '#e5fafa',
    '#58675c': '#506b78', '#d6e5d8': '#cce5eb', '#f5faf3': '#f2fbfc',
    '#eef8f5': '#edf9fa', '#ccece0': '#cce5eb',
}


def apply_identity():
    path = ROOT / 'assets/style.css'
    css = path.read_text(encoding='utf-8')
    for old, new in COLORS.items():
        css = css.replace(old, new)
    for old, new in [('6, 78, 39', '0, 69, 99'), ('22, 101, 52', '0, 107, 128'),
                     ('192, 236, 121', '124, 228, 230'), ('6, 60, 30', '0, 61, 87'),
                     ('6, 50, 25', '0, 51, 76')]:
        css = css.replace(old, new)
    path.write_text(css, encoding='utf-8')
    for name in ['index.html', 'politica-de-privacidade.html']:
        path = ROOT / name
        html = path.read_text(encoding='utf-8').replace('content="#166534"', 'content="#006b80"')
        if 'class="brand-slogan"' not in html:
            html = html.replace('<p class="hero-lead">', '<p class="brand-slogan">' + SLOGAN + '</p>\n<p class="hero-lead">')
        if 'class="footer-slogan"' not in html:
            html = re.sub(r'(<div class="footer-brands">.*?</div>)', r'\1<p class="footer-slogan">' + SLOGAN + '</p>', html)
        if name == 'index.html':
            html = html.replace('Vida Nova Tratamentos — Acolhimento e Bem-estar em Goiás', 'Vida Nova Tratamentos — ' + SLOGAN)
        def whatsapp_button(match):
            anchor = match[0]
            if 'wa.me/' not in anchor or 'class=' not in anchor:
                return anchor
            return re.sub(r'<i data-lucide="[^"]+"></i>', '<img class="contact-whatsapp-icon" src="assets/whatsapp.webp" alt="" width="24" height="24"/>', anchor, count=1)
        html = re.sub(r'<a\b[^>]*>.*?</a>', whatsapp_button, html, flags=re.S)
        path.write_text(html, encoding='utf-8')


if __name__ == '__main__':
    apply_identity()
