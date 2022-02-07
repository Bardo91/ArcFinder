import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ArcFinder",
    version="0.0.1",
    author="Bardo91",
    author_email="pabramsor@gmail.com",
    description="App to scrap realstate houses and flats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "ArcFinder"},
    packages=setuptools.find_packages(where="ArcFinder"),
    python_requires=">=3.6",
)