""" This module contains code to check the version of a package """

import requests
import re

pypi_API_url = "https://pypi.org/pypi/%NAME%/json"

def check_package_name(name: str) -> bool:
    """
    Returns True if the given package name is a valid module name in Python and False otherwise
    """
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None


def sanatize_package_name(name: str) -> str:
    """ 
    Sanitize a given package name by removing invalid characters and replacing underscores with hyphens.

    :param str name: The package name to sanitize.
    :return str: The sanitized package name.
    """
    sanitized = re.sub(r'[^A-Za-z0-9_\-]', '', name)
    sanitized = sanitized.replace('_', '-')
    return sanitized.lower()


def get_pip_version(name: str) -> str:
    """ 
    Returns the name of the most recent version on PyPI.org or raises a ModuleNotFound Error 
    
    :param str name: The name of the package
    :returns str: Version string
    :raises ModuleNotFound: The package name is invalid or not registered at PyPI
    :raises 
    """
    global pypi_API_url
    if not check_package_name(name):
        raise ModuleNotFoundError(f"The given package name is invalid")
    name = sanatize_package_name(name)
    url = pypi_API_url.replace("%NAME%", name)

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except requests.RequestException as ex:
        raise ModuleNotFoundError()
    except (ValueError, KeyError) as ex:
        raise ModuleNotFoundError()