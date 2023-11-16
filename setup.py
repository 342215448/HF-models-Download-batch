from time import time
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="niu_download",
    version="0.0.1",
    author="Peinan Feng & Junhao Ruan & Peizhuo Liu (NEUNLPLAB)",
    author_email="fpnan@foxmail.com",
    description="A tool that can download Hugging Face model(s)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/342215448/SaoDownload.git",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    packages=setuptools.find_packages(where="src"),
    install_requires=[
            "requests",
            "tqdm",
            "Beautifulsoup4",
        ],
    entry_points={
            "console_scripts": [
                "niu-download = sao_download.download:cli_main",
            ],
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},

    python_requires=">=3.6",
)
