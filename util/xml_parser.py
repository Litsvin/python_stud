import xml.etree.ElementTree as xml

from enums.Language import Language


def parse_pom(pom_path):
    namespaces = {'xmlns': 'http://maven.apache.org/POM/4.0.0'}

    tree = xml.parse(pom_path)
    root = tree.getroot()

    name = root.find(".//xmlns:artifactId", namespaces=namespaces).text.capitalize()

    dependencies = root.findall(".//xmlns:dependency", namespaces=namespaces)
    artifacts = {}

    for dependency in dependencies:
        artifact_id = dependency.find("xmlns:artifactId", namespaces=namespaces).text
        version = dependency.find("xmlns:version", namespaces=namespaces).text
        version = version if ('${' not in version) else 'not set'
        artifacts[artifact_id] = version

    artifact_names = artifacts.keys()

    runtimes = {}

    for ar_name in artifact_names:
        if 'java' in ar_name:
            runtimes[Language.JAVA] = artifacts.get(ar_name)
        if 'jython' in ar_name:
            runtimes[Language.PYTHON] = artifacts.get(ar_name)

    print('=' * 80)
    print('App name: ' + name)

    print('=' * 80)
    for key, value in runtimes.items():
        print('Runtime: %s; version: %s' % (key, value))

    print('=' * 80)
    for key, value in artifacts.items():
        print('Artifact: %s; version: %s' % (key, value))
    print('=' * 80)


parse_pom('../resources/pom.xml')
