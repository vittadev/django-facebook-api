import re

from setuptools import setup, find_packages
setup(
    name='django-facebook-api',
    version=__import__('facebook_api').__version__,
    description='Django implementation for Facebook Graph API',
    long_description=open('README.md').read(),
    author='ramusus',
    author_email='ramusus@gmail.com',
    url='https://github.com/ramusus/django-facebook-api',
    download_url='http://pypi.python.org/pypi/django-facebook-api',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,  # because we're including media that Django needs
    install_requires=[
        'django',
        'django-annoying',
        'django-social-api>=0.1.1',
        'facebook-sdk==1.0.0',
        'python-dateutil>=1.5',
    ],
    dependency_links=['https://github.com/pythonforfacebook/facebook-sdk/tarball/master#egg=facebook-sdk-1.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
