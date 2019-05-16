import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
     name='sec',  
     version='0.1',
     scripts=['sec'] ,
     author="Daniel Goldszmit",
     author_email="daniel.goldszmit@gmail.com",
     description="Utility methodos do secure a dataframe",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/daniegoldszmit/sec",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.6",
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.2",
         "Programming Language :: Python :: 3.3",
         "Programming Language :: Python :: 3.4",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
