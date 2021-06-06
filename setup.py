import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()
    

setuptools.setup(
    name="suresh_package",
    version="0.0.1",
    author="Suresh Abeyweera",
    author_email="suresh.abeyweera@gmail.com",
    description="A small mathematics library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suresh-abeyweera/suresh_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: python ::3",
        "Licence :: OSI Approved :: MIT Licence",
        "Opearating System :: OS Independent",
    ],
    python_requires'>=3.6',
)