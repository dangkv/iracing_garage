{% import "function_macros.py" as macros %}

def {{ api_method }}(self{{ macros.argument_builder(api_parameters) }}) -> dict:

    endpoint = endpoints.URL_{{- macros.url_builder(api_group, api_method) }}
    func_name = inspect.stack()[0][3]

    {{- macros.param_builder(api_parameters) }}
    return self._get(
        url=endpoint,
        api_group=self.api_group,
        func_name=func_name,
        params=params,
    )
