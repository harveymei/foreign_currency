#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/8/16 14:33
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: currency.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
1，记录外币增减记录及金额
2，统计每种外币当前合计金额并绘图
3，为每种货币条形图添加数值标签
4，根据支出记录（负浮点数值）重新计算总额
"""

import matplotlib.pyplot as plt
import csv
import datetime

# 文件操作，读取存取记录，并计算各个货币的当前余额
filename = "data.csv"
with open(filename) as f_object:
    reader = csv.reader(f_object)
    header_row = next(reader)  # 读取文件头（首行）

    # 循环遍历每一行，根据货币符号判断将金额依次放入各个货币列表
    usd_list, hkd_list, eur_list = [], [], []
    for row in reader:
        currency_code = row[1]
        # 判断货币类型，根据判断结果分别取值并放入各个货币列表
        if currency_code == 'USD':
            usd_list.append(float(row[-1]))
        elif currency_code == 'HKD':
            hkd_list.append(float(row[-1]))
        else:
            eur_list.append(float(row[-1]))

    # 循环遍历各个货币列表并累加计算总值
    total_usd, total_hkd, total_eur = 0, 0, 0

    for i in usd_list:
        total_usd = total_usd + i
    for j in hkd_list:
        total_hkd = total_hkd + j
    for k in eur_list:
        total_eur = total_eur + k

# 绘图
# plt.rcdefaults()  # Restore the rcParams from Matplotlib's internal default style.
fig, ax = plt.subplots()

# 定义货币名称元组和各个货币总额元组
currency_name = ('USD', 'HKD', 'EUR')
total_amount = (total_usd, total_hkd, total_eur)

# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh
# 位置参数y，条状图的y坐标值，浮点数或者数组形式。
# 位置参数width，条状图宽度值，浮点数或者数组形式。
# ax.barh((0, 1, 2), total_amount, align='center')
hbars = ax.barh((0, 1, 2), total_amount, align='center')

# 设置y轴刻度位置，浮点数列表，列表中元素数量应与y轴刻度标签数量一致。
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks
ax.set_yticks([0, 1, 2])

ax.set_yticklabels(currency_name)  # 设置y轴刻度标签
ax.invert_yaxis()  # 标签从上到下阅读，即倒置y轴（改变排序）
ax.set_xlabel('Amount')  # 设置x轴标签
ax.set_title('Foreign Currency Total Amount')  # 设置图表标题

# 为条状图添加标签
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label
# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
# ax.set_xlim(right=15)  # adjust xlim to fit labels

# plt.show()
saved_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 日期对象转换为日期字符串
plt.savefig(saved_file + '.png')
