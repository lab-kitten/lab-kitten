import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lab-kitten", 
    version="0.0.3",
    author="Ding Ruiqi",
    author_email="e0134117@u.nus.edu",
    description="lab-kitten",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lab-kitten",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)