# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'myst_parser',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'Component Generator'
year = '2022'
author = 'Onna'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.0.0'

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/onna/python-component-generator/issues/%s', '#'),
    'pr': ('https://github.com/onna/python-component-generator/pull/%s', 'PR #'),
}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

#if not on_rtd:  # only set the theme if we're building docs locally
#    html_theme = 'furo'

html_static_path = ["_static"]
html_logo = "_static/o-logo.png"
html_favicon = "_static/favicon.png"
html_theme = "furo"

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
#html_sidebars = {
#   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
#}
#html_short_title = '%s-%s' % (project, version)
html_short_title = "Component Generator"
html_title = "Component Generator"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
