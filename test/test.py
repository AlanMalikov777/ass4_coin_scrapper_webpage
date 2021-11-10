import sys
sys.path.append("..")
from src import news
from src import web_server
from src import dbpy
web_server.start()