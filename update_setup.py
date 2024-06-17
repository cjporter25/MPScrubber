# Test script to automate updating the setup installs list.

import re

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()

def update_setup(install_requires):
    with open('setup.py', 'r') as f:
        setup_content = f.read()

    new_install_requires = "install_requires=[\n        " + ",\n        ".join(f"'{pkg}'" for pkg in install_requires) + "\n    ],"

    updated_setup_content = re.sub(
        r"install_requires=\[(.*?)\],",
        new_install_requires,
        setup_content,
        flags=re.DOTALL
    )

    with open('setup.py', 'w') as f:
        f.write(updated_setup_content)

if __name__ == "__main__":
    install_requires = read_requirements()
    update_setup(install_requires)