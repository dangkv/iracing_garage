import json
from jinja2 import Environment, FileSystemLoader


def read_json(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def load_methods(doc: dict, api_group: str) -> dict:
    api_methods = doc.get(api_group)
    method_list = []

    for method_name, method_value in api_methods.items():
        parameter_list = []

        if method_value.get("parameters"):
            for key, value in method_value.get("parameters").items():
                param = ApiParameters(
                    name=key,
                    data_type=value.get("type"),
                    note=value.get("note"),
                    is_required=value.get("required", False),
                )
                parameter_list.append(param)

        method = ApiMethods(
            api_group=api_group,
            api_method=method_name,
            link=method_value.get("link"),
            note=method_value.get("note"),
            parameters=parameter_list,
        )

        method_list.append(method)

    return method_list


def print_functions(method_list: list, template):
    with open(
        "src/tools/function_builder/python_endpoints.py",
        mode="w",
        encoding="utf-8",
    ) as output:
        for method in method_list:
            params = method.parameters

            the_function = template.render(
                api_group=method.api_group,
                api_method=method.api_method,
                api_parameters=params,
            )
            output.write(the_function)


def main(json_path: str, api_group: str) -> None:
    env = Environment(
        loader=FileSystemLoader("src/tools/function_builder/templates/")
    )
    function_template = env.get_template("function_template.py")
    doc = read_json(json_path)
    method_list = load_methods(doc=doc, api_group=api_group)
    print_functions(method_list, function_template)
    print()


class ApiMethods:
    def __init__(
        self,
        api_group: str,
        api_method: str,
        link: str,
        note=None,
        parameters: list = None,
    ):
        self.api_group = api_group
        self.api_method = api_method
        self.parameters = self._sort_parameters(parameters)
        self.note = note

    @staticmethod
    def _sort_parameters(parameters: list = None) -> list:
        """_summary_
        Sort parameters so that all required parameters are first in the list.
        """
        if parameters is None:
            return

        return sorted(parameters, key=lambda p: p.is_required, reverse=True)


class ApiParameters:
    def __init__(
        self,
        name: str,
        data_type: str,
        note: str,
        is_required: bool,
    ):
        self.name = name
        self.data_type = self._to_py_data_type(data_type)
        self.note = note
        self.is_required = is_required

    @staticmethod
    def _to_py_data_type(data_type):
        data_type_map = {
            "boolean": "bool",
            "number": "int",
            "numbers": "int",
            "string": "str",
        }
        return data_type_map[data_type]


if __name__ == "__main__":
    api_group = "member"
    json_path = "src/tools/api.json"
    main(json_path, api_group)
