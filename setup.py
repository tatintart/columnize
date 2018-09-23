import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='columnize',
    version='0.1',
    description='List things in columns',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='console list',
    author='Xavier Lepaul',
    author_email='xavier@lepaul.fr',
    license='MIT',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        # 3.3 required for shutil.get_terminal_size
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'columnize=columnize:command',
        ],
    },
)
