"""PytSite Font Awesome Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from plugins import assetman

    assetman.register_package(__name__)
    assetman.t_js(__name__)
    assetman.t_css(__name__)
    assetman.t_copy_static(__name__)

    # Version 4
    assetman.js_module('font-awesome-4', __name__ + '@font-awesome-4')
    assetman.library('font-awesome-4', 'font_awesome@v4/css/font-awesome.css')

    # Alias for backward compatibility
    assetman.js_module('font-awesome', __name__ + '@font-awesome-4')
    assetman.library('font-awesome', 'font-awesome-4')

    # Version 5
    assetman.js_module('font-awesome-5', __name__ + '@font-awesome-5')
    assetman.library('font-awesome-5', 'font_awesome@v5/css/all.min.css')


def plugin_install():
    from plugins import assetman

    assetman.build(__name__)
