#coding=utf-8
from enthought.traits.api import HasTraits,Float,Property,cached_property
class Rectangle(HasTraits):
	width=Float(1.0)
	height=Float(2.0)

	area=Property(depends_on=['width','height'])

	@cached_property
	def _get_area(self):
		"area的get函数，注意此函数名和对应的Property属性名的关系"

		print 'recalculating'
		return self.width * self.height