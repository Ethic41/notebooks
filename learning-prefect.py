# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2024-12-25 00:18:10
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


import httpx

from prefect import flow, task # Prefect flow and task decorators


@flow(log_prints=True)
def show_stars(github_repos: list[str]):
    """Flow: Show the number of stars that GitHub repos have"""

    for repo in github_repos:
        # Call Task 1
        repo_stats = fetch_stats(repo)

        # Call Task 2
        stars = get_stars(repo_stats)

        # Print the result
        print(f"{repo}: {stars} stars")


@task
def fetch_stats(github_repo: str):
    """Task 1: Fetch the statistics for a GitHub repo"""

    return httpx.get(f"https://api.github.com/repos/{github_repo}").json()


@task
def get_stars(repo_stats: dict):
    """Task 2: Get the number of stars from GitHub repo statistics"""

    return repo_stats['stargazers_count']


# Run the flow
if __name__ == "__main__":
    show_stars([
        "PrefectHQ/prefect",
        "pydantic/pydantic",
        "huggingface/transformers"
    ])



# %%
