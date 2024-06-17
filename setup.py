# import chardet
from setuptools import setup, find_packages

# DIDN'T WORK
# def read_requirements():
  #  with open('requirements.txt', 'rb') as f:
   #     raw_data = f.read()
    #    result = chardet.detect(raw_data)
    #    encoding = result['encoding']
    #    return raw_data.decode(encoding).splitlines()

setup(
    name='mpscrubber',
    version='0.2',
    # marketplace is currently the only required folder for the package
    packages=find_packages(include=['marketplace', 'marketplace.*']),
    # Retrieve python requirements list
    install_requires=["attrs==23.2.0",
                        "beautifulsoup4==4.12.3",
                        "build==1.2.1",
                        "certifi==2024.6.2",
                        "cffi==1.16.0",
                        "chainmap==1.0.3",
                        "chardet==5.2.0",
                        "charset-normalizer==3.3.2",
                        "colorama==0.4.6",
                        "combomethod==1.0.12",
                        "et-xmlfile==1.1.0",
                        "greenlet==3.0.3",
                        "h11==0.14.0",
                        "idna==3.7",
                        "installer==0.7.0",
                        "nulltype==2.3.1",
                        "openpyxl==3.1.4",
                        "options==1.4.10",
                        "outcome==1.3.0.post0",
                        "packaging==24.1",
                        "pip-review==1.3.0",
                        "pycparser==2.22",
                        "pyproject_hooks==1.1.0",
                        "PyQt5==5.15.10",
                        "PyQt5-Qt5==5.15.2",
                        "PyQt5-sip==12.13.0",
                        "PySocks==1.7.1",
                        "python-dotenv==1.0.1",
                        "requests==2.32.3",
                        "selenium==4.21.0",
                        "setuptools==70.0.0",
                        "six==1.16.0",
                        "sniffio==1.3.1",
                        "sortedcontainers==2.4.0",
                        "soupsieve==2.5",
                        "SQLAlchemy==2.0.30",
                        "trio==0.25.1",
                        "trio-websocket==0.11.1",
                        "typing_extensions==4.12.2",
                        "urllib3==2.2.2",
                        "webdriver-manager==4.0.1",
                        "wheel==0.43.0",
                        "wsproto==1.2.0",],
    # Main script is located in primary directory as "main.py"
    entry_points={
        'console_scripts': [
            'mpscrubber=main:main',
        ],
    },
)