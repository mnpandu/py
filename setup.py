# setup.py
from setuptools import setup, find_packages

setup(
    name='secretsutil',
    version='0.1.0',
    description='Reusable Fernet-based encryption utility for managing encrypted credentials',
    author='Your Name or Team',
    packages=find_packages(),
    install_requires=[
        'cryptography>=41.0.0',
        'python-dotenv>=1.0.0'
    ],
    python_requires='>=3.7',
)
