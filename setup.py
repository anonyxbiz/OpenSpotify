from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="wazing_net",
    version="1.0.8",
    description="Wazing_net - Fast and easy access to request methods just like requests",
    author="Anonyxbiz",
    author_email="biz@anonyxis.life",
    url="https://github.com/anonyxbiz/wazing_net",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['wazing_net'],
    python_requires='>=3.6',
)
