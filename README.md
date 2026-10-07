# Casa da Macaxeira · proposta de website

Conceito independente de apresentação para a Casa da Macaxeira, Praça 13 de Maio, 84, Poço, Maceió, AL. Não representa contratação ou aprovação da marca.

Site estático com HTML semântico, CSS responsivo e JavaScript mínimo. Fotos reais; sem imagens geradas, preços inventados ou formulário simulado. Pesquisa e decisão GO concluídas antes do desenvolvimento.

## Publicação

- URL pública: [Abrir o site](https://gabi0102souza-stack.github.io/casa-da-macaxeira-preview/)
- Repositório: [casa-da-macaxeira-preview](https://github.com/gabi0102souza-stack/casa-da-macaxeira-preview)
- Branch: `main`
- GitHub Pages: diretório raiz da branch.
- Status: **publicado via HTTPS**, com QA local e público concluídos em 07/10/2026. [QA_REPORT](docs/QA_REPORT.md).

## Abrir localmente

Na pasta do projeto, execute `python -m http.server 4178 --bind 127.0.0.1` e abra `http://127.0.0.1:4178/`. Não há etapa de build nem dependências de produção.

Verificações de integridade: `python scripts/check_site.py` e `node --check assets/js/site.js`. Após deploy, `python scripts/check_public.py` verifica respostas HTTPS e compara os 21 arquivos de produção com a cópia local, tolerando apenas normalização de quebras de linha em texto.

## Estrutura

- `index.html`: experiência principal.
- `creditos.html`: origem e limites das informações e imagens.
- `assets/css/site.css`, `assets/js/site.js`: apresentação e menu móvel.
- `assets/images/`: WebP e favicon; arquivos locais sem metadados de câmera.
- `assets/fonts/`: WOFF2 e licenças.
- `docs/evidence/`: evidências públicas selecionadas da pesquisa, sem dados de sessão.
- `scripts/prepare_assets.py`: reprodução da conversão, a partir dos originais de pesquisa não versionados.

## Documentação

- [Pesquisa](docs/RESEARCH.md): VERIFIED, INFERENCE e NEEDS OWNER CONFIRMATION.
- [Origem dos assets](docs/ASSET_SOURCES.md): fontes, datas, transformações e direitos.
- [QA](docs/QA_REPORT.md): resultados reais e limitações dos testes.
- [Direção criativa](CREATIVE_DIRECTION.md).
- [Estratégia](SITE_STRATEGY.md).
- [Autocrítica](SELF_CRITIQUE.md).

## Atualização antes de uso oficial

Confirmar cardápio/preços, feriados, regras de entrega/reserva, história, disponibilidade do e-mail e direitos da marca/fotos. Fotos do ambiente são acervo de 2023; prato clássico, de 2017. Nenhuma alegação de operação contínua desde 2014 foi publicada. As fontes não confirmaram música ao vivo ou área infantil atuais.

`noindex, nofollow` e `robots.txt` são orientações para indexadores, não controle de acesso. A proposta é pública e usa somente informações públicas do negócio. Imagens e logo pertencem aos respectivos titulares; não há licença geral sobre esses assets.
