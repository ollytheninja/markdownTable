import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-markdown-table",
    version="0.3.3",
    author="hvalev",
    description="A package used to generate basic markdown tables from a list of dicts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hvalev/markdownTable",
    packages=['markdown_table'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
