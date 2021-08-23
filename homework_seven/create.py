import json
dict_ = {"my_project": [{"settings": ['__init__.py', 'dev.py', 'prod.py']},
                         {"mainapp": ['__init__.py', 'models.py', 'views.py', {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
                         {"authapp": ['__init__.py', 'models.py', 'views.py', {'templates': [{'authapp': ['base.html', 'index.html']}]}]}]}

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(dict_, f, indent=4)