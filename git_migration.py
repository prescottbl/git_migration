#!/usr/bin/python3

import subprocess, os
import yaml

def yaml_parser(file_name):
    with open(file_name, "r") as yamlfile:
        yamldata = yaml.load(yamlfile, Loader=yaml.FullLoader)
    return yamldata

def git_to_git():
    for git_dir in git_list:
        git_path = root_path+git_dir
        print(f"\nBeginning process for {git_dir}.\n")
        if os.path.exists(git_path):
            print(f"Changing Directory to {git_path}.")
            os.chdir(git_path)
            git_check = subprocess.check_output(["git", "remote", "-v"])
            print(str(git_check))
            if "hub" in str(git_check):
                print("Pulling Changes from BitBucket.")
                subprocess.Popen(["git", "pull", "origin", "master"]).wait()
                print("Pushing Changes to GitHub.")
                subprocess.Popen(["git", "push", "hub", "master"]).wait()
            else:
                print("Adding GitHub Remote.")
                subprocess.Popen(["git", "remote", "add", "hub", git_remotes[git_dir]["gh_url"]]).wait()
                print("Pulling Changes from BitBucket.")
                subprocess.Popen(["git", "pull", "origin", " master"]).wait()
                print("Pushing Changes to GitHub.")
                subprocess.Popen(["git", "push", "hub", "master"]).wait()
        else:
            os.chdir(root_path)
            subprocess.Popen(["git", "clone", git_remotes[git_dir]["bb_url"]]).wait()
            print(f"Changing Directory to {git_path}.")
            os.chdir(git_path)
            print("Adding GitHub Remote.")
            subprocess.Popen(["git", "remote", "add", "hub", git_remotes[git_dir]["gh_url"]]).wait()
            print("Pushing Changes to GitHub.")
            subprocess.Popen(["git", "push", "hub", "master"]).wait()
        print(f"Fetching and pushing tags and other branches for {git_dir}.")
        subprocess.Popen(["git", "push", "hub", "'refs/remotes/origin/*:refs/heads/*'"]).wait()
        subprocess.Popen(["git", "fetch", "origin", "--tags"]).wait()
        subprocess.Popen(["git", "push", "hub", "--tags"]).wait()

if __name__ == "__main__":
    git_remotes = yaml_parser("./git_info.yaml")["git_repos"]
    git_list = list(git_remotes.keys())
    root_path = yaml_parser("./git_info.yaml")["globals"]["root_directory"]
    git_to_git()
