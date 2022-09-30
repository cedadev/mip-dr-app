# mip-dr-app
Prototype django MIP Data Request app and tools

## Setting up the app

Clone the repo:

```
git clone https://github.com/agstephens/mip-dr-app
cd mip-dr-app/
```

Install the requirements:

```
pip install -r requirements.txt
```

Set environment variable(s):

```
export PYTHONPATH=$PWD/.
export DJANGO_SETTINGS_MODULE=mip_dr_app.settings
```

## Populating the contents from the Data Request XML

```
cd scripts/
python generate_views_and_templates.py
python generate_models_from_xml.py

django-admin makemigrations mip_dr_app_api
django-admin migrate

python generate_import_data_script.py
python import_data.py
```

## Running the server

```
django-admin runserver localhost:8888
# Or: 0.0.0.0:8888 (if running on a private network on a vagrant VM)
```

View at: http://localhost:8888

E.g.:

```
$ curl http://localhost:8888
```


