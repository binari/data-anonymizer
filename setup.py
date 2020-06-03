import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="",
    version="0.0.1",
    author="",
    author_email="",
    description="Anonimize data in SQL files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brbit/data-anonymizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6'
)
