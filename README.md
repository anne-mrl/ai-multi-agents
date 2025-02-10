# AI mutli-agents assistant
Application Python qui simule une interaction entre un utilisateur et un
système de support technique composé de trois agents d’IA collaboratifs.

L'utilisateur interroge l'agent principal depuis l'interface web, qui lui-même interroge dans un premier temps un agent spécialisé connecté à une base de connaissances FAISS (Agent FAISS). Si l'Agent FAISS est dans l'incapacité de trouver une réponse appropriée, alors l'agent principal interroge le troisième agent qui réalise une requête ChatGPT-4o (Agent GPT4-o).

Quelque soit l'agent qui répond, Agent FAISS ou Agent GPT-4o, l'informatoin est remontée à l'agent principal qui la restitue à l'utilisateur dans l'interface web.


## Installation

#### Pré-requis
Version de Python 3.10 utilisée pour le développement :  https://www.python.org/downloads/

#### Etapes
1. Cloner le repo
````commandline
git clone
````

2. Créer un fichier `.env` à la racine du projet `<path>/ai-multi-agents/` contenant votre clef API openai
````commandline
# .env content
OPENAI_API_KEY=<your-openai-api-key>
````

3. Environnement virtuel et installation des dépendances
````commandline
cd <path>/ai-multi-agents/
python -m venv venv
venv\Scripts\activate     # for Windows
source venv/bin/activate  # for Linux
python -m pip install --upgrade pip
pip install -r requirements.txt
````

4. Lancer l'applicaton
````commandline
python main.py
````
Vous devriez voir ceci dans votre terminal :
````commandline
←[32mINFO←[0m:     Started server process [←[36m8164←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://0.0.0.0:5000←[0m (Press CTRL+C to quit)

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://<ip>:8501

````
Une fenêtre de votre navigateur s'ouvre automatiquement, vous n'avez plus qu'à poser vos questions à l'assistant !
