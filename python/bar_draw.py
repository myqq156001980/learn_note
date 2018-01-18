import matplotlib as mpl

import matplotlib.pyplot as plt
import numpy as np

# mpl.use('Agg')

# 必须配置中文字体，否则会显示成方块
# 注意所有希望图表显示的中文必须为unicode格式
custom_font = mpl.font_manager.FontProperties(fname='/Library/Fonts/华文细黑.ttf')


font_size = 10  # 字体大小
fig_size = (8, 6)  # 图表大小

names = (u'小明', u'小红')  # 姓名
subjects = (u'语文', u'数学', u'英语', '化学')  # 科目
scores = ((65, 90, 75, 90), (85, 80, 90, 100),)  # 成绩

# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小z
mpl.rcParams['figure.figsize'] = fig_size
# 设置柱形图宽度
bar_width = 0.35

index = np.arange(len(scores[0]))
# 绘制「小明」的成绩
rects1 = plt.bar(index, scores[0], bar_width, color='#0072BC', label=names[0])
# 绘制「小红」的成绩
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
# X轴标题
plt.xticks(index + bar_width, subjects, fontproperties=custom_font)
# Y轴范围
plt.ylim(ymax=100, ymin=0)
# 图表标题
plt.title(u'企鹅班同学成绩对比', fontproperties=custom_font)
# 图例显示在图表下方
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, ncol=5, prop=custom_font)


# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('white')


add_labels(rects1)
add_labels(rects2)

# 图表输出到本地
plt.savefig('scores_par.png')
