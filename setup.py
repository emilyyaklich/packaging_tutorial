import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-emilyyaklich", # distribution name of package
    version="0.0.1", # version of the package
    author="Emily Yaklich", # author of package           
    author_email="emily.yaklich@gmail.com", # author email
    description="A small example package", # short one-sentence description
    long_description=long_description, # detailed description of package,README
    long_description_content_type="text/markdown", # markup used
    url="https://github.com/emilyyaklich/example_package", # homepage of project
    packages=setuptools.find_packages(), #list of all import packages in dist.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # give index and pip metadata about the package
    python_requires='>=3.6',
)
