from setuptools import setup


setup(
    name="grpc_types",
    version="0.1.0",
    description="gRPC interfaces",
    long_description="A package containing all proto buffer message and package definitions.",
    keywords="grpc",
    author="James Tarball <james.tarball@newtonsystems.co.uk>",
    author_email="james.tarball@newtonsystems.co.uk",
    url="https://github.com/newtonsystems/grpc_types",
    license="newtonsystems",
    packages=["grpc_types"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
)
