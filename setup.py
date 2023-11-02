from setuptools import setup, find_packages


setup(
    name='Loja-ifmt',
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'flask',
        'pycryptodome',
        'sqlalchemy',
        'mysql-connector-python',
        'python-dotenv',
    ]
)
