# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'fixitinfirmware'
copyright = '2025, Ralph Hempel'
author = 'Ralph Hempel'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sys
import os

sys.path.append(os.path.abspath('extensions'))
sys.path.append(os.path.abspath('glossaries'))

extensions = ['glossary.glossary',
              'teaserlink',
             ]

templates_path = ['_templates']
exclude_patterns = ['drafts/*']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'my_piccolo_theme'
html_theme_path = ['themes']
html_static_path = ['_static']
html_short_title = "Fix It In Firmware ..."

html_theme_options = {
  "header_nav_links": {"About":"pages/about/index",
                       "Resources":"pages/resources/index",
                       "Archive":"posts/index",
  }
}