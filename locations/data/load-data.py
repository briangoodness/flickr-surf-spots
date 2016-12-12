# Python 3.5.2
import time
import os
import pandas as pd
from sqlalchemy import create_engine
import dj_database_url

# load CSV file into DataFrame
filename = 'flickr-photo-uploads.csv'
df = pd.read_csv(filename)
df.id = df.id.astype(int)

# select columns to load
cols = ['id',
        'place_id',
        'datetaken',
        'dateupload',
        'owner',
        'latitude',
        'longitude',
        'latitude_rnd',
        'longitude_rnd',
        'url',
        'page_url',
        'title']

#insert into locations table
conn_info = os.environ['DATABASE_URL']
conn = create_engine(conn_info, pool_size=20, max_overflow=10)
t0 = time.time()
df[cols].to_sql('locations_location', con=conn, if_exists='replace', index=False)
print(time.time() - t0)
