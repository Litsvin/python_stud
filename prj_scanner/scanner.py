from os import walk

from enums.Language import Language, Runtime
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
    app_info.runtime = define_runtime(extensions)

    return app_info


def define_runtime(extensions):
    lang_list = []
    for lang in Language.values():
        for ext in extensions:
            if ext == Runtime.extention:
                lang_list.append()
    # for ext in extensions: lang. in Language.values()




    for ext in extensions:
        if ext in Language.values():
            lang_list.append(ext)
    return lang_list


def scan_folder(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        f.extend(dirnames)
        f.extend(filenames)
    return f


detect_app_info('/Users/akratovich/projects/carina').__str__
