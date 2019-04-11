from sanic import Sanic
from .wiki import wiki_bp
from .zotero import zotero_bp

__all__ = ['app']

app = Sanic(__name__)
app.blueprint(wiki_bp, url_prefix='/wiki')
app.blueprint(zotero_bp, url_prefix='/zotero')
