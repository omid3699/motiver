import json

from .settings import BASE_DIR

DATA = json.load(open((BASE_DIR / "motivational-quotes.json"), mode="r"))[
    "motivationalQuotes"
]
