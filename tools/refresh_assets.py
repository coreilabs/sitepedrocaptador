"""Renova as URLs de publicação e mantém os metadados da marca."""
from pathlib import Path
import re
import secrets

ROOT = Path(__file__).resolve().parent.parent


def refresh_assets():
    versions = {}
    for name in ['index.html', 'politica-de-privacidade.html']:
        path = ROOT / name
        text = path.read_text(encoding='utf-8')

        def version(match):
            asset = match.group(1)
            token = versions.setdefault(asset, secrets.token_hex(6))
            return asset + '?v=' + token

        text = re.sub(r'(assets/[^\s"<>?]+\.(?:css|js|webp))(?:\?v=[a-zA-Z0-9]+)?', version, text)
        title = 'Privacidade | Vida Nova Tratamentos' if name.startswith('politica') else 'Vida Nova Tratamentos | Acolhimento em Goiás'
        description = 'Saiba como seus dados são usados no site e no contato com nossa equipe.' if name.startswith('politica') else 'Tratamento, acolhimento e orientação em todo o Brasil. Fale com nossa equipe 24 horas.'
        for key, value in [('og:title', title), ('og:description', description), ('twitter:description', description)]:
            text = re.sub(r'(<meta (?:property|name)="' + re.escape(key) + r'" content=")[^"]*(">)', lambda m: m[1] + value + m[2], text)
        for key, value in [('twitter:title', title), ('twitter:image', 'https://vidanovatratamentogo.com.br/assets/og.webp?v=' + versions['assets/og.webp'])]:
            tag = '<meta name="' + key + '" content="' + value + '">'
            pattern = r'<meta name="' + key + r'" content="[^"]*">'
            text = re.sub(pattern, lambda m: tag, text) if re.search(pattern, text) else text.replace('</head>', tag + '</head>')
        path.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    refresh_assets()
