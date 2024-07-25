# python-api

Link de referencia: https://realpython.com/api-integration-in-python/

Instalar Lib: python -m pip install flask

Comando para listar todas a dependencias: pip freeze

Comando para rodar a aplicação: python demo_api_controller.py

# Insomnia

GET
URL -> http://127.0.0.1:5000/countries, http://127.0.0.1:5000/countries/4

POST
URL -> http://127.0.0.1:5000/countries
JSON -> {"name": "Brasil", "capital": "Brasilia", "area": 3010408}

DEL
URL -> http://127.0.0.1:5000/countries/4

PATCH
URL -> http://127.0.0.1:5000/countries/4
JSON -> {"area": 1234567}

PUT
URL -> http://127.0.0.1:5000/countries/4
JSON -> {"area": 988765433,"capital": "Brasilia","name": "Brasil"}



