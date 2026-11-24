# Atualização da identidade — Vida Nova Tratamentos

Texto para encaminhar ao responsável pelo tema WordPress:

> Atualize a identidade visual do tema Vida Nova Tratamentos usando o site estático desta pasta como referência aprovada. O slogan é “Cuidando de vidas, restaurando sonhos”. Aplique a identidade em todos os templates do tema, incluindo início, páginas internas, unidades, arquivos, busca, erro 404 e política de privacidade, conforme existirem. Preserve conteúdo, fotos das unidades, contatos, formulários e funcionalidades.

## Artes aprovadas

Os arquivos abaixo estão na pasta `assets/` do site atualizado. Use os arquivos integralmente, mantendo proporções, transparência e cores originais:

- `logotipo-horizontal.webp`: cabeçalho e abertura desktop.
- `logotipo-vertical.webp`: abertura mobile e rodapé.
- `favicon.webp`: ícone do site. Se o painel exigir outro formato ou tamanho, gere a versão necessária a partir deste original, sem deformar.
- `og.webp`: imagem de compartilhamento, 1200 × 630 px.
- `whatsapp.webp`: ícone original dos botões de WhatsApp, exibido a 24 × 24 px.

Substitua também logos configurados no Personalizador, opções do tema e metadados de plugins de SEO, se existirem. Evite metadados duplicados entre tema e plugin.

## Paleta e aplicação

| Uso | Cor |
| --- | --- |
| Cor principal | `#006b80` |
| Azul profundo, títulos e slogan | `#004563` |
| Turquesa claro, destaques | `#7ce4e6` |
| Fundo suave | `#edf9fa` |
| Fundo alternado | `#f5fbfc` |
| Destaque suave | `#e5fafa` |
| Texto secundário | `#506b78` |
| Bordas | `#cce5eb` |
| Base | `#ffffff` |

Use `assets/style.css` e `assets/static.css` como referência de aplicação. Troque também as cores fixas antigas, sombras, gradientes, sobreposições de fotos, estados hover/foco, campos, filtros, cartões e navegação mobile. O verde anterior da marca deve sair; o verde dos botões WhatsApp deve permanecer por identificar o serviço (`#128c4a`, hover `#0d703a`, texto branco).

Coloque o slogan em texto visível após o logotipo na abertura e no rodapé. Mantenha contraste, leitura e quebra natural em telas pequenas. Preserve as fotos das unidades e seus vínculos.

Os botões WhatsApp devem usar o ícone original pequeno, alvo de pelo menos 48 px e detalhe de balão. Preserve os números existentes e a normalização centralizada do projeto, sem alterar telefones exibidos ou gerar envios durante os testes.

## Compartilhamento e cache

- Na página inicial, use `og:title` e `twitter:title`: **Vida Nova Tratamentos**.
- Use `og:description` e `twitter:description`: **Cuidando de vidas, restaurando sonhos. Acolhimento e orientação para você e sua família.**
- Nas páginas internas, mantenha metadados específicos e naturais, visando até 50 caracteres no título e 90 na descrição. Esses valores são critérios editoriais; a exibição do WhatsApp pode variar.
- Use a URL pública absoluta da nova imagem em `og:image`, `og:image:secure_url` se existir e `twitter:image`, com o mesmo token hexadecimal aleatório novo. Preserve formato WebP, largura 1200 e altura 630 quando esses metadados estiverem presentes. Não altere canonical ou URL das páginas por causa da identidade.
- Gere uma nova versão hexadecimal aleatória para cada CSS/JS alterado, uma vez na preparação da publicação. Use o helper existente do tema e o parâmetro de versão de `wp_enqueue_style`/`wp_enqueue_script`; não gere valores aleatórios por visitante. Se houver bundler, use o mecanismo de release/manifest suportado.
- Publique imagens, CSS/JS e templates com suas referências novas juntos. Limpe os caches aplicáveis e solicite nova leitura pelo depurador de compartilhamento da plataforma quando necessário. Não prometa atualização imediata de prévias antigas do WhatsApp.

## Execução e validação

1. Identifique o tema realmente ativo, tema filho, campos e opções usados. Faça backup dos arquivos e dos dados relevantes antes de alterar. Não substitua arquivos PHP por HTML do site estático.
2. Caso seja solicitado usar o WordPress de testes, reutilize `C:/laragon/www/ctwp` em `http://cardoso.localhost/`. Confira a configuração privada sem expor credenciais e preserve o banco selecionado e os outros projetos. Inspecione junctions antes de editar o diretório do tema.
3. Aplique as alterações nos templates, assets e configurações apropriados. Verifique se uma regeneração/build mantém a nova identidade.
4. Valide no Google Chrome via Playwright em desktop e celular: cabeçalho, slogan, rodapé, menus, páginas internas, logos sem deformação, contraste, botões e ícones pequenos, formulários sem envio real, erros de console e URLs dos recursos.
5. Verifique favicon, metadados renderizados e imagem social acessível. Teste com rastreamento e ações externas reais bloqueados no ambiente local.
6. Entregue os arquivos e o relatório de validação. A publicação em produção deve seguir o escopo autorizado para o projeto WordPress.

Este trabalho alterou apenas o site estático em `C:/laragon/www/sitepedrocaptador`. O tema WordPress e a produção não foram alterados.
