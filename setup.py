from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='py-allspice',
    version='{{VERSION_PLACEHOLDER}}',
    description='A python wrapper for the AllSpice Hub API',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='AllSpice, Inc.',
    author_email='maintainers@allspice.io',
    keywords=['AllSpice','AllSpice Hub','api','wrapper'],
    url='https://github.com/Langenfeld/py-gitea',
    download_url='https://github.com/AllSpiceIO/py-allspice'
)

install_requires = [
    'requests',
    'frozendict',
]

extras_require = {
    'test': ['pytest']
}

if __name__ == '__main__':
    setup(
        **setup_args,
        install_requires=install_requires,
        extras_require=extras_require
    )
