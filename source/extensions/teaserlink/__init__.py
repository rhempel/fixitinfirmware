"""TeaserLink extention to embed a TeaserLink header in sphinx outputs."""

from typing import Any, Dict

from sphinx.application import Sphinx

# from .font_handler import Fontawesome
from .teaserlink import _NODE_VISITORS, TeaserLink, teaserlink_node

__version__ = "0.0.1"
__author__ = "Ralph Hempel"
__email__ = "rhempel@hempeldesigngroup.com"


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add teaserlink node to the sphinx builder."""
    # load the teaserlink node/role
    app.add_node(teaserlink_node, **_NODE_VISITORS)  # type: ignore
    app.add_role("teaserlink", TeaserLink())

#    # load the font
#    font_handler = Fontawesome()

#    # install html related files
#    raise Exception(str(font_handler.css_file.resolve()))
#    app.add_css_file(str(font_handler.css_file.resolve()))
#    app.add_js_file(str(font_handler.js_file.resolve()))

 #   # install latex files
 #   app.add_latex_package("fontspec")
 #   app.connect("config-inited", font_handler.add_latex_font)
 #   app.connect("config-inited", font_handler.enforce_xelatex)
 #   app.connect("builder-inited", font_handler.add_latex_font_files)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }