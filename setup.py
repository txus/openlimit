import sys
from setuptools import setup

setup(
    name="openlimit",
    description="Rate limiter for the OpenAI API",
    version="v0.2.8",
    packages=["openlimit", "openlimit.utilities", "openlimit.buckets"],
    python_requires=">=3",
    url="https://github.com/shobrook/openlimit",
    author="shobrook",
    author_email="shobrookj@gmail.com",
    # classifiers=[],
    install_requires=["aioredis", "tiktoken"],
    keywords=["openai", "rate-limit", "limit", "api", "request", "token", "leaky-bucket", "gcra", "redis", "asyncio"],
    license="MIT"
)
