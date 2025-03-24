import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="miligrad",
    version="0.1.0",
    author="Vaibhav Pandey",
    author_email="vaifaipandey1996@gmail.com",
    description="A tiny scalar-valued autograd engine inspired from Andrej Karpathy's micrograd with a small PyTorch-like neural network library on top with some added functionalities ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaifai/miligrad",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
