# mip-dr-app
Prototype django MIP Data Request app and tools

## Setting up the app

Clone the repo:

```
git clone https://github.com/cedadev/mip-dr-app
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
django-admin makemigrations mip_dr_app_api
django-admin migrate

python generate_import_data_script.py
python import_data.py
```

## Create an Admin User Account

```
python manage.py createsuperuser
```

Then follow the on screen prompts and enter the required details

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

## Importing Data

It is possible to update the data by importing a file:
- Go to the admin page, e.g. `http://localhost:8888/admin/` and login with your admin credentials  
- Select the required table to upload data to
- Press the `IMPORT` button near the top right of the page
- Choose a file to import and press the `SUBMIT` button
- Check the data in the preview panel is correct
- Press the `CONFIRM IMPORT` button

The file to be uploaded must be in one of the following formats:
- csv
- xls
- xlsx
- tsv
- json
- ymal
