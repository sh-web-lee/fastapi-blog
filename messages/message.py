from messages.mconfig import mconfigs


class Message:
    def __init__(self, code=mconfigs.c200):
        self._resp = code

    def __str__(self):
        print(str(self._resp))

    def update(self, k, v):
        self._resp[k] = v
        return self

    def to_dict(self):
        return dict(self._resp)

    def __call__(self, k):
        return self._resp[k]

    def recode(self, code):
        self._resp = code
        return self


if __name__=='__main__':
    m = Message()
    m.update('hello', 'test')
    print(m.to_dict(), m('hello'))