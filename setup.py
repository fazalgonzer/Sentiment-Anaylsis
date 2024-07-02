import setuptools

long_description="p orject where user can uploat list of reviwes or a review so th emodel can work on it "

__version__= "0.0.0.0"

REPO_NAME="Sentiment_Anaylsis"
AUTHOR_USER_NAME="fazal"
SRC_REPO ="Sentiment_Anaylsis"
AUTHOR_EMAIL ="fazslgonzer@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
