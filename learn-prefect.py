#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2024-12-25 00:21:41
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import httpx

from prefect import flow, task


@task
def fetch_stats(github_repo: str):
    # fetch the stats from the GitHub API

    return httpx.get(f"https://api.github.com/repos/{github_repo}").json()


@task
def get_stars(repo_stats: dict):
    # extract the number of stars from the API response

    return repo_stats["stargazers_count"]


@flow(log_prints=True)
def show_stars(repos: list[str]):
    for repo in repos:
        stats = fetch_stats(repo)
        stars = get_stars(stats)
        print(f"The {repo} repository has {stars} stars")


if __name__ == "__main__":
    show_stars(["PrefectHQ/prefect", "ethic41/fingerprint"])
