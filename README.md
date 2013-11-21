Django version for Site Vins


===
installation
git clone https://github.com/quantumlicht/django-wine.git
create virtual env
source </path/to/venv>/bin/activate
pip install -r requirements.txt
cd django-wine/project
python manage.py migrate corewine --settings=project.settings.dev
python manage.py loaddata data.json --settings=project.settings.dev
djangoadmin.py compilemessages

===
Execution
	
- cd project && python manage.py runserver --settings=project.settings.<environment>
* Environment can be dev or test


=== 
Run tests

coverage run manage.py test --settings=project.settings.test
coverage html --include="$SITE_URL*" --omit="admin.py,*/site-packages/*"