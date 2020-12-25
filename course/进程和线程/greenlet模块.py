from greenlet import greenlet

# 通过greenlet可以在函数间来回切换
def eat(name):
    print('%s eat1' % name)
    g2.switch('egon')
    print('%s eat2' % name)
    g2.switch()

def play(name):
    print('%s play1' % name)
    g1.switch()
    print('%s play2' % name)

g1=greenlet(eat)
g2=greenlet(play)

g1.switch('egpn')