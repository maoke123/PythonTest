﻿#coding=utf-8
from matplotlib.font_manager import fontManager
import matplotlib.pyplot as plt
import os
fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(111)
plt.xticks([])
plt.yticks([])
x,y=0.05,0.08
fonts=[font.name for font in fontManager.ttflist if
os.path.exists(font.name) and os.stat(font.name).st_size>1e6]
font=set(fonts)
dy=(1.0-y)/(len(fonts)/4+(len(fonts)%4!=0))
for font in fonts:
	t=ax.text(x,y,u"中文字体",{'fontname':font,'fontsize':14},tranform=ax.tranxAxes)
	ax.text(x,y-dy/2,font,tranform=ax.tranAxes)
	x+=0.25
	if x>=1.0:
		y+=dy
		x=0.05
plt.show()