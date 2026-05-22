def setup(app):
    app.add_config_value('glossary_path', True, 'html')

    app.add_node(image_glossary,
                 html=(visit_image_glossary_node, depart_image_glossary_node),
                 latex=(visit_image_glossary_node, depart_image_glossary_node),
                 text=(visit_image_glossary_node, depart_image_glossary_node))
    app.add_directive('image_glossary', ImageGlossaryDirective)
    app.connect('build-finished', purge_image_glossary)

    return {'version': '0.1'}   # identifies the version of our extension

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from sphinx.locale import _

import image_glossary

class ImageGlossary(nodes.image, nodes.Element):
    pass

def visit_image_glossary_node(self, node):
    self.visit_image(node)

def depart_image_glossary_node(self, node):
    self.depart_image(node)

class ImageGlossaryDirective(Directive):

    # this enables content in the directive
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "align": directives.unchanged,
    }

    def run(self):
      env = self.state.document.settings.env

      if not hasattr(env, 'image_glossary'):
        env.image_glossary = image_glossary.make_image_glossary()

      image_glossary_node = ImageGlossary('')
      image_glossary_node.attributes['uri'] = env.image_glossary[self.content[0]].uri
      image_glossary_node.attributes['alt'] = env.image_glossary[self.content[0]].alt

      for k,v in self.options.items():
        image_glossary_node.attributes[k] = v

      return [image_glossary_node]

def purge_image_glossary(app, exception):
    if not hasattr(app.builder.env, 'image_glossary'):
      return
    app.builder.env.image_glossary = None
