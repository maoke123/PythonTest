# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits,Int,Str,Array,List,Enum
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

class MetadataTest(HasTraits):
	i=Int(99,myinfo="test my info")
	s=Str("test",label=u"字符串",fontproperties=font)

	#NumPy数组
	a=Array
	#元素为Int的列表
	list=List(Int)

test=MetadataTest()