# dingdong
Dingdong, your program ends!

This little project was inspired by the projects of [knockknock](https://github.com/huggingface/knockknock) and [itchat](https://github.com/littlecodersh/ItChat). It helps you keeping tracking the status of your programs on your wechat.


## Requirements

- pillow
- itchat


## Installation

```shell
python setup.py install
```

## Usage

Just like the examples in `test.py`, you need to add the decorator ahead of your function:

```python
@wx_reminder(to_user='wechat_id', enable_cmd_qr=1)
def test_correct():
    print('hello there')
```

The default value of `to_user='filehelper'`, which means that the messages will send to yourself, you can change it to the wechat id of your friends. The `enable_cmd_qr` is to control the QR code in terminal, the detail please refer to [here](https://github.com/littlecodersh/ItChat#%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%BA%8C%E7%BB%B4%E7%A0%81), the default value is `1`, you can try `2` when you meet uncorrect display of QR code in terminal.


## Thanks

- [knockknock](https://github.com/huggingface/knockknock) 
- [itchat](https://github.com/littlecodersh/ItChat)


## Contact

Author: Light Lee
Email: light8lee@gmail.com
