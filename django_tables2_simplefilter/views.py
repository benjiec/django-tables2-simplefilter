
from django_tables2 import SingleTableView

def F(field, verbose_name, values_list):
  for f in values_list:
    if (type(f[0]) != type('') and type(f[0]) != type(u'')) or \
       (type(f[1]) != type('') and type(f[1]) != type(u'')):
      raise Exception('Filter values list should have string values for both option name and value')
  return dict(field=field, verbose_name=verbose_name, values_list=values_list)


class FilteredSingleTableView(SingleTableView):
  """
  Add filtering options to SingleTableView. Define list of filters in the Table
  subclass (not in Table.Meta). Likely not secure.

  List of filters should be list of values returned by the F function. The
  values list passed into F should be a tuple of verbose value and actual
  value. For example,

    import django_tables2 as tables
    class MyTable(tables.Table):
      ...
      filters = (F('field1','Filter name',values_list=(('True','1'),('False','0'))),
                 F('field2','Another filter',values_list=[ (str(x), x.name) for x in SomeModel.objects.all()]))

  In your template, include django_tables2_simplefilter/filter_selection.html,
  passing in the filters variable. For example,

    {% include "django_tables2_simplefilter/filter_selection.html" with filters=filters only %}

  CSS classes are: filter-form, filter-item, filter-name, filter-selection,
  filter-actions, filter-submit, filter-reset

  """

  def get_queryset(self):
    q = super(FilteredSingleTableView, self).get_queryset()
    if hasattr(self.table_class, 'filters'):
      h = {}
      for f in self.table_class.filters:
        field = f['field']
        if field in self.request.GET and self.request.GET[field]:
          h[field] = self.request.GET[field]
      q = q.filter(**h)
    return q

  def get_context_data(self, **kwargs):
    c = super(FilteredSingleTableView, self).get_context_data(**kwargs)
    if hasattr(self.table_class, 'filters'):
      h = []
      for f in self.table_class.filters:
        v = {}
        field = f['field']
        v = dict(**f)
        v['selected'] = None
        if field in self.request.GET and self.request.GET[field] != "":
          v['selected'] = self.request.GET[field]
        h.append(v)
      c['filters'] = {}
      c['filters']['filters'] = h

      # now add base params for sorting, pagination, etc.
      table = self.get_table()
      base_params = [table.prefixed_order_by_field,
                     table.prefixed_page_field,
                     table.prefixed_per_page_field]
      base_param_values = []
      for p in base_params:
        if p in self.request.GET and self.request.GET[p] != "":
          base_param_values.append((p, self.request.GET[p]))
      c['filters']['base_params'] = base_param_values
    return c 

