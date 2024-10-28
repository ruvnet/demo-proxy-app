from setuptools import setup, find_packages

setup(
    name="app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",  # Require newer FastAPI that supports Pydantic v2
        "uvicorn>=0.15.0",
        "httpx>=0.23.0", 
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
