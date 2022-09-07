from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='py-gitea',
    version='0.2.3',
    description='A python wrapper for the Gitea API',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Vincent Langenfeld ',
    author_email='langenfv@tf.uni-freiburg.de',
    keywords=['Gitea','api','wrapper'],
    url='https://github.com/Langenfeld/py-gitea',
    download_url='https://pypi.org/project/py-gitea/'
)

install_requires = [
    'requests',
    'frozendict',
    'pytest'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)