django-tables2-simplefilter
===========================

Simple filtering support for django-tables2. Works only with queryset based tables.

Usage:

1. Define a list of filters in Table subclass. List of filters should be list
of values returned by the django_tables2_simplefilter.F function. The values
list passed into F, 3rd argument, should be a tuple of verbose value and actual
value. For example,

```
    import django_tables2 as tables
    class MyTable(tables.Table):
      ...
      filters = (F('field1','Filter name',values_list=(('True','1'),('False','0'))),
                 F('field2','Another filter',values_list=[ (str(x), x.name) for x in SomeModel.objects.all()]))
```

First argument to F should be a field name, which can either be a field in the
model, or a related field using the standard Django double-underscore syntax.
E.g. "fktable__field".


2. In your template, include django_tables2_simplefilter/filter_selection.html,
passing in the filters variable. For example,

```
    {% include "django_tables2_simplefilter/filter_selection.html" with filters=filters only %}
```

CSS classes are: filter-form, filter-item, filter-name, filter-selection,
filter-actions, filter-submit, filter-reset


3. Use FilteredSingleTableView in urls.py. For example,

```
  from django_tables2_simplefilter import FilteredSingleTableView
  ...
  urlpatterns = patterns('',
    ...
    url(r'^my-list/$',
        FilteredSingleTableView.as_view(template_name='some_template.html',
                                        table_class=MyTable,
                                        model=MyModel, 
                                        table_pagination={"per_page": 50}),
        name='my-list-view'),

```

