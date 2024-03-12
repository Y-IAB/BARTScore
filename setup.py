import setuptools

with open("BARTScore/README.md", "r") as fh:
  long_description = fh.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()
    install_requires = [ir.split("==")[0] for ir in install_requires]

setuptools.setup(
    name="BARTScore",  # Replace with your own username
    version="0.0.1",
    description="The BARTScore metric for Natural Language Generation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Y-IAB/BARTScore",
    packages=setuptools.find_packages(),
    py_modules=['bart_score'],
    license="Apache 2.0",
    python_requires=">=3",
    install_requires=install_requires)
