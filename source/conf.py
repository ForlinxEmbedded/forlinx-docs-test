# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '123'
copyright = '2025, dell'
author = 'dell'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 其他扩展
    'myst_parser',
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

myst_enable_extensions = [
    "deflist",
    "html_admonition",
    "html_image",
    # 你需要的其它扩展
]

# 如果需要指定文档后缀
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


