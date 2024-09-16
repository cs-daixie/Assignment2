import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict
from platform import python_version
from packaging.version import Version

min_version = '3.9.0'

def check_python_version():
    cur_version = python_version()
    print('Your python version is ', cur_version)
    assert Version(cur_version) >= Version(min_version), 'Make sure you use python version >=' + min_version

def check_env_setup():
    dependencies = open("requirements.txt").readlines()
    try:
        pkg_resources.require(dependencies)
        print("✅ ALL GOOD")
    except DistributionNotFound as e:
        print("⚠️ Library is missing")
        print(e)
    except VersionConflict as e:
        print("⚠️ Library version conflict")
        print(e)
    except Exception as e:
        print("⚠️ Something went wrong")
        print(e)

if __name__ == '__main__':
    check_python_version()
    check_env_setup()