import os, subprocess, json
from pathlib import Path


REQUIRED_PYTHON_VERSION = '3.10'


def generate_root_path() -> str:
    current_dir = os.getcwd()
    print(f'currently in {current_dir} directory')

    pwd = subprocess.check_output(['pwd'])
    path = pwd.decode('utf-8')

    parts = path.split('/')
    username = parts[2]

    dir_path = f'/Users/{username}'

    return dir_path

def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=False)
    print(f'directory created: {dir_path}')

    return

def install_poetry():
    '''
    installs `poetry` - package manager for python
    '''

    os.system('brew install poetry')
    poetry_version = subprocess.check_output(['poetry', '--version']).decode('utf-8')

    print()
    print(f'{poetry_version} installed!')

    return poetry_version

def install_python():
    '''
    installs `python` - programming language used in raw
    '''

    os.system(f'brew install python@{REQUIRED_PYTHON_VERSION}')
    python_version = subprocess.check_output(['python3', '--version']).decode('utf-8')

    print()
    print(f'{python_version} installed!')

def install_pipx():
    '''
    installs `pipx`
    '''

    os.system(f'brew install pipx')
    pipx_version = subprocess.check_output(['pipx', '--version']).decode('utf-8')

    print()
    print(f'{pipx_version} installed!')

    return pipx_version

def clone_repo(clone_to):
    '''
    clone repo from GitHub
    '''

    os.chdir(clone_to)
    os.system(f'git clone https://github.com/dvodnenko/raw.git .')

    print()
    print('repo cloned!')

    os.system(f'poetry env use python{REQUIRED_PYTHON_VERSION}')
    os.system('source .venv/bin/activate')
    os.system('poetry install')

    os.chdir(clone_to)
    os.system('pwd')

def create_data_file(root_dir):

    if Path(f'{root_dir}/.rawdata.json').exists():
       return

    os.chdir(root_dir)
    os.system('touch .rawdata.json')

    basic_data = {
        'tags': [],
        'active_session': {},
        'sessions': []
    }

    with open(f'{root_dir}/.rawdata.json', 'w', encoding='utf-8') as file:
        json.dump(basic_data, file, ensure_ascii=False, indent=4)

def install_via_pipx(raw_dir):
    os.chdir(raw_dir)

    os.system('pipx uninstall raw')
    os.system('pipx install .')


def install():

    # creating /raw directory that will store raw
    dir_path = input('enter path to the folder(press enter to use ~/Documents):')
    root_path = generate_root_path()
    if dir_path == '':
        dir_path = f'{root_path}/Documents'

    if not Path(dir_path).exists():
        print(f'Such folder does not exist: {dir_path}')
        exit(1)
        return
    
    raw_dir_path = f'{dir_path}/raw'

    create_directory(raw_dir_path)

    # install poetry, python and pipx
    install_python()
    poetry_version = install_poetry().strip()
    pipx_version = install_pipx().strip()

    # clone repo
    clone_repo(clone_to=raw_dir_path)

    create_data_file(root_path)

    os.chdir(raw_dir_path)

    with open('src/raw/data.py', 'r', encoding='utf-8') as file:
        content = file.readlines()

    del content[0]

    with open('src/raw/data.py', 'w', encoding='utf-8') as file:
        file.write(f"DATA_PATH = '{root_path}/.rawdata.json'")
    
    with open('src/raw/data.py', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.writelines(content)

    install_via_pipx(raw_dir_path)

    os.system('clear')

    print(f'✅created directory for raw: {raw_dir_path}')
    print(f'✅installed python: python@{REQUIRED_PYTHON_VERSION}')
    print(f'✅installed poetry: {poetry_version}')
    print(f'✅installed pipx: {pipx_version}')
    print(f'✅cloned raw repo')
    print(f'✅created data file ({root_path}/.rawdata.json)')


install()
