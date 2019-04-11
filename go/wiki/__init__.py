import asyncio

import aiohttp as aiohttp
from sanic import Blueprint, response

__all__ = ['wiki_bp']

MATHJAX_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js'
REPO_BASE_URI = 'https://raw.githubusercontent.com/haowen-xu/' \
                'research-notes/master/'
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
</head>
<body>
{content}
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
</body>
</html>
'''

wiki_bp = Blueprint(__name__)


async def pandoc(md_source):
    proc = await asyncio.create_subprocess_exec(
        'pandoc',
        '-f', 'markdown', '-t', 'html',
        '--mathjax=' + MATHJAX_CDN,
        '-',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    # write the source
    proc.stdin.write(md_source.encode('utf-8'))
    proc.stdin.close()

    # Wait for the subprocess exit.
    await proc.wait()
    return (await proc.stdout.read()).decode('utf-8')


@wiki_bp.route('/<path:path>')
async def go_to_paper(request, path):
    # canonical the path
    path = path.lstrip('/')
    if path.endswith('/') or path.endswith('.md'):
        path = path.replace(' ', '_').rstrip('/') + '.md'
    uri = REPO_BASE_URI + path

    # for non-markdown file, just redirect
    if not uri.endswith('.md'):
        return response.redirect(uri)

    # fetch the markdown file
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as resp:
            if resp.status != 200:
                return response.html(await resp.text(), resp.status)

            md_source = await resp.text()

    # use pandoc to translate the markdown into html
    html = await pandoc(md_source)
    html = PAGE_TEMPLATE.format(
        content=html
    )
    return response.html(html)
