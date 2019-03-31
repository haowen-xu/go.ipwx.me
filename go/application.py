from sanic import Sanic
from .zotero import zotero_bp

__all__ = ['app']

app = Sanic(__name__)
app.blueprint(zotero_bp, url_prefix='/zotero')
