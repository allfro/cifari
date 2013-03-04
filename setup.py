from setuptools import setup, find_packages

setup(
    name='cifari',
    author='Nadeem Douba',
    version='1.0',
    author_email='ndouba@gmail.com',
    description='CIFari Project',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari==0.7',
        'cif'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
