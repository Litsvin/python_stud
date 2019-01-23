from util.api import api_utils
from util.reader import get_config

git_api_base_url = 'https://api.github.com/repos/'
MAVEN = 'Maven'
POM = 'pom.xml'


def scan_project(url):
    if 'http' in url:
        print('Will scan project with following URL: ' + url)
        url = url.replace('https://github.com/', git_api_base_url)
        repo_content = get_root_content(url)
        name = define_project_name(url)
        build_tool = define_build_tool(repo_content)
        langs = define_programming_langs(url).keys()
        define_tech_stack(url, build_tool)

        # (name, langs, frameworks, test_frameworks, build_tool, build_cmd, run_cmd):


def define_tech_stack(url, build_tool):
    if 'http' in url:
        headers = {
            'user-agent': 'Listvin',
            'Authorization': 'token {0}'.format(get_config().get('git_token')),
            'accept': 'application/vnd.github.v3.raw'
        }
        if build_tool is MAVEN:
            build_file_name = POM
        modified_url = '{0}/contents/{1}'.format(url, build_file_name)
        response = api_utils.do_get(modified_url, headers)

        # for line in response:
        #     print("Pom's line: " + line + '/n')
        print(response)
        return response
    else:
        raise Exception("Scanning local repo isn't currently supported")


def define_project_name(url):
    if 'http' in url:
        headers = {
            'user-agent': 'Listvin',
        }
        response = api_utils.do_get(url, headers)
        name = response['name'].capitalize()
        print(name)
        return name
    else:
        raise Exception("Scanning local repo isn't currently supported")


def define_programming_langs(url):
    if 'http' in url:
        headers = {
            'user-agent': 'Listvin',
        }
        response = api_utils.do_get('{0}/languages'.format(url), headers)
        print(response)
        return response
    else:
        raise Exception("Scanning local repo isn't currently supported")


def define_build_tool(file_list):
    build_tool_name = ''
    for file in file_list:
        if POM in file['name']:
            build_tool_name = MAVEN
            print(build_tool_name)
            break
    if not build_tool_name:
        raise Exception('Unsupported build tool')
    return build_tool_name


def get_root_content(url):
    headers = {
        'user-agent': 'Listvin',
        'Authorization': 'token {0}'.format(get_config().get('git_token'))
    }
    response = api_utils.do_get('{0}/contents'.format(url), headers)

    # for line in response:
    #     print(str(line) + '/n')
    return response


scan_project('https://github.com/qaprosoft/carina')
