from sanic import Blueprint, response

__all__ = ['zotero_bp']

zotero_bp = Blueprint(__name__)


@zotero_bp.route('/<paper_id:[A-z0-9]+>')
async def go_to_paper(request, paper_id):
    uri = 'https://www.zotero.org/ipwx/items/itemKey/{}'.format(paper_id)
    return response.redirect(uri)
