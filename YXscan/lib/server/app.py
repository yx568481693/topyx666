from flask import Flask

cmsserver = Flask(__name__)
cmsserver.config.from_object('config')
