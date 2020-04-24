#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <fcntl.h>
int main()
{
 int fd,ret,i;
 char buf[]={0xfb,0xbf,0x06,0x01,0x00,0x07,0xed};
 char buf_1[] = {0xfb,0xbf,0x06,0x02,0x00,0x08,0xed};
 char buf_2[] =
{0xfb,0xbf,0x0b,0x03,0xD0,0xA1,0xC6,0xBB,0xB9,0xFB,0xB4,0xED};
 char rbuf[99];

 fd = open("/dev/rfcomm0", O_RDWR);
 if(fd < 0){ printf("open dev/rfcomm error!\r\n");
return -1;}

 //write(fd,buf_1,sizeof(buf_1));
 //write(fd,buf_1,sizeof(buf_1));
 write(fd,buf_2,sizeof(buf_2));
 printf("write end!\r\n");

 while(1){
 ret = read(fd,rbuf,sizeof(rbuf));
 printf("recv ret:%d\r\n",ret);
for(i=0; i<ret; i++)
printf("[%d]:%x ",i, rbuf[i]);
sleep(1);
 }
 close(fd);

}