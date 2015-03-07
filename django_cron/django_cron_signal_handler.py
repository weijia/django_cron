from djangoautoconf.auto_conf_signals import before_server_start, before_server_stop
import django_cron

__author__ = 'weijia'


def on_before_server_start(sender, **kwargs):
    django_cron.start_cron_when_run_server()


def on_before_server_stop(sender, **kwargs):
    django_cron.stop()

before_server_start.connect(on_before_server_start)
before_server_stop.connect(on_before_server_start)


