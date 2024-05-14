{%- macro argument_builder(api_parameters) %}
    {%- if api_parameters %}
    {%- for param in api_parameters%}
    {%- if loop.first %}, {% endif %} {{- param.name }}: {{ param.data_type }}{% if not param.is_required %} = None{% endif %}{% if not loop.last %}, {% endif %}
    {%- endfor %}
    {%- endif %}
{%- endmacro %}

{% macro url_builder(api_group, api_method) %}
{{- api_group.upper() }}_{{ api_method.upper() -}}
{% endmacro %}

{% macro param_builder(api_parameters) %}
    {% if api_parameters %}
    params = {
        {%- for param in api_parameters%}
        "{{param.name}}": {{param.name}}{% if not loop.last %},{% endif -%}
        {% endfor %}
    }
    {% else %}
    params = None
    {% endif -%}
{% endmacro %}
