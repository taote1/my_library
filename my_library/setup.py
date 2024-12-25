from setuptools import setup, find_packages

setup(
    name="my_library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    tests_require=["unittest"],
    test_suite="tests",
    author="Ваше имя",
    author_email="zz2846630@gmail.com",
    description="Пример библиотеки с математическими операциями",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/taote1/my_library",
)
 
