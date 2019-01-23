class FrameworkInstance(object):

    def __init__(self, fr_name, fr_type, desc):
        self.fr_name = fr_name
        self.fr_type = fr_type
        self.desc = desc

    def __str__(self):
        return 'Framework: name = {0}, type = {1}, description = {2}'.format(self.fr_name, self.fr_type, self.desc)


class AppInfo2(object):

    def __init__(self, name, langs, frameworks, test_frameworks, build_tool, build_cmd, run_cmd):
        self.name = name
        self.langs = langs
        self.frameworks = frameworks
        self.test_frameworks = test_frameworks
        self.build_tool = build_tool
        self.build_cmd = build_cmd
        self.run_cmd = run_cmd

    def __init__(self):
        pass


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
