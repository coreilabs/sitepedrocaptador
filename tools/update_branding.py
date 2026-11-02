from pathlib import Path
import json, re, shutil, sys

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://coreilabs.github.io/sitepedrocaptador'
REPLACEMENTS = {
    'https://clinicadependenciaquimica.net.br': BASE,
    'clinicadependenciaquimica.net.br': 'coreilabs.github.io/sitepedrocaptador',
    'Clínica de Dependência Química': 'Cardoso Tratamentos',
    'Dependência Química e Alcoolismo em Goiás': 'Acolhimento e Bem-estar em Goiás',
    'dependência química e alcoolismo': 'acolhimento e bem-estar',
    'dependência química ou alcoolismo': 'acolhimento e bem-estar',
    'dependência química e ao alcoolismo': 'bem-estar e à qualidade de vida',
    'nove clínicas': 'nove unidades',
    'promoção da recuperação': 'promoção do bem-estar',
    'a recuperação envolve': 'o cuidado envolve',
    'processo de recuperação': 'processo de cuidado',
    'rotina terapêutica': 'rotina de cuidado',
    'pacientes, familiares': 'pessoas atendidas, familiares',
    'etapas do tratamento': 'etapas do acompanhamento',
    'durante o tratamento': 'durante o acompanhamento',
    'compreender o tratamento': 'compreender o acompanhamento',
    'Acolhimento e Bem-estar em Goiás | Acolhimento': 'Cardoso Tratamentos | Acolhimento e Bem-estar em Goiás',
    'Acolhimento para Acolhimento e Bem-estar em Goiás': 'Cardoso Tratamentos — Acolhimento e Bem-estar em Goiás',
    'Acolhimento e orientação para acolhimento e bem-estar': 'Acolhimento, orientação e apoio ao bem-estar',
    'Acolhimento para acolhimento e bem-estar': 'Acolhimento, orientação e bem-estar',
    'Apoio para acolhimento e bem-estar': 'Apoio para você e sua família',
    'ajuda com acolhimento e bem-estar': 'apoio e qualidade de vida',
    'acompanhamento para acolhimento e bem-estar': 'acompanhamento e apoio ao bem-estar',
    'Busca ajuda para acolhimento e bem-estar?': 'Busca acolhimento e orientação?',
    'Dúvidas sobre acolhimento, acolhimento e bem-estar': 'Dúvidas sobre acolhimento e orientação',
    'cuidado para acolhimento e bem-estar': 'cuidado e apoio ao bem-estar',
    'site de acolhimento para acolhimento e bem-estar': 'site de acolhimento e orientação',
}

def revise(text):
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text

if __name__ == '__main__':
    source = Path('C:/Users/user/Documents/cardosotratamentos')
    for original, targets in {
        'favicon_icon.webp': ['assets/favicon.webp'],
        'logotipo_cardoso_tratamentos_horizontal.webp': ['assets/logotipo-horizontal.webp'],
        'logotipo_cardoso_tratamentos_vertical.webp': ['assets/logotipo-vertical.webp'],
        'opengraph_cardoso_tratamentos.webp': ['assets/og.webp'],
    }.items():
        for target in targets:
            if '--local' not in sys.argv:
                shutil.copy2(source / original, ROOT / target)
    for name in ['index.html', 'politica-de-privacidade.html', 'robots.txt', 'sitemap.xml', 'assets/js/main.js', 'tools/validate.cjs']:
        path = ROOT / name
        text = revise(path.read_text(encoding='utf-8'))
        if name.endswith('.html'):
            text = re.sub(r'<div class="footer-brands">.*?</div></div>', '<div class="footer-brands"><img class="footer-group-logo" alt="Cardoso Tratamentos" src="assets/logotipo-vertical.webp" loading="lazy"/></div>', text)
            text = text.replace('rel="noopener"', 'rel="noopener noreferrer"')
            text = re.sub(r'(assets/(?:logotipo-horizontal|logotipo-vertical|grupo-araujo-vertical|favicon|og)\.webp)(?!\?)', r'\1?v=20261102', text)
        path.write_text(text, encoding='utf-8')
    path = ROOT / 'assets/js/units.js'
    config = json.loads(path.read_text(encoding='utf-8').removeprefix('window.GAT_CONFIG = ').strip().removesuffix(';'))
    for unit in config['unidades']:
        unit['descricao'] = f"Unidade em {unit['cidade']} - {unit['estado']}. Acolhimento e acompanhamento individualizado. Consulte nossa equipe sobre estrutura, condições e disponibilidade."
    path.write_text('window.GAT_CONFIG = ' + json.dumps(config, ensure_ascii=False) + ';\n', encoding='utf-8')
    (ROOT / 'CNAME').unlink(missing_ok=True)
