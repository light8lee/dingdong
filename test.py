from dingdong import wx_reminder

@wx_reminder(enable_cmd_qr=2)
def test_correct():
    print('hello there')

@wx_reminder(enable_cmd_qr=2)
def test_exception():
    raise("it's so terrible")

if __name__ == '__main__':
    test_correct()
    test_exception()