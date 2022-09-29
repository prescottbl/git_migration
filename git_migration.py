#!/usr/bin/python3

import subprocess, os
import yaml


def yaml_parser(file_name):
    with open(file_name, "r") as yamlfile:
        yamldata = yaml.load(yamlfile)
    return yamldata

def git_to_git():
    for git_dir in git_list:
        root_path = "/home/bprescott/syncd/"
        git_path = root_path+git_dir
        print("Beginning process for {}.").format(git_dir)
        print("Changing Directory to {}.").format(git_path)
        if os.path.exists(git_path):
            os.chdir(git_path)
            if "hub" in subprocess.Popen(["git", "remote", "-v"]).context().wait():
                print("Pulling Changes from BitBucket.")
                subprocess.Popen(["git", "pull", "origin master"]).wait()
                print("Pushing Changes to GitHub.")
                subprocess.Popen(["git", "push", "hub master"]).wait()
            else:
                print("Adding GitHub Remote.")
                subprocess.Popen(["git", "remote", "add", "hub", git_remotes[git_dir][1]]).wait()
                print("Pulling Changes from BitBucket.")
                subprocess.Popen(["git", "pull", "origin", " master"]).wait()
                print("Pushing Changes to GitHub.")
                subprocess.Popen(["git", "push", "hub", "master"]).wait()
        else:
            os.chdir(root_path)
            subprocess.Popen(["git", "clone", git_remotes[git_dir][0]]).wait()
            print("Changing Directory to {}.").format(git_path)
            os.chdir(git_path)
            print("Adding GitHub Remote.")
            subprocess.Popen(["git", "remote", "add", "hub", git_remotes[git_dir][1]]).wait()
            print("Pushing Changes to GitHub.")
            subprocess.Popen(["git", "push", "hub", "master"]).wait()

if __name__ == "__main__":
    git_list = yaml_parser("./git_info.yaml")[git_info][git_repos]
    bb_remotes = yaml_parser("./git_info.yaml")[git_info][bitbucket_remotes]
    gh_remotes = yaml_parser("./git_info.yaml")[git_info][github_remotes]
    git_remotes = {}
    for git in git_list:
        for bb_remote in bb_remotes:
            for gh_remote in gh_remotes:
                git_remotes[git] = [bb_remote, gh_remote]
    git_to_git()




