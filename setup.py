from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name = 'pgbackup',
    version = '0.1.0',
    description = 'Backs up a PostgreSQL database locally or to an S3 bucket',
    long_description = readme,
    author='Shashank Chattopadhyaya',
    author_email = 'shashank.chattopadhyaya@gmail.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = []
)

