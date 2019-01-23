from os import walk

from enums.Language import Language
from models.AppInfo import AppInfo, FrameworkInstance
from util.api.api_utils import *
from util.reader import read_txt


def detect_app_info(url):
    if 'http' in url:
        print('Will scan project with provided GitHub url: ' + url)
        git_api_base_url = 'https://api.github.com/repos/'
        url.replace('https://github.com/', git_api_base_url)
        headers = {
            'user-agent': 'Listvin',
            'Content-Type': 'application/json'
        }
        repo_info = do_get('{0}qaprosoft/carina'.format(git_api_base_url), headers)
        langs = do_get('{0}qaprosoft/carina/languages'.format(git_api_base_url), headers)
        print('Repo info:')
        print(repo_info)

        print(langs)

        name = repo_info['name']
        print('Project name: ' + name.capitalize())
        runtimes = langs.keys()
        print('Used languages: ' + str(runtimes))
        frameworks = ''
        test_frameworks = ''
        build_tool = ''
        build_cmd = ''
        run_cmd = ''

        # app_info = AppInfo2.__init__()
    else:
        app_info = AppInfo(Language)
        print('Will scan project with provided path: ' + url)
        project_content = scan_folder(url)

        extensions = []
        for item in project_content:
            if '.' in item:
                extensions.append(item.split('.')[-1])
        extensions = set(extensions)
        print(extensions)
        app_info.runtime = define_runtimes(extensions)
        return app_info


def fetch_pom():
    

def define_framework():
    frameworks = []
    lines = read_txt('/Users/akratovich/projects/python/python_stud/resources/java_frameworks.txt')

    fr_type = ''
    desc = ''
    fr_name = ''
    for line in lines:
        if '###' in line:
            fr_type = line.split(' ')[1].strip()
        if line.count('*') == 2:
            desc = str(line.replace('*', ''))
        if '[' in line and ']' in line:
            fr_name = line.split('[')[1].split(']')[0]
        if fr_name:
            frameworks.append(FrameworkInstance(fr_name, fr_type, desc))


def define_runtimes(actual_extensions):
    supported_extentions = []
    langs = Language.values()
    for lang in langs:
        supported_extentions.append(lang.extention)

    langs = []
    for ext in actual_extensions:
        if ext in supported_extentions:
            langs.append(Language.define_by_extention(ext).name)
    print('Detected runtimes: ' + langs.__str__())
    return langs


def scan_folder(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        f.extend(dirnames)
        f.extend(filenames)
    return f


# detect_app_info('/Users/akratovich/projects/carina').__str__
# detect_app_info('https://github.com/qaprosoft/carina')
# define_framework()