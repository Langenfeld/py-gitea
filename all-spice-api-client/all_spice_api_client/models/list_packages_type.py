from enum import Enum


class ListPackagesType(str, Enum):
    COMPOSER = "composer"
    CONAN = "conan"
    CONTAINER = "container"
    GENERIC = "generic"
    HELM = "helm"
    MAVEN = "maven"
    NPM = "npm"
    NUGET = "nuget"
    PUB = "pub"
    PYPI = "pypi"
    RUBYGEMS = "rubygems"
    VAGRANT = "vagrant"

    def __str__(self) -> str:
        return str(self.value)
