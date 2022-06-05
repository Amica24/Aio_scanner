import logging

from aiohttp import web

from app.scanner.routes import setup_routes as setup_scanner_routes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def setup_app(application):
    setup_scanner_routes(application)


app = web.Application()

if __name__ == "__main__":  #
    setup_app(app)
    web.run_app(app)
