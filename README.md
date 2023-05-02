# LearnItAll
a minimal e-learning platform written in python/django.

#### Features
- Generic content support for Text, HTML, Files, Images, Videos and other types can be added easily.
- Caching support using [memcache](https://memcached.org/) and [pipenv](https://pipenv.pypa.io/en/latest/)
- CMS for Instructors to easily CRUD their courses and contents.
- Minimal nice UI.

### Getting Started
1. Install [memcache](https://memcached.org/) and [pipenv](https://pipenv.pypa.io/en/latest/)
2. start by clonning this repo
```
git clone https://github.com/BishrGhalil/learnitall.git
cd learnitall
```
3. installing required packages
```
pipenv install
```
4. in a different terminal run the memcache demon
```
memcached -l 127.0.0.1:11211
```
5. start the development server
```
pipenv shell
python manage.py migrate
python manage.py runserver
```
