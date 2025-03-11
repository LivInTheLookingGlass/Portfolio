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
rst_prolog = '''
.. meta::
    :fediverse:creator: @LivInTheLookingGlass@transfem.social

.. raw:: html

    <a rel='me' href='https://transfem.social/@LivInTheLookingGlass' role='none'
     style='display: none; visibility: hidden; pointer-events: none; animation: none; transition: none'></a>
    <script data-goatcounter='https://livinthelookingglass.goatcounter.com/count'
     async src='//gc.zgo.at/count.js'></script>

.. |orcid-logo| image:: /_static/icons/ORCID-iD_icon_vector.svg
    :alt: ORCiD logo
    :class: logo
    :target: https://orcid.org/0009-0004-2296-7033

.. |linkedin-logo| image:: /_static/icons/In-Blue-128@2x.png
    :alt: LinkedIn logo
    :class: logo
    :target: https://www.linkedin.com/in/olivia-kay-appleton

.. |github-logo| image:: /_static/icons/github-mark.svg
    :alt: GitHub logo
    :class: logo
    :target: https://github.com/LivInTheLookingGlass

.. |gitlab-logo| image:: /_static/icons/gitlab-logo-500.svg
    :alt: GitLab logo
    :class: logo gitlab-logo
    :target: https://gitlab.com/LivInTheLookingGlass

.. |osm-logo| image:: /_static/icons/osm-logo-2011.svg
    :alt: OpenStreetMap logo
    :class: logo
    :target: https://www.openstreetmap.org/user/LivInTheLookingGlass

'''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx_tags',
    'sphinxcontrib.mermaid',
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_title = "Olivia Appleton-Crocker's Portfolio"
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_favicon = '_static/favicon.png'
html_baseurl = 'https://oliviaappleton.com'
html_theme_options = {
    'accent_color': 'violet',
    'light_logo': '_static/favicon-light.svg',
    'dark_logo': '_static/favicon-dark.svg',
}

# -- Options for external link roles -----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html

extlinks = {
    'github': ('https://github.com/%s', '|github-logo| %s'),
    'gitlab': ('https://gitlab.com/%s', '|gitlab-logo| %s'),
}

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
        for name in ('robots.txt', '_redirects'):
            source = Path(__file__).parent.joinpath(name)
            dest_path = Path(app.outdir, name)
            copy(source, dest_path)


def setup(app):
    app.connect('build-finished', build_finished)
