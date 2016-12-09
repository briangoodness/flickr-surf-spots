from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template.loader import get_template

# sqlalchemy
import pandas as pd
import os
from sqlalchemy import create_engine, Table
conn_info = os.environ['DATABASE_URL']
conn = create_engine(conn_info, pool_size=20, max_overflow=10)

# Create your views here.
def map(request):
    return render(request, 'map.html')
    
