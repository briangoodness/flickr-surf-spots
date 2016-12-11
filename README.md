# Mapping Using Flickr Surf Spots

## App Hosted @ : http://flickr-surf-spots.herokuapp.com/

## Technology Stack:
- Python: v3.5.2
- Frontend: Bootstrap, Leaflet JS / CSS
- Web Framework: Django (relies upon Django-GeoJson)
- Database: PostgreSQL/PostGIS (Hosted on Heroku)
- App Server: Heroku
- File Server: Amazon S3

## Notes:
- In order to get GeoJSON working, I had to fix a bug in the serializers.py file of the django-geojson package's code (reference: https://github.com/makinacorpus/django-geojson/issues/80)
- On Heroku, in order to specify the Python version (3.5.2), there needs to also be a runtime.txt file in the root directory (see https://devcenter.heroku.com/articles/python-runtimes#build-behavior)
- In order for the geospatial packages to install on Heroku, a custom Python buildpack for GEO/GIS libraries-- like geos, proj and gdal-- must be added. This can be done using the instructions here: https://github.com/cyberdelia/heroku-geo-buildpack
- In order for GEOS/GDAL to be accessed properly while hosted on Heroku, it needs to be pointed to a file, and not a folder. [This page](https://github.com/cyberdelia/heroku-geo-buildpack/issues/31) shows one method that works.
- I ran into issues with buildpacks and versions on Heroku. While on the Heroku server, it could not find gunicorn, but, worked fine after uninstalling the dependencies in the requirements.txt file, and the reinstalling them. See one of the answers [here](http://stackoverflow.com/questions/33021874/heroku-gunicorn-not-working-bash-gunicorn-command-not-found).
