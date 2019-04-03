import itchat
import datetime
import traceback
import functools
import socket

DATE_FORMAT = "%Y-%m-%d %H:%M:%d"


def wx_reminder(to_user: str='filehelper', enable_cmd_qr: int=1):
    itchat.auto_login(hotReload=True, enableCmdQR=enable_cmd_qr)
    def decorator_sender(func):
        @functools.wraps(func)
        def wrapper_sender(*args, **kwargs):

            start_time = datetime.datetime.now()
            host_name = socket.gethostname()
            func_name = func.__name__
            contents = ['Your training has started.',
                        'Machine name: %s' % host_name,
                        'Main call: %s' % func_name,
                        'Starting date: %s' % start_time.strftime(DATE_FORMAT)]
            content = '\n'.join(contents)
            itchat.send(content, toUserName=to_user)

            try:
                value = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time
                contents = ["Your training is complete.",
                            'Machine name: %s' % host_name,
                            'Main call: %s' % func_name,
                            'Starting date: %s' % start_time.strftime(DATE_FORMAT),
                            'End date: %s' % end_time.strftime(DATE_FORMAT),
                            'Training duration: %s' % str(elapsed_time)]
                content = '\n'.join(contents)
                itchat.send(content, toUserName=to_user)
                return value

            except Exception as ex:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time
                contents = ["Your training has crashed.",
                            'Machine name: %s' % host_name,
                            'Main call: %s' % func_name,
                            'Starting date: %s' % start_time.strftime(DATE_FORMAT),
                            'Crash date: %s' % end_time.strftime(DATE_FORMAT),
                            'Crashed training duration: %s\n\n' % str(elapsed_time),
                            "Here's the error:",
                            '%s\n\n' % ex,
                            "Traceback:",
                            '%s' % traceback.format_exc()]
                content = '\n'.join(contents)
                itchat.send(content, toUserName=to_user)
                raise ex

        return wrapper_sender

    return decorator_sender