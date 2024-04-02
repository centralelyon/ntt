# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import ntt

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ntt'
copyright = '2023, Romain Vuillemot'
author = 'Romain Vuillemot'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx_design',
        'nbsphinx',
        'nbsphinx_link']

templates_path = ['_templates']

exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

#       'pygment_light_style': 'lightbulb',
#       'pygment_dark_style': 'monokai'
#         'pygment_light_style': 'github-light',
#         'pygment_dark_style': 'github-dark'

html_theme_options = {
        'github_url': 'https://github.com/centralelyon/ntt/',
        'show_prev_next': False,
        'pygment_light_style': 'github-light',
        'pygment_dark_style': 'github-dark'
}

html_logo = 'images/logo_liris.png'

html_css_files = ['custom.css']

# -- Options for nbsphinx extension  -------------------------------------------------

# Avoid duplicate display of widgets, see: https://github.com/spatialaudio/nbsphinx/issues/378#issuecomment-573599835
nbsphinx_execute = 'never'
nbsphinx_widgets_path = ''
