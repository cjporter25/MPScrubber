from setuptools import setup, find_packages


setup(
    name='mpscrubber',
    version='0.1',
    packages=find_packages(include=['Marketplace', 'Marketplace.*']),
    install_requires=[
        'attrs==23.1.0'
        'beautifulsoup4==4.12.2'
        'certifi==2023.7.22'
        'cffi==1.16.0'
        'chainmap==1.0.3'
        'charset-normalizer==3.3.2'
        'combomethod==1.0.12'
        'et-xmlfile==1.1.0'
        'greenlet==3.0.3'
        'h11==0.14.0'
        'idna==3.4'
        'nulltype==2.3.1'
        'openpyxl==3.1.2'
        'options==1.4.10'
        'outcome==1.3.0.post0'
        'packaging==23.2'
        'pycparser==2.21'
        'PyQt5==5.15.10'
        'PyQt5-Qt5==5.15.2'
        'PyQt5-sip==12.13.0'
        'PySocks==1.7.1'
        'python-dotenv==1.0.0'
        'requests==2.31.0'
        'selenium==4.16.0'
        'setuptools==70.0.0'
        'six==1.12.0'
        'sniffio==1.3.0'
        'sortedcontainers==2.4.0'
        'soupsieve==2.5'
        'SQLAlchemy==2.0.25'
        'trio==0.23.2'  
        'trio-websocket==0.11.1'
        'typing_extensions==4.9.0'
        'urllib3==2.1.0'
        'webdriver-manager==4.0.1'
        'wsproto==1.2.0',
        # Simply add other requirements if necessary in the future
    ],
    entry_points={
        'console_scripts': [
            'mpscrubber=main:main',
        ],
    },
)