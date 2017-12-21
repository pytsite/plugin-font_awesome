"""PytSite Font Awesome Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _register_assetman_resources():
    from plugins import assetman

    if not assetman.is_package_registered(__name__):
        assetman.register_package(__name__)
        assetman.t_css(__name__)
        assetman.t_copy_static(__name__)
        assetman.js_module('font-awesome', __name__ + '@font-awesome')
        assetman.library('font-awesome', [
            'font_awesome@css/font-awesome.css'
        ])

    return assetman


def plugin_install():
    _register_assetman_resources().build(__name__)


def plugin_load():
    _register_assetman_resources()
