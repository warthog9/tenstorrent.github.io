import os
import subprocess
import yaml


def build_doc(project, version):
    print(f"Building {project} {version}")
    os.environ[f"current_version"] = version
    if version == "latest":
        subprocess.run(f"cd {project} && make html", shell=True)
        return
    
    subprocess.run(f"git checkout {project}_{version}", shell=True)
    subprocess.run("git checkout main -- conf.py", shell=True)
    subprocess.run("git checkout main -- versions.yaml", shell=True)

    subprocess.run(f"cd {project} && make html", shell=True)

def move_dir(src, dst):
    subprocess.run(["mkdir", "-p", dst])
    subprocess.run("mv " + src + "* " + dst, shell=True)

os.environ["homepage"] = "https://tenstorrent.github.io/"

with open("versions.yml", "r") as yaml_file:
    subprocess.run("rm -rf output", shell=True)
    docs = yaml.safe_load(yaml_file)
    for project, versions in docs.items():
        for version in versions:
            build_doc(project, version)
            if project == "core" and version == "latest":
                # This is a special case to populate the root folder and home page
                move_dir(f"{project}/_build/html/", f"output/")
            else:    
                move_dir(f"{project}/_build/html/", f"output/{project}/{version}/")
            print(f"Built {project} {version}")
