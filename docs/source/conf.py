# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Picturesque'
copyright = '2024, Ridwan bin Mohammad (Tiash)'
author = 'Ridwan bin Mohammad (Tiash)'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = []

templates_path = ['_templates']

# -- Options for HTML output

import sphinx_adc_theme
html_theme = 'sphinx_adc_theme'
html_theme_path = [sphinx_adc_theme.get_html_theme_path()]

# -- Options for EPUB output
epub_show_urls = 'footnote'
