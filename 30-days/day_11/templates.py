import os

FILE_PATH = os.path.abspath(__file__)
print(FILE_PATH)
BASE_DIR = os.path.dirname(FILE_PATH)
print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


class Template:
    template_name = ''
    context = None

    def __init__(self, template_name="", context=None, *args, **kwargs):
        self.template_name = template_name
        self.context = context

    def get_template(self):
        template_path = os.path.join(TEMPLATE_DIR, self.template_name)
        if not os.path.exists(template_path):
            raise Exception("Esto no existe")
        template_content = ''
        with open(template_path, 'r') as f:
            template_content = f.read()
        return template_content

    def render(self, context=None):
        render_context = {}
        if self.context is not None:
            render_context = self.context
        else:
            render_context = context

        if not isinstance(render_context, dict):
            render_context = {}
        template_content = self.get_template()
        return template_content.format(**render_context)


obj = Template(template_name="hello.txt", context={"name": "Alberto"})
print(obj.context)
print(obj.render())
