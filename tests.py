import unittest

from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from app.scanner.views import handle


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/scan/{ip}/{begin_port}/{end_port}/', handle)
        return app

    @unittest_run_loop
    async def test_handle(self):
        async with self.client.request(
                'GET', '/scan/204.152.190.71./20/21/'
        ) as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertIn('port', text)


if __name__ == '__main__':
    unittest.main()
