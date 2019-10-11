from setuptools import setup
import ii
 
setup(
    name = "ii",
    version = ii.__version__,
    keywords = "ii",
    author = "cilame",
    author_email = "opaquisrm@hotmail.com",
    license = "MIT",
    description = "my tools",
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
    ],
    packages = [
        "ii",
    ],
    package_data ={
        "ii":[
            'tcc-0.9.27-win32-bin.zip',
            'tcc-0.9.27-win64-bin.zip',
            'upx-3.95-32.zip',
            'upx-3.95-64.zip',
            'winapi-full-for-0.9.27.zip',
        ]
    },
    python_requires=">=3.5",
    entry_points={
        'console_scripts': [
            'ii = ii.init:init_all',
        ]
    },
)