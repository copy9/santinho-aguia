# Santinho Eletrônico

Plataforma de comunicação e mobilização política: perfil público, publicações, cortes, cabos eleitorais, cadastro de eleitores, painel eleitoral e mapa territorial.

Este repositório é uma página única (`index.html`), sem servidor e sem dependências para rodar. Basta abrir o arquivo no navegador ou publicar com o GitHub Pages.

## Demonstração

Depois de ativar o GitHub Pages, a página fica em:

`https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/`

O perfil que abre por padrão (Aurora Valença) é um personagem fictício, com foto e capa ilustradas, criado só para demonstração. Edite pelo botão **Editar perfil**.

## O que tem

- **Perfil**: capa, foto, biografia, publicações com foto e "post de campanha", cortes e materiais.
- **Cabos eleitorais**: convites únicos e árvore de cabos.
- **Eleitores**: cadastro com consentimento obrigatório (LGPD) e árvore por ordem de chegada.
- **Painel Eleitoral**: eleitorado oficial do TSE por estado, meta territorial, cobertura e eleitores por cabo.
- **Mapa**: Brasil com os 27 estados e, ao clicar em um estado, os limites dos municípios e os locais de votação (nome, endereço, seções e eleitores).
- **Central de Cabos, Engajamento, Central Demográfica e Central de Mensagens** (envio bloqueado até haver integração autorizada).

## Assistente

O botão de chat no canto da tela abre um assistente que explica qualquer parte da plataforma. Ele responde pelo manual interno (arquivo `index.html`, constante `KB`). Quando a página roda dentro do claude.ai, ele também usa o Claude para respostas mais naturais. Ele só enxerga contagens (quantos cadastros, cabos e publicações), nunca nomes, telefones ou endereços.

## Dados e fontes

| Dado | Fonte |
|---|---|
| Eleitorado por estado | TSE, cadastro eleitoral 2026 (divulgado em 20/07/2026) |
| Locais de votação (coordenadas, seções, eleitores) | TSE, "Eleitorado por local de votação 2026", 1º turno de 04/10/2026 |
| Limites de estados e municípios | IBGE, API de malhas (qualidade mínima) |
| Nomes de municípios | IBGE, API de localidades |

- 95.112 locais de votação; 94.350 têm coordenadas, e 44 foram descartados por estarem fora do estado a que pertencem.
- Os limites do IBGE estão na qualidade mínima, então as divisas aparecem simplificadas em zoom alto.
- O município Boa Esperança do Norte (MT) não existe na malha do IBGE usada.

## Privacidade

Os cadastros de eleitores, publicações e demais dados digitados ficam **somente no navegador** de quem usa (`localStorage`). Nada é enviado a servidor. O repositório contém apenas dados públicos do TSE e do IBGE.

## Como rodar

Abra `index.html` no navegador. Para publicar: **Settings > Pages > Deploy from a branch > main / (root)**.

## Como atualizar os dados

Os scripts em `scripts/` foram usados para gerar os dados embutidos no `index.html`. Eles esperam os CSVs do TSE (um por estado) e os arquivos do IBGE (`BR`, `BR__1_`, `municipios.json`) e têm caminhos fixos que precisam ser ajustados. Veja os comentários no início de cada arquivo.

## Licença

Defina a licença do código antes de tornar o repositório público. Os dados do TSE e do IBGE têm as condições de uso dos respectivos portais.
