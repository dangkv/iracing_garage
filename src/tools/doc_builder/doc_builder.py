import json


# Function to extract endpoints from JSON data and write to markdown file
def extract_and_write_endpoints(json_file_path, markdown_file_path):
    # Read JSON data from file
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Open markdown file for writing
    with open(markdown_file_path, "w") as markdown_file:
        # Iterate through JSON data and write endpoints to markdown file
        for category, endpoints in data.items():
            markdown_file.write(f"## {category}\n\n")
            for endpoint, details in endpoints.items():
                markdown_file.write(f"### {category}.{endpoint}()\n\n")
                if "note" in details:
                    markdown_file.write("".join(details["note"]) + "\n\n")
                else:
                    markdown_file.write("No Description" + "\n\n")

                # Check if parameters exist
                if "parameters" in details:
                    markdown_file.write(
                        "| Parameter | Type | Description | Required |\n"
                    )
                    markdown_file.write(
                        "|:---------|:----:|:------------|:--------:|\n"
                    )
                    for param_name, param_details in details[
                        "parameters"
                    ].items():
                        param_type = param_details.get(
                            "type", "Unknown"
                        )  # Check if 'type' key exists
                        param_note = param_details.get(
                            "note", "No description available"
                        )  # Check if 'note' key exists
                        required = param_details.get(
                            "required", False
                        )  # Check if 'required' key exists
                        markdown_file.write(
                            f'| `{param_name}` | `{param_type}` | {param_note} | {"True" if required else "False"} |\n'
                        )

                markdown_file.write(f"\nlink: ```{details['link']}```\n\n")

            # Add the "---" line after all endpoints in the category are processed
            markdown_file.write("---\n\n")


if __name__ == "__main__":
    # File paths
    json_file_path = "src/tools/api.json"
    markdown_file_path = "src/tools/doc_builder/methods.md"

    # Call the function
    extract_and_write_endpoints(json_file_path, markdown_file_path)
