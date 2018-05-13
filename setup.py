from setuptools import setup, find_package

setup(name='sincerity',
      version='0,3',
      url='https://github.com/riemannulus/sincerity',
      license='CPOL',
      author='riemannulus',
      author_email='riemannulus@hitagi.moe',
      description='Recognized recoding sound',
      packages=find_package(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
