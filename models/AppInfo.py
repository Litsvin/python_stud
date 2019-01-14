class AppInfo(object):

    def __init__(self, name, app_components, build_info):
        self.name = name
        self.app_components = app_components
        self.build_info = build_info

    def __init__(self):
        pass

    def __str__(self):
        print('=' * 10 + 'PROJECT DESCRIPTION' + '=' * 10)
        print('Project language: ' + self.runtime)


class BuildInfo:

    def __init__(self, build_tools, build_cmd):
        self.build_tools = build_tools
        self.build_cmd = build_cmd

    def __init__(self):
        pass


class AppComponents:

    def __init__(self, runtimes, frameworks, test_frameworks):
        self.runtimes = runtimes
        self.frameworks = frameworks  # should be a dict: lib_name : version
        self.test_frameworks = test_frameworks  # should be a dict: lib_name : version

    def __init__(self):
        pass
