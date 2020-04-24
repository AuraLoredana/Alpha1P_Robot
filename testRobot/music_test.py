import os
from time import sleep

char1 = {0xfb, 0xbf, 0x06, 0x02, 0x00, 0x08, 0xed}
print(char1)
char2 = {0xfb, 0xbf, 0x06, 0x02, 0x00, 0x08, 0xed}
print(char2)
char3 = {0xfb, 0xbf, 0x0b, 0x03, 0xD0, 0xA1, 0xC6, 0xBB, 0xB9, 0xFB, 0xB4, 0xED}
print(char3)
fd = os.open("/dev/rfcomm0", os.O_RDWR | os.O_CREAT)
# ser = serial('dev/rfcomm0', 9600)
#
# while True:
#     result = ser.read()
#     print(result)

def openRfcomm():
    if fd < 0:
        print("open dev/rfcomm error!\r\n")
        return -1


# write(fd,char2,sizeof(char2))
# write(fd,char2,sizeof(char2))

os.write(fd, char3, len(char3))
print("write end!\r\n")

while True:
    print("recv ret:%d\r\n", ret)
    ret = os.read(fd, char1, len(char1))
    for i in ret:
        print("[%d]:%x ", i, char1[i])
        sleep(1)
        os.close(fd)
