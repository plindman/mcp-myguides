
import logging
import json
from logging import LogRecord

class JSONFormatter(logging.Formatter):
    """
    Formats log records as JSON strings.
    """
    def format(self, record: LogRecord) -> str:
        log_object = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
        }
        if record.exc_info:
            log_object["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_object)

def setup_logging():
    """
    Sets up structured logging for the application.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove any existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
