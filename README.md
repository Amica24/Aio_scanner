### Описание проекта

Проект "Aio_scanner" представляет собой web-приложение, предназначенное для
сканирования открытых TCP портов удаленного хоста. Приложение реализует
следующее REST API:

    * GET /scan/<ip>/<begin_port>/<end_port>

    где:
         ip - хост, который необходимо просканировать
         begin_port - начала диапозона портов для сканирования
         end_port - конец диапозона портов дл€ сканирования

    Формат ответа:  [{"port": "integer", "state": "(open|close)"}]
    
Принцип создания интерфейса - REST API на основе Aiohttp Framework.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Amica24/Aio_scanner.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить проект:

```
python3 main.py

```
