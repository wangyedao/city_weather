#-*- coding:utf-8 -*-
# author:**ZLH**
# datetime:2019/6/5 16:16
import re
import requests
from matplotlib import pyplot as plt
headers = {'Host': 'www.yangshitianqi.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
}
"""
kkk
"""
# 获取济南近30天的最低温和最高温
city = input("请输入想要搜索的城市拼音：")
html = requests.get(f'https://www.yangshitianqi.com/{city}/30tian.html',headers=headers).text
# 使用正则提取数据
pattern_temperature = r'<div class="fl i3 nz">(\d+~\d+)℃</div>'
pattern_date = r'<div class="t2 nz">(\d\d\.\d\d)</div>'
temperature = re.findall(pattern_temperature, html)
date = re.findall(pattern_date, html)
print(date)
# 整理数据
max_d = [int(i.split('~')[1]) for i in temperature]
min_d = [int(i.split('~')[0]) for i in temperature]
# print(max_d)
# print(min_d)
# 近30日最低温和最高温
max_m = max(max_d)
min_m = min(min_d)
print(f'最高温度{max_m}°')
print(f'最低温度{min_m}°')
# 近30日最低温最高温所处的日期（第几天）
max_m_d = max_d.index(max_m)
min_m_d = min_d.index(min_m)
print(f'最高温度日期为近三十日的第{max_m_d}天')
print(f'最低温度日期为近三十日的第{min_m_d}天')
# 日期
date = [i.split('.')[0] + '月' + i.split('.')[1] + '日' for i in date]
# 定义图像质量
plt.figure(figsize=(18.5, 9), dpi=180)
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 绘制图像
plt.plot(range(30), max_d, linestyle=':')
plt.plot(range(30), min_d, linestyle=':')

# 显示日期
plt.xticks(range(30), date, rotation=315)

# xy轴标识
plt.xlabel('日期', size=18)
plt.ylabel('温度/℃', size=18)
plt.title('近30日天气情况', size=36)

# 标记最高温和最低温
plt.text(
    # x轴坐标
    max_m_d,
    # y轴坐标
    max_m + 1,
    # 文字
    f'最高温，{max_m}℃',
    # 字体大小
    fontsize=18,
    # 文字颜色
    color='orange',
    # 相对位置-水平
    ha='center',
    # 相对位置-垂直
    va='center',
    # 透明度
    alpha=1
)
plt.text(
    # x轴坐标
    min_m_d,
    # y轴坐标
    min_m - 1,
    # 文字
    f'最低温，{min_m}℃',
    # 字体大小
    fontsize=18,
    # 文字颜色
    color='red',
    # 相对位置-水平
    ha='center',
    # 相对位置-垂直
    va='center',
    # 透明度
    alpha=1
)
# 显示网格
plt.grid(axis='y', alpha=0.2)
plt.savefig(f'{city}.png')
plt.show()