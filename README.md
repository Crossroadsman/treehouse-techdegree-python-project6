treehouse-techdegree-python-project6
====================================

Installation
------------
See [requirements.txt][link01] in the [mineral_catalog][link02] project folder for the listing of required packages for Pip


Usage
-----
- The catalog app can be run using `manage.py runserver <ip>:<port>`
- Tests can be run using `manage.py test`. Detailed HTML test reports will be generated and saved in the [cover][link03] subdirectory
- The script for populating the database is in the [scripts][link04] subdirectory. You can see it in action by:
  - deleting the sqlite database (`db.sqlite3`);
  - creating a new empty database with relevant migrations (`python3 manage.py migrate`); then
  - repopulate the DB by running `python3 scripts/populate_database.py`.



[link01]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/blob/master/mineral_catalog/requirements.txt
[link02]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog
[link03]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/cover
[link04]: https://github.com/Crossroadsman/treehouse-techdegree-python-project6/tree/master/mineral_catalog/scripts
