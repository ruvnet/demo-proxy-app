from setuptools import setup, find_packages

setup(
    name="app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.115.2",  # Latest stable FastAPI version
        "uvicorn>=0.30.0",   # Latest stable Uvicorn version
        "httpx>=0.23.0,<0.28.0",
        "pydantic>=2.9.0",   # Latest stable Pydantic version
        "pydantic-settings>=2.0.0",
        "sqlalchemy>=1.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0,<8.0.0",
            "pytest-cov>=4.0.0,<5.0.0",
            "black>=23.0.0,<24.0.0",
            "isort>=5.0.0,<6.0.0",
            "mypy>=1.0.0,<2.0.0",
        ]
    },
)