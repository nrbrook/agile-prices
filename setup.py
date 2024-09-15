from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Octopus Agile Price Fetcher'
LONG_DESCRIPTION = 'Python scripts to fetch agile prices from Octopus'

# Setting up
setup(
        name="agile-prices", 
        version=VERSION,
        author="Nick Brook",
        author_email="nrbrook@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'octopus', 'agile'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)