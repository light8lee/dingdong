import paho.mqtt.client as mqtt
import itchat
import datetime
import traceback
import functools
import socket

DATE_FORMAT = "%Y-%m-%d %H:%M:%d"

def mqtt_reminder(host: str='localhost', port: int=1883, topic: str='dingdong', qos: int=1):
    """mqtt reminder decorator
    
    Keyword Arguments:
        host {str} -- mqtt server host (default: {'localhost'})
        port {int} -- mqtt server port (default: {1883})
        topic {str} -- mqtt topic that will be published (default: {'dingdong'})
        qos {int} -- qos of mqtt, can be 0/1 (default: {1})
    """
    client = mqtt.Client()
    client.connect(host, port, 60)
    print(client)
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
            client.publish(topic, content, qos)

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
                client.publish(topic, content, qos)
                client.disconnect()
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
                client.publish(topic, content, qos)
                client.disconnect()
                raise ex

        return wrapper_sender

    return decorator_sender