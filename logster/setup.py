import setuptools

setuptools.setup(
    name="logster",
    packages=setuptools.find_packages(exclude=["logster_tests"]),
    install_requires=[
        "dagster==0.14.15",
        "dagit==0.14.15",
        "pytest",
    ],
)
