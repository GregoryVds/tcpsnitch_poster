import matplotlib
# Will only work with matplotlib 2.x

# Do not use any X11 backend
matplotlib.use('Agg')
# matplotlib.rcParams['hatch.linewidth'] =0.1  # previous pdf hatch linewidth
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Network info - 85%',
          'connect() - 8%',
          'Exchange data - 6%',
          'Other usages - 1%']
values = [85,8,6,1]

plt.style.use('classic')
plt.figure(figsize=(7, 4.5))

pie = plt.pie(values, startangle=90,  pctdistance=1.3)
patches = pie[0]
patches[0].set_hatch("///")
patches[1].set_hatch("\\\\\\")
patches[2].set_hatch("---")
patches[3].set_hatch("|||")

#NUM_COLORS = len(labels)
#cm = plt.get_cmap('gist_rainbow')
#plt.gca().set_prop_cycle("color", [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])

plt.axis('equal')
l = plt.legend(pie[0], labels,  bbox_to_anchor=(0.45, 0.35))
for i, text in enumerate(l.get_texts()):
    if i==0:
        text.set_color("red")

plt.gcf().subplots_adjust(top=0.90)
fig=plt.figure(1)
fig.patch.set_facecolor('#EBEBEB')
plt.savefig("finding4.pdf", facecolor=fig.get_facecolor(), edgecolor='none')
