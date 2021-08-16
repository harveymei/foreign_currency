#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/8/16 14:33
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: currency.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/8/9 17:45
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: example2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import matplotlib.pyplot as plt

# plt.rcdefaults()  # Restore the rcParams from Matplotlib's internal default style.
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim', 'Jerry')
"""
元组中为三种外币的合计金额，当增加或减少时（记录每次增减变化，并重新计算总和），总额应产生变化。
"""
performance = (2.00, 4.00, 6.00, 8.00, 10.00)

# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh
# 位置参数y，条状图的y坐标值，浮点数或者数组形式。
# 位置参数width，条状图宽度值，浮点数或者数组形式。
ax.barh((0, 2, 3, 5, 8), performance, align='center')  # 使用元组传递x轴刻度值

# 设置y轴刻度位置，浮点数列表，列表中元素数量应与y轴刻度标签数量一致。
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks
ax.set_yticks([0, 2, 3, 5, 8, 10])

ax.set_yticklabels(people)  # 设置y轴刻度标签
ax.invert_yaxis()  # 标签从上到下阅读，即倒置y轴（改变排序）
ax.set_xlabel('Performance')  # 设置x轴标签
ax.set_title('How fast do you want to go today?')  # 设置图表标题

plt.show()
