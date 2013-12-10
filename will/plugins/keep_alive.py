import datetime
import requests
from will.plugin_base import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template
import will.settings as settings


class KeepAlivePlugin(WillPlugin):
    keep_alive_url = "/keep-alive"

    @periodic(second=0)
    def ping_keep_alive(self):
        requests.get("%s%s" % (settings.WILL_URL, keep_alive_url))

    @route(keep_alive_url)
    @rendered_template("keep_alive.html")
    def keep_alive(self):
        return {}

    @route("/ping")
    def ping(self):
        self.say("Someone pinged me!")
        return "PONG"
