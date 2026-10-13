import logging
import json
from datetime import datetime, timezone


class JSONFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        })


def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.handlers = [handler]