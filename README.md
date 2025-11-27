
# PDF Inserter App

Pequena aplicação Flask para inserir páginas em um PDF:

- Insere todas as páginas de um PDF (5 páginas) após a **primeira página** do PDF original.
- Insere todas as páginas de outro PDF (2 páginas) após a **última página** do PDF original.

## Requisitos

- Python 3.9+
- Pip

## Como rodar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Linux/macOS
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python app.py
```

4. Abra no navegador:

Acesse `http://127.0.0.1:5000` (ou o endereço mostrado no terminal).

5. Uso:

- Envie o **PDF original**.
- Envie o **PDF com as 5 páginas** (conteúdo que será inserido após a primeira página).
- Envie o **PDF com as 2 páginas** (conteúdo que será inserido após a última página).
- Clique em **"Gerar PDF modificado"** e o download será iniciado automaticamente.
