
# Blog API – FastAPI + SQLite

Ce projet est une API backend simple développée avec **FastAPI** et **SQLite**.  
Elle permet de gérer des articles de blog (CRUD : Create, Read, Update, Delete) avec documentation interactive via **Swagger UI**.


* Installation

   1. Cloner le projet
```bash
git clone https://github.com/ton-compte/blog_api.git
cd blog_api
```

 2. Créer un environnement virtuel dans le terminal 

  python -m venv venv

3. Activer l’environnement dans le terminal
   
- **Windows (PowerShell)** :
  
 venv\Scripts\Activate.ps1

- **Linux / MacOS** :
  
source venv/bin/activate


 4. Installer les dépendances

pip install fastapi[standard] uvicorn sqlalchemy pydantic


* Lancer le serveur

uvicorn blog_api.main:app --reload


Le serveur démarre sur :  
 [http://127.0.0.1:8000](http://127.0.0.1:8000)  
 Documentation Swagger : `http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")  
 Documentation ReDoc : `http://127.0.0.1:8000/redoc` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fredoc")  



 Endpoints disponibles
 ---------------------

* Créer un article
  
  POST /api/articles


* Lire tous les articles

   GET /api/articles

* Lire un article par ID
  
  GET /api/articles/{id}


* Modifier un article

   PUT /api/articles/{id}



*Supprimer un article

DELETE /api/articles/{id}


* Rechercher un article

GET /api/articles/search?query=texte



 Bonnes pratiques appliquées
- Validation des entrées avec **Pydantic**.  
- Codes HTTP corrects (`200`, `201`, `400`, `404`, `500`).  
- Documentation automatique avec **Swagger UI**.  
- Séparation claire entre **models**, **schemas**, **database**, et **main**.  








Veux-tu que je génère aussi un **exemple de test avec `curl` ou `httpie`** pour que tu puisses montrer dans ton rapport comment tu as vérifié tes endpoints ?
