
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "ai-text-summarizator-"
AUTHOR_USER_NAME = "AyushKumarSD"
SRC_REPO = "AItextSummarization"
AUTHOR_EMAIL = "kayush@sandiego.edu"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An AI-powered text summarization package",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)



