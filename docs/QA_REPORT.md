# QA · Casa da Macaxeira

Data: 07/10/2026. Navegador integrado do Codex; desktop e viewports de teste explícitos. Todas as verificações abaixo foram executadas, salvo as marcadas como pendentes.

## Status

- Integridade estática: **PASS**, 57 referências verificadas; JavaScript com sintaxe válida.
- Local: **PASS** em 320, 390, 768 e 1440 pixels.
- Publicação: **PASS**, GitHub Pages, HTTPS, branch `main`, raiz do repositório.
- URL pública: [Casa da Macaxeira](https://gabi0102souza-stack.github.io/casa-da-macaxeira-preview/).
- Repositório: [casa-da-macaxeira-preview](https://github.com/gabi0102souza-stack/casa-da-macaxeira-preview).

## Escopo

| Viewport local | Resultado |
|---|---|
| 320 × 740 | Sem overflow; barra móvel com texto em duas linhas onde necessário; controles com ao menos 44px de altura |
| 390 × 844 | Sem overflow; endereço/horário e CTAs acessíveis; menu abre, Escape fecha e devolve focus ao botão |
| 768 × 1024 | Sem overflow; cabeçalho completo e composição em duas colunas |
| 1440 × 960 | Sem overflow; hero, cardápio, ambiente, visita e rodapé verificados |

O navegador de teste apresenta scrollbar de 15px, portanto as larguras úteis foram 305, 375, 753 e 1425px. Isso não foi tratado como overflow: `scrollWidth` igual a `clientWidth` em todas as larguras. O breakpoint real móvel é 760px.

## Interações e acessibilidade

- Menu móvel: abre/fecha; `aria-expanded` acompanha o estado; Escape fecha e retorna focus.
- Link da barra “Endereço & horário”: chega a `#visite` e carrega a fachada.
- Âncoras do cabeçalho: cardápio, ambiente e visita navegam corretamente.
- Details de cuscuz/escondidinhos: expansão real, compatível com controles nativos; sem dependência de JavaScript.
- Teclado: Shift+Tab a partir da marca alcança “Pular para o conteúdo”, visível e com contorno de focus.
- Um H1 por página, `lang=pt-BR`, alt em todas as imagens. Logos duplicados usam alt vazio dentro de links com nome acessível.
- Imagens de conteúdo carregam ao percorrer a página; fontes Fraunces e DM Sans carregadas localmente.
- Texto principal 16px; barra móvel 14px; informações secundárias mínimas de 12px.
- Contraste em cores sólidas: texto principal/papel 9,71:1; branco/bordô 7,58:1; branco/verde 8,64:1; texto claro/bordô 5,94:1. O texto secundário foi escurecido após medir contraste insuficiente na primeira versão; contraste final acima de 4,5:1.
- `prefers-reduced-motion` desliga scroll suave e transições. Confirmado no CSS; preferência do sistema não foi alterada nos testes.
- Sem erros ou avisos de console relacionados à prévia final.

Esta é uma verificação prática e de código, não uma certificação WCAG completa. Não foram usados leitor de tela, auditoria axe, Lighthouse nem emulação de rede lenta; não se inventa nota desses serviços. Ampliação de texto a 200% não foi manualmente testada.

## Destinos e precisão

WhatsApp em todos os CTAs: **5582987533631**, mensagens de consulta codificadas, sem envio automático. Maps, Instagram e Linktree foram abertos na pesquisa e correspondem ao restaurante correto. `tel:+5582987533631` e `mailto:casadamacaxeira84@gmail.com` conferidos no DOM. Tel/mailto não acionados para evitar abrir um contato real.

`noindex, nofollow` presente nas duas páginas; `robots.txt` bloqueia indexação; declaração de conceito independente no rodapé e créditos. Sem preços, pratos inventados, narrativa de inauguração, reserva confirmada, música ou área infantil não comprovadas. Imagem do hero não rotulada como macaxeira; fotos antigas identificadas como acervo.

## Performance observada

JavaScript de produção: **900 bytes**, sem bibliotecas. Nenhum widget, iframe de mapa, analytics ou request externo necessário à renderização. Fontes locais WOFF2; imagens locais WebP, `srcset`, `sizes`, dimensões declaradas, hero prioritário e demais imagens lazy.

Payload de arquivos para a **página inteira**, somando variantes escolhidas, HTML/CSS/JS/fontes/favicon, sem compressão HTTP: aproximadamente **421 KiB em mobile** e **610 KiB em desktop**. É soma de bytes estáticos, não medição de tempo, Core Web Vitals ou de transferência em rede real. O navegador pode carregar imagens lazy antecipadamente conforme suas próprias heurísticas.

## Evidências locais

- [Desktop 1440](qa/local-desktop-1440.jpg), [página completa](qa/local-desktop-full.jpg).
- [Mobile 390](qa/local-mobile-390.jpg), [mobile 320](qa/local-mobile-320.jpg), [mobile completo](qa/local-mobile-full.jpg).
- [Tablet 768](qa/local-tablet-768.jpg).
- [Auditoria do DOM](qa/local-audit.json): destinos, imagens, fontes e noindex.

## Verificação pública

**PASS** em 320 × 740, 390 × 844, 768 × 1024 e 1440 × 960. A URL pública foi aberta no navegador, com imagens e fontes carregadas, sem overflow horizontal em nenhuma dessas larguras. O desktop e o mobile foram conferidos visualmente.

- As âncoras de cardápio, ambiente e endereço funcionaram no site publicado.
- Menu móvel abriu; Escape fechou e devolveu focus. O details de cuscuz/escondidinhos expandiu os itens esperados.
- A página de créditos abriu pelo rodapé e voltou corretamente para a proposta.
- O CTA de pedido abriu a página pública do WhatsApp com **+55 82 98753-3631** e a mensagem de consulta esperada. Não se abriu a conversa nem se enviou mensagem.
- **21 arquivos de produção** responderam com HTTP 200 e conteúdo correspondente à cópia local: HTML, créditos, robots, CSS, JS, fotos, variantes, fontes e licenças. Normalização CRLF/LF foi tolerada somente em texto; hashes da resposta estão registrados. Todos os srcsets foram verificados, inclusive variantes não escolhidas no viewport.
- Nenhum erro/aviso de console associado ao domínio do site. `noindex, nofollow` confirmado no DOM público.
- Primeiro deploy: [workflow concluído com sucesso](https://github.com/gabi0102souza-stack/casa-da-macaxeira-preview/actions/runs/37658155111), código `0d133e0`. O commit posterior acrescenta relatório, evidências e script de QA, sem alterar HTML/CSS/JS/imagens.

Evidências: [desktop 1440](qa/public-desktop-1440.jpg), [desktop completo](qa/public-desktop-full.jpg), [mobile 390](qa/public-mobile-390.jpg), [tela 320](qa/public-320.jpg), [tablet 768](qa/public-768.jpg), [DOM e interações](qa/public-audit.json), [respostas HTTPS e hashes](qa/public-http.json).

Nenhum pedido, reserva ou mensagem foi enviado nos testes. Tel/mailto foram verificados como destinos; não se executou contato com a empresa. As limitações de auditoria de acessibilidade e performance descritas acima também se aplicam ao QA público.
