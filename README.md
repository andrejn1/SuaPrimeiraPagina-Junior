# SuaPrimeiraPagina+Junior


## Como rodar:

```bash
git clone https://github.com/andrejn1/SuaPrimeiraPagina-Junior.git
cd SuaPrimeiraPagina-Junior
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Funcionalidades:

- `/criar_autor/` — cadastrar autor
- `/criar_categoria/` — cadastrar categoria
- `/criar_post/` — criar post
- `/buscar/` — buscar post por título

Pronto! Projeto básico completo com padrão MVT.
