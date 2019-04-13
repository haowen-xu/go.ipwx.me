from sanic import Blueprint, response

__all__ = ['wiki_bp']

wiki_bp = Blueprint(__name__)


@wiki_bp.route('/<path:path>')
async def go_to_page(request, path):
    uri = 'https://wiki.haowen-xu.com/' + path
    return response.redirect(uri)
