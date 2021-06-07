from setuptools import setup

setup(
    name='aideqc',
    version='0.0.1',    
    description='Hello World',
    url='http://docs.aide-qc.org',
    author='Alex McCaskey',
    author_email='mccaskeyaj@ornl.gov',
    license='BSD 3-clause, EPL, EDL',
    packages=['aideqc'],
    install_requires=['docker-py',
                      'docker', 'tqdm', 'webbrowser', 'tabulate', 'argcomplete'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)