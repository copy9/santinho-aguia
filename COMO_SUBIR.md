# Como subir no GitHub e criar a página para visualizar

## 1. Criar o repositório
1. Entre em https://github.com/new
2. Em **Repository name**, escreva um nome novo, por exemplo `santinho-eletronico-v2`.
3. Escolha **Public** (para a página abrir para qualquer pessoa) e clique em **Create repository**.

## 2. Enviar os arquivos
1. Na página do repositório novo, clique em **uploading an existing file**.
2. Arraste para lá **o conteúdo desta pasta**: `index.html`, `README.md` e a pasta `scripts`.
   O arquivo `.gitignore` é opcional (alguns computadores escondem arquivos que começam com ponto).
3. Clique em **Commit changes**.

## 3. Criar a página para visualizar
1. No repositório, abra **Settings** e, no menu da esquerda, **Pages**.
2. Em **Build and deployment**, deixe **Source** como **Deploy from a branch**.
3. Em **Branch**, escolha **main** e a pasta **/ (root)**, e clique em **Save**.
4. Espere de 1 a 2 minutos e recarregue. O endereço aparece no topo da página:
   `https://SEU_USUARIO.github.io/santinho-eletronico-v2/`

## Observações
- A primeira abertura da página é mais lenta, porque o arquivo tem cerca de 6 MB.
- Os cadastros digitados ficam só no navegador de quem usa. Nada vai para o GitHub.
- Repositório privado só publica a página em plano pago do GitHub.
