from setuptools import setup, find_packages

with open("README.md", "r") as fileObj:
    longDescription = fileObj.read()

setup(
    name="PyWatermark",
    packages=find_packages(),
    version="0.1.0",
    author="Ieshaan Saxena",
    author_email="ieshaan1999@gmail.com",
    description="A library to watermark your images easily.",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/ieshaan12/watermark",
    download_url="",
    include_package_data=True,
    package_data={'PyWatermark': ['fonts/*.ttf']},
    install_requires = [
        'Pillow >= 7.2.0',
        'os'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
