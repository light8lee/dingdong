from dingdong import wx_reminder
from dingdong import mqtt_reminder

@wx_reminder(enable_cmd_qr=2)
def test_wx_correct():
    print('hello there')


@wx_reminder(enable_cmd_qr=2)
def test_wx_exception():
    raise("it's so terrible")


@mqtt_reminder(host='localhost', port=1883, topic='dingdong', qos=1)
def test_mqtt_correct():
    print('hello there')


@mqtt_reminder(host='localhost', port=1883, topic='dingdong', qos=1)
def test_mqtt_exception():
    raise("it's so terrible")

if __name__ == '__main__':
    test_wx_correct()
    test_wx_exception()
    test_mqtt_correct()
    test_mqtt_exception()