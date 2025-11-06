from vercel_proxy import DjangovProxy
from server.server.wsgi import application

handler = DjangovProxy(application)
