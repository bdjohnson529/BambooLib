import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BambooLib-bdjohnson529", # Replace with your own username
    version="0.0.1",
    author="Ben Johnson",
    description="Data analysis in Python and SQL",
    url="https://github.com/bdjohnson529/BambooLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires =	['pandas>=1.0.1',
						'numpy>=1.18.1',
						'pyodbc>=4.0.0',
						'scikit-learn>=0.22.1',
                        'usaddress-scourgify>=0.2.3'
	]
)