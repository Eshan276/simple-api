from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simple-api-framework",  # Choose a unique name
    version="0.1.0",
    author="Eshan Das",
    author_email="eshandas2002@gmail.com",
    description="A simple API framework for creating local APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eshan276/simple-api-framework",  # Your GitHub repo
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[],
    keywords="api, web, framework, localhost, simple",
)
