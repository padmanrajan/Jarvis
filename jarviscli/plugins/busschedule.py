from plugin import LINUX, PYTHON3, plugin, require
import tabula
import time
import re
@require(python=PYTHON3, platform=LINUX)
@plugin('busschedule')
def busschedule(jarvis, s):
    df2 = tabula.read_pdf("http://iitmandi.ac.in/files/inst_bus_schedule_12thjune2019.pdf",pages='1-2',multiple_tables=True)
    t1=df2[0][0]
    t2=df2[2][2]
    st2=t2.to_string()
    sn1=re.findall('\\d+:\\d+',st2)
    st1=t1.to_string()
    sn2=re.findall('\\d+:\\d+ ',st1)
    sn=sn2+sn1
    arr=time.ctime().split(' ')
    systime=arr[3].split(':')
    flag=0
    for i in range(0,len(sn)):
        bustimeinHr=sn.__getitem__(i).split(':')
        if( systime.__getitem__(0) <= bustimeinHr.__getitem__(0)): 
            if(systime.__getitem__(1) <= bustimeinHr.__getitem__(1)):
                print("Next bus to North campus: "+sn.__getitem__(i))
                flag=1
                break
    if(flag==0):
        print("No bus today")
