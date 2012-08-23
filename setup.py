#!/usr/bin/env python
from distutils.core import setup

setup(
    name = 'django-report-tools',
    description = 'Class-based reports for elegant data views.',
    version = '0.1',
    author = 'Evan Brumley',
    author_email = 'evan.brumley@gmail.com',
    url = 'http://github.com/evanbrumley/django-report-tools',
    packages=['report_tools', 'report_tools.tests', 'report_tools.renderers',
        'report_tools.renderers.googlecharts', 
        'report_tools.renderers.googlecharts.gviz_api'],
    package_data={'report_tools': [
        'templates/report_tools/renderers/googlecharts/*.html',
        'renderers/googlecharts/gviz_api/COPYRIGHT',
        'renderers/googlecharts/gviz_api/README']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
