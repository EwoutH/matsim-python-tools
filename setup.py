import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
VERSION = (HERE / "VERSION").read_text()

# This call to setup() does all the work
setup(
    version=VERSION,
    name="matsim-tools",
    description="MATSim Agent-Based Transportation Simulation Framework - official python tools",
    long_description_content_type="text/markdown",
    url="https://github.com/matsim-vsp/matsim-python-tools",
    author="VSP-Berlin",
    author_email="charlton@tu-berlin.de",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
    ],
    packages=["matsim", "matsim.pb"],
    install_requires=[
        "protobuf >= 3.10.0",
        "xopen",
        "pandas",  # "shapely", "geopandas >= 0.6.0"
    ],
    extras_require={
        'calibration': ["optuna >= 2.7.0"],
        'scenariogen': ["sumolib", "traci", "lxml", "optax", "requests", "tqdm", "sklearn", "xgboost", "lightgbm",
                        "sklearn-contrib-lightning", "numpy", "sympy"]
    },
    tests_require=["assertpy", "pytest"],
    entry_points={
        'console_scripts': [
            'matsim-tools=matsim.cli.main:main',
            'matsim-scenariogen=matsim.scenariogen:main'
        ]
    },
    long_description=README,
)
