# conf.py
import os
import sys

# Add the project directory to the system path
sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "ntt"
author = "Romain Vuillemot"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

html_theme = "classic"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Extension configuration -------------------------------------------------

# Example configuration for autodoc:
# autodoc_default_options = {
#     'members': True,
#     'undoc-members': True,
#     'private-members': True,
#     'special-members': '__init__',
#     'show-inheritance': True,
# }

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "MyDocumentation"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "letterpaper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    "preamble": "",
}

# -- Options for manual page output ------------------------------------------

man_pages = [(master_doc, "mydocumentation", "My Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (
        master_doc,
        "MyDocumentation",
        "My Documentation",
        author,
        "MyDocumentation",
        "One line description of project.",
        "Miscellaneous",
    ),
]
