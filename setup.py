from setuptools import setup, find_packages

setup(
    name="app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.15.0",
        "httpx>=0.23.0", 
        "pydantic>=2.0.0",
        "pydantic-settings>=2.0.0",
        "sqlalchemy>=1.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
        ]
    },
)
