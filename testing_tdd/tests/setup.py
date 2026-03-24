from setuptools import setup

setup(
   name='unique code',
   version='1.0',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   license='MIT',
   author='Asanov Denis',
   author_email='denisasanov67@gmail.com',
   packages=['mtracker'],
   install_requires=[],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
    url = 'https://github.com/denisasanov67-design/git-.git'
)