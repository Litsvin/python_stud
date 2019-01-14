from os import walk

from enums.Language import Language
from models.AppInfo import AppInfo


def detect_app_info(url):
    app_info = AppInfo(Language)
    if 'http' in url:
        print('Will scan project with provided url: ' + url)
    #     nothing's here for now
    else:
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


detect_app_info('/Users/akratovich/projects/carina').__str__
