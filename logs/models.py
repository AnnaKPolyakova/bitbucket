from django.db import models


class Log(models.Model):
    host = models.CharField(
        verbose_name="host",
        max_length=150,
    )
    request_time = models.DateTimeField(
        verbose_name='request_time',
    )
    request_line = models.CharField(
        verbose_name='request_line',
        max_length=150,
        blank=True,
        null=True,
    )
    remote_logname = models.CharField(
        verbose_name='remote_logname',
        max_length=150,
        blank=True,
        null=True,
    )
    remote_user = models.CharField(
        verbose_name='remote_user',
        max_length=150,
        blank=True,
        null=True,
    )
    referer = models.CharField(
        verbose_name='referer',
        max_length=150,
    )
    user_agent = models.CharField(
        verbose_name='user_agent',
        max_length=150,
    )
    final_status = models.PositiveIntegerField(
        verbose_name='final_status',
        blank=True,
        null=True,
    )
    bytes_sent = models.PositiveIntegerField(
        verbose_name='bytes_sent',
    )

    class Meta:
        verbose_name_plural = "Логи"
        verbose_name = "Логи"

    def __str__(self):
        return f"host: {self.host}, request_time: {self.request_time}"
