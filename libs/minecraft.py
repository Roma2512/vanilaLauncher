from minecraft_launcher_lib import *
import os, shutil

versions = {"magic": {"version": "1.12.2", "loader": "forge", "icon": "", "name": "Магия"},
            "pidro": {"version": "1.20.1", "loader": "forge", "icon": "", "name": "пидро"}}

def install_ver(id: str, callback: dict):
    version = versions[id]

    if os.path.isdir(f"minecraft/{id}"):
        shutil.rmtree(f"minecraft/{id}")
    else:
        os.mkdir(f"minecraft/{id}")

    match version["loader"]:
        case "forge":
            forge.install_forge_version(forge.find_forge_version(version["version"]), f"minecraft/{id}", callback=callback)
        case "fabric":
            fabric.install_fabric(version["version"], f"minecraft/{id}", callback=callback)
        case "vanilla":
            install.install_minecraft_version(version["version"], f"minecraft/{id}", callback=callback)

def getVersionList():
    result = []
    for version in versions.values():
        result.append(version)
    return result
def getVersions():
    return versions