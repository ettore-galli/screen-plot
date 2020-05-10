from setuptools import setup, find_packages

packages = find_packages(
    include=[
        'screen_plot',
        'screen_plot.*'
    ]
)

setup(
    name='screen_plot',
    version='0.0.1.dev0',
    packages=packages,
    url='',
    license='',
    author='ettoregalli',
    author_email='',
    description=''
)
