class AppInfo(object):

    def __init__(self, runtime):
        self.runtime = runtime

    def __str__(self):
        print('=' * 10 + 'PROJECT DESCRIPTION' + '=' * 10)
        print('Project language: ' + self.runtime)
