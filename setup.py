from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='upfrontsystems.q',
      version=version,
      description="Lightweight queue on Redis.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Upfront Systems',
      author_email='rijk@upfrontsystems.co.za',
      url='git@github.com:upfrontsystems/q.git',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upfrontsystems'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pyga',
          'redis',
          'rq',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      processqueue=upfrontsystems.q.scripts.queueprocessor:processqueue
      """,
      )
