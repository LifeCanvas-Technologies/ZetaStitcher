from setuptools import setup, find_packages

setup(
    name='zetastitcher',
    version='1.0.0',
    author='Giacomo Mazzamuto',
    author_email='mazzamuto@lens.unifi.it',
    description='ZetaStitcher is a tool designed to stitch large '
                 'volumetric images such as those produced by Light-Sheet '
                 'Fluorescence Microscopes.',
    packages=find_packages(exclude=('tests', 'scripts')),
    install_requires = [
        "cachetools==5.5.2",
        "coloredlogs==15.0.1",
        "cvxpy==1.6.2",
        "humanize==4.12.1",
        "imageio==2.37.0",
        "numpy==1.26.4",
        "networkx==3.4.2",
        "opencv-python==4.11.0.86",
        "pandas==2.2.3",
        "pims==0.7",
        "psutil==7.0.0",
        "pyyaml==6.0.2",
        "qpsolvers==4.5.0",
        "scipy==1.11.1",
        "tifffile==2025.2.18",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'stitch-align = zetastitcher.align.aligner:main',
            'stitch-fuse = zetastitcher.fuse.__main__:main',
            'stitch-downscale = zetastitcher.scripts.stitch_downscale:main',
        ]
    },
    license='GPLv3+',
    url="https://github.com/LifeCanvas-Technologies/ZetaStitcher"
)
