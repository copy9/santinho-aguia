# Santinho Eletrônico

Plataforma de comunicação e mobilização política: perfil público, publicações, cortes, cabos eleitorais, cadastro de eleitores, painel eleitoral e mapa territorial.

Este repositório é uma página única (`index.html`), sem servidor e sem dependências para rodar. Basta abrir o arquivo no navegador ou publicar com o GitHub Pages.

## Demonstração

Depois de ativar o GitHub Pages, a página fica em:

`https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/`

O perfil que abre por padrão (Aurora Valença) é um personagem fictício, com foto e capa ilustradas, criado só para demonstração. Edite pelo botão **Editar perfil**.

## O que tem

- **Login**: contas locais, recuperação de senha por código e modo demonstração.
- **Perfil**: capa, foto, biografia, publicações com foto e "post de campanha", cortes e materiais.
- **Cabos eleitorais**: convites únicos, árvore de cabos e remoção.
- **Eleitores**: cadastro com consentimento obrigatório (LGPD), campos sensíveis opcionais, exclusão de cadastro e árvore por ordem de chegada.
- **Painel Eleitoral**: eleitorado oficial do TSE por estado, meta territorial, cobertura e eleitores por cabo.
- **Mapa**: Brasil com os 27 estados e, por estado, os limites dos municípios e os locais de votação.
- **Central de Cabos**, **Engajamento** (ranking de cabos e atividade), **Métricas de Indicação** (origem, dias e horários), **Central Demográfica** e **Base TSE** (tabela por estado, busca e CSV).
- **Central de Mensagens**: envio manual, um contato por vez, abrindo o WhatsApp com a mensagem pronta.
- **Dados**: backup (.json), importação, eleitores em .csv e apagar tudo.
- **Assistente** de ajuda com manual interno.

## Login

A página abre na tela de login: entrar com e-mail e senha, criar conta ou ver a demonstração. Ao criar a conta é gerado um **código de recuperação**, a única forma de redefinir a senha (não há envio de e-mail). Após 5 tentativas erradas o login trava por 1 minuto.

**Importante:** não há servidor. As contas e os dados ficam só no navegador do aparelho (`localStorage`), e cada conta tem seus próprios dados. As senhas são guardadas com PBKDF2-SHA256 e sal aleatório, mas a proteção vale apenas contra quem usa aquele navegador: quem tem acesso técnico ao arquivo ou ao navegador consegue ler o conteúdo. Para proteger dados de verdade, entre vários usuários e aparelhos, é necessário um servidor com autenticação (próximo passo do projeto).

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
