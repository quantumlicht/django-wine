class NameSearchMixin(object):

	def get_queryset(self):
		queryset = super(NameSearchMixin, self).get_queryset()

		q = self.request.GET.get('q')
		if q:
			return queryset.filter(name__icontains=q)

		return queryset