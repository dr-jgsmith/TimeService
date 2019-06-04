from setuptools import setup

setup(name='TimeService',
      version='0.02',
      description='Toolkit for computing with hypergraphs and hypernetworks',
      classifiers=[
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7.3',
          'Topic :: Time',
      ],
      author='Justin G. Smith',
      author_email='justingriffis@wsu.edu',
      license='MIT',
      packages=['TimeService'],
      include_package_data=True,
      zip_safe=False)
