import matplotlib
# Do not use any X11 backend
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import numpy as np
import matplotlib.pyplot as plt
objects = ["socket", "setsockopt", "getsockopt", "fcntl", "connect", "getsockname", "read", "bind", "poll", "close", "write", "select", "recvfrom", "sendto", "recv", "send", "epoll_ctl", "epoll_wait", "epoll_pwait", "ioctl", "listen", "shutdown", "getpeername", "accept4", "accept", "sendmsg", "writev", "recvmsg", "readv", "fdopen", "dup"]
andro = [100, 100, 100, 100, 100, 98, 97, 95, 93, 93, 92, 86, 76, 75, 52, 48, 43, 41, 41, 35, 16, 14, 12, 12, 12, 5,  2,  1,  1, 0, 0]
linux = [100,  69,  71,  80, 100, 59, 54, 33, 45, 95, 52, 26, 92,  9, 54, 54, 26, 16,  0, 92, 23, 16, 50, 0,  16, 14, 19, 14, 7, 5, 7]

y_pos = np.arange(len(objects))


N = len(objects)
ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind, andro, width, color='b')
rects2 = ax.bar(ind + width, linux, width, color='y')
ax.legend((rects1[0], rects2[0]), ('Android', 'Linux'))


ax.set_xticks(ind + width / 2)
ax.set_xticklabels(objects)

plt.title('API functions usage')
plt.ylabel('Percentage of apps using function')
plt.ylim([0,100])
plt.margins(x=0.01, y=0)
plt.grid(True, axis='y')
plt.yticks(range(100)[0::10])
plt.xticks(rotation='vertical')

plt.tight_layout()
fig=plt.figure(1)
fig.patch.set_facecolor('#EBEBEB')
plt.savefig("finding1.pdf", facecolor=fig.get_facecolor(), edgecolor='none')
