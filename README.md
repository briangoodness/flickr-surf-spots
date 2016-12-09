# Mapping Using Flickr Surf Spots

## App Hosted @ : http://flickr-surf-spots.herokuapp.com/

## Technology Stack:
- Frontend: Bootstrap, Leaflet JS / CSS
- Web Framework: Django (relies upon Django-GeoJson)
- Database: PostgreSQL/PostGIS (Hosted on Heroku)
- App Server: Heroku
- File Server: Amazon S3

## Notes:
- In order to get GeoJSON working, I had to fix a bug in the serializers.py file of the django-geojson package's code (reference: https://github.com/makinacorpus/django-geojson/issues/80)
- In order to install Shapely on Heroku, a custom Python buildpack must be added. This can be done using the instructions here: https://github.com/JasonSanford/heroku-buildpack-python-geos
