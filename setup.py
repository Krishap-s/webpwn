import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webpwn",
    version="0.0.1",
    author="Krishap",
    description="Web exploit development library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Krishap-s/webpwn",
    project_urls={
        "Bug Tracker": "https://github.com/Krishap-s/webpwn/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
