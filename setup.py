import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="ReetKapoor"
SRC_REPO="TextSummarizer"
AUTHOR_EMAIL="reetkapoor29-1@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for NLP app.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
    
    