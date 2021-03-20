from base import connect_mysql
import re
import time
# re.match(pattern, string, flags=0)
pat = r'(CN21090\d){11}'
a = 'CN210902771'
if 'CN21090' in a and len(a) == 11:
    print('符合条件')
else:
    print(f'字符串 {a} 不符合条件')

nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(nowtime)