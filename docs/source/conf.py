# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../../'))

import mock
 
MOCK_MODULES = ['numpy', 'scipy.stats', 'scipy', 'matplotlib', 'matplotlib.pyplot', 'scipy.interpolate']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()


# -- Project information -----------------------------------------------------

project = 'EpiGEN'
copyright = '2019, David B. Blumenthal, Lorenzo Viola, Markus List, Jan Baumbach, Tim Kacprowski, Paolo Tieri'
author = 'David B. Blumenthal, Lorenzo Viola, Markus List, Jan Baumbach, Tim Kacprowski, Paolo Tieri'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.napoleon', 'recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
latex_engine = 'pdflatex'
latex_documents = [('index', 'user_guide.tex', 'EpiGEN: an epistasis simulation pipeline', 'David B. Blumenthal, Lorenzo Viola, Markus List, Jan Baumbach, Paolo Tieri, and Tim Kacprowski', 'howto')]
latex_elements = {
'papersize': 'a4paper',
'maketitle': '\\makeatletter\\py@HeaderFamily\\raggedright{\\huge\\@title}\\\\[24pt]{\\Large User Guide}\\\\[24pt]{\\large\\@author}\\makeatother\\normalfont',
'printindex': '\\footnotesize\\raggedright\\printindex'}