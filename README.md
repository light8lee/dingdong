# dingdong
Dingdong, your program ends!

This little project was inspired by the projects of [knockknock](https://github.com/huggingface/knockknock) and [itchat](https://github.com/littlecodersh/ItChat). It helps you keeping tracking the status of your programs on your wechat or any MQTT clients.


## Requirements

- pillow
- itchat
- paho-mqtt


## Installation

```shell
git clone https://github.com/light8lee/dingdong && cd dingdong
python setup.py install
```

## Usage

Just like the examples in `test.py`, you need to add the decorator ahead of your function:

```python
@wx_reminder(to_user='wechat_id', enable_cmd_qr=1)
def test_wx_correct():
    print('hello there')
```

The default value of `to_user='filehelper'`, which means that the messages will send to yourself, you can change it to the wechat id of your friends. The `enable_cmd_qr` is to control the QR code in terminal, the detail please refer to [here](https://github.com/littlecodersh/ItChat#%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%BA%8C%E7%BB%B4%E7%A0%81), the default value is `1`, you can try `2` when you meet uncorrect display of QR code in terminal.


You can also apply this project to send messages to MQTT clients. First, you need to start a MQTT server, here I recommend [Mosquitto](https://mosquitto.org/), and using the `mqtt_reminder` decorator to publish a topic:

```python
@mqtt_reminder(host='localhost', port=1883, topic='dingdong', qos=1)
def test_mqtt_correct():
    print('hello there')
```

Here is an example of MQTT client to subscribe the corresponding topic:

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("dingdong")

def on_message(client, userdata, msg):
    print(msg.topic+" " + ":" + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
```

You can save this code to `sub.py`, and run `python sub.py`, when the `test_mqtt_correct()` function starts and ends, it will automatically print the message.

What's more, you can download mqtt clients from APP Store or Google Play to subscribe the topic on your smart phone, so you will not miss the program status.

## Thanks

- [knockknock](https://github.com/huggingface/knockknock) 
- [itchat](https://github.com/littlecodersh/ItChat)


## Contact

Author: Light Lee
Email: light8lee@gmail.com
