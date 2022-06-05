import json
import logging
import socket

from aiohttp import web


def is_port_open(host, port) -> bool:
    """
    determine whether `host` has the `port` open
    """
    s = socket.socket()
    try:
        s.connect((host, port))
    except Exception as error:
        logging.info(f'Ошибка при подключении к порту {port}: {error}')
        return False
    else:
        logging.info(f'Подключении к порту {port} произведено успешно')
        return True


async def handle(request):
    """
    returns ports and states (open/close)
    """
    logging.info('Получен входящий запрос')
    host = request.match_info['ip']
    begin_port = int(request.match_info['begin_port'])
    end_port = int(request.match_info['end_port'])
    response_obj = []
    for port in range(begin_port, end_port):
        if is_port_open(host, port):
            response_obj.append({'port': port, 'state': 'open'})
        else:
            response_obj.append({'port': port, 'state': 'close'})
    return web.Response(text=json.dumps(response_obj), status=200)
