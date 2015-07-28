# Render, render_to_response , HTTPResponse
- render, is simply a wrapper around HTTPResponse that takes template name as an argument and then render this template with given parameters to retrun a HTTPResponse with rendered body. Required Argument is request & template_name

- render_to_response, renders a given template with given context dictionary and returns an HTTPResponse object with rendered text. Required Argument is template_name

- HTTPResponse is typically used to pass contents of a page as a string.


