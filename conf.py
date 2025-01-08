from pathlib import Path
from shutil import copy
from typing import Optional

from sphinx.application import Sphinx

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Portfolio'
copyright = '2025, Olivia Appleton-Crocker'
author = 'Olivia Appleton-Crocker'
rst_prolog = """
.. meta::
    :fediverse:creator: https://tech.lgbt/@LivInTheLookingGlass

.. raw:: html

    <a rel="me" href="https://tech.lgbt/@LivInTheLookingGlass" role="none"
     style="display: none; visibility: hidden; pointer-events: none; animation: none; transition: none"></a>
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx_tags',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# -- Options for sphinx-tags extension ---------------------------------------
# https://sphinx-tags.readthedocs.io/en/latest/configuration.html

tags_create_tags = True
tags_page_title = 'Tags'

# -- Options extend the bulid process ----------------------------------------
# https://www.sphinx-doc.org/en/master/development/tutorials/extending_build.html


def build_finished(app: Sphinx, exception: Optional[Exception]):
    if app.builder.name == 'html':
        source = Path(__file__).parent.joinpath('webfinger')
        dest_path = Path(app.outdir, '.well-known', 'webfinger')
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        copy(source, dest_path)


def setup(app):
    app.connect('build-finished', build_finished)
