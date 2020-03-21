import time


def process(percent, width=50):
    if percent>1 :
        percent=1
    show_str = ('[%%-%ds]' % width) % ('#'*int(width*percent))
    print('\r%s%d%%' % (show_str, int(percent*100)), end='')




rec_size=0
total_size = 10241
while rec_size<total_size:
    rec_size +=1024
    time.sleep(0.1)
    process(rec_size/total_size)