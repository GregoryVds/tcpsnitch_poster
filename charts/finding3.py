import matplotlib
# Do not use any X11 backend
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import numpy as np
import matplotlib.pyplot as plt

objects = ('socket', 'connect', 'getsockopt', 'setsockopt', 'fcntl',
           'getsockname', 'read', 'bind', 'poll', 'close',
           'write', 'select', 'recvfrom', 'sendto', 'recv',
           'send', 'epoll_ctl', 'epoll_wait', 'epoll_pwait', 'ioctl',
           'listen', 'shutdown', 'getpeername', 'accept4', 'accept',
           'sendmsg', 'writev', 'recvmsg', 'readv')

y_pos = np.arange(len(objects))
usage = [100, 100, 100, 100, 100, 98, 97, 95, 93, 93, 92, 86, 76, 75, 52, 48, 43, 41, 41, 35, 16, 14, 12, 12, 12, 5, 2, 1, 1]

plt.bar(y_pos, usage, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Percentage of apps using function')
plt.title('Android API functions usage')
plt.ylim([0,100])
plt.margins(x=0.01, y=0)
plt.grid(True, axis='y')
plt.yticks(range(101)[0::10])
plt.xticks(rotation='vertical')

plt.tight_layout()
fig=plt.figure(1)
fig.patch.set_facecolor('#EBEBEB')
plt.savefig("finding3.pdf", facecolor=fig.get_facecolor(), edgecolor='none')
