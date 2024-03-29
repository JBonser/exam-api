from setuptools import setup

setup(
    name="exam-api",
    version=0.1,
    packages=["app"],
    install_requires=[
        "dataclasses",
        "fastapi",
        "pkg-resources",
        "pydantic",
        "starlette",
        "SQLAlchemy",
        "alembic",
        "requests",
        "uvicorn",
        "bcrypt",
        "passlib[bscrypt]",
        "pytest",
        "pytest-cov",
        "python-multipart",
        "PyJWT",
    ],
)
