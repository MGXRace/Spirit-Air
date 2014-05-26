#-*- coding: utf-8 -*-
import os
__all__ = ['Air']


_BASE_DIR = os.path.dirname(__file__)


class Air(object):
    name = 'Air'
    author = 'MGXRace'
    description = 'Spirit forum theme inspired by fluxbb\'s Air'

    template_dir = os.path.join(_BASE_DIR, 'templates')
    static_dir = os.path.join(_BASE_DIR, 'static')
    compress_precompilers = (
        (
            'text/spirit-air-scss',
            'cd {0} && sass --scss {{infile}} {{outfile}}'.format(static_dir)
        ),
    )