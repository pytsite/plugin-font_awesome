"""PytSite Font Awesome Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from plugins import assetman

    assetman.register_package(__name__)
    assetman.t_css(__name__)
    assetman.t_copy_static(__name__)
    assetman.js_module('font-awesome', __name__ + '@font-awesome')
    assetman.library('font-awesome', [
        'font_awesome@css/font-awesome.css'
    ])


def plugin_install():
    from plugins import assetman

    plugin_load()
    assetman.build(__name__)
