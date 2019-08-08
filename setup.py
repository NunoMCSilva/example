import setuptools


def read(fname: str) -> str:
    with open(fname) as fp:
        return fp.read()


setuptools.setup(
    name="example2-pkg-blackcat",
    version="0.0.2",
    author="Nuno Miguel Casteloa da Silva",
    author_email="NunoMCSilva@gmail.com",
    description="A small example package",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/NunoMCSilva/example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
