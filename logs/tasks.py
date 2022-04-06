from logs.celery import app
import glob
import re

from apachelogs import LogParser
from celery.utils.log import get_task_logger

from config.settings import settings
from logs.models import Log
from logs.utils import check_log_line

logger = get_task_logger(__name__)


@app.task()
def parsing_logs_task():
    logger.info('Задача parsing_logs_task запущена')
    format = re.sub(r'\\', "", settings.APACHE_LOG_FORMAT)
    parser = LogParser(format)
    file_mask = settings.APACHE_LOG_FOLDER + "/" + settings.APACHE_LOG_FILE
    for file in sorted(glob.glob(file_mask)):
        with open(file, "r") as f:
            for line in f:
                if check_log_line(parser, line):
                    data = parser.parse(line)
                    Log.objects.get_or_create(
                        host=data.remote_host,
                        request_time=data.request_time,
                        request_line=data.request_line,
                        remote_logname=data.remote_logname,
                        remote_user=data.remote_user,
                        referer=data.headers_in["Referer"],
                        user_agent=data.headers_in["User-agent"],
                        final_status=data.final_status,
                        bytes_sent=data.bytes_sent,
                    )
        logger.info('Задача parsing_logs_task завершена')
