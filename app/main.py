"""
File: main.py
Author: Chuncheng Zhang
Date: 2024-07-05
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Fastapi server

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-07-05 ------------------------
# Requirements and constants
from fastapi import FastAPI, Request, Response, HTTPException, responses
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path

from loguru import logger


# %% ---- 2024-07-05 ------------------------
# Function and class

class WebApp(object):
    project_root = Path(__file__).parent.parent
    script_folder = project_root.joinpath('script')
    title = 'Linux Cookbook with Fast API Support'
    app = FastAPI(title=title)
    jinja2_template: Jinja2Templates = None

    def __init__(self):
        self.mount_path()
        self.mount_jinja2_template()
        logger.info(f'Initialized')

    def mount_path(self):
        mounts = [
            dict(
                path='/static', name='static',
                directory=self.project_root.joinpath('web/static'))
        ]

        for dct in mounts:
            self.app.mount(
                path=dct['path'], name=dct['name'],
                app=StaticFiles(directory=dct['directory']))
            logger.debug(f'Mounted path {dct}')

    def mount_jinja2_template(self):
        self.jinja2_template = Jinja2Templates(
            directory=self.project_root.joinpath('web/template'))

    def something_is_wrong(self, exc):
        import traceback
        detail = traceback.format_exc()
        print(detail)
        logger.error(exc)
        return detail


# ----------------------------------------
# ---- Must have app in-advance ----
wa = WebApp()
app = wa.app


# ----------------------------------------
# ---- Routines ----
@app.get('/')
async def index(request: Request):
    return wa.jinja2_template.TemplateResponse('index.html', {'request': request})


@app.get('/findScripts')
async def find_scripts(request: Request):
    files = wa.script_folder.iterdir()
    names = [e.relative_to(wa.script_folder).as_posix() for e in files]
    return names


@app.get(
    '/script',
    response_class=responses.PlainTextResponse)
async def get_script(request: Request, name=None):
    path = wa.script_folder.joinpath(name)
    try:
        return open(path).read()
    except Exception as exc:
        detail = wa.something_is_wrong(exc)
        raise HTTPException(status_code=404, detail=detail)
    finally:
        logger.debug(f'Requested {path}')
        pass


# %% ---- 2024-07-05 ------------------------
# Play ground

# %% ---- 2024-07-05 ------------------------
# Pending

# %% ---- 2024-07-05 ------------------------
# Pending
