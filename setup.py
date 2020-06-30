import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command
from setuptools import setup, find_namespace_packages
from tethys_apps.app_installation import find_resource_files
from setuptools import setup, find_namespace_packages
### Apps Definition ###
app_package = 'ueb_app'
release_package = 'tethysapp-' + app_package

### Python Dependencies ###
dependencies = []
# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)

setup(
    name=release_package,
    version='0.0.1',
    description='',
    long_description='',
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,

)
