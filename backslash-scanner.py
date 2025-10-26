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
# @Date    : 2024-10-25 20:10:44
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0
# @About   : Notebook on learning about backslash powered scanner



# %% [markdown]
# # Backslash Scanner
#
# ## Probe pair fuzzing
#
# ![probe pair fuzzing](diffing.png)
#
# ## Alternate probe-pairs
#
# ```bash
# ' vs \' // single-quoted string
# ' vs '' // single-quoted string (alternative escaping)
# " vs \" // double-quoted string
# 7/0 vs 7/1 // number
# ${{ vs $}} // interpolation
# /**/ vs /*/ // raw code
# ,99 vs ,1 // order-by
# sprintz vs sprintf // function name 
#
# ```
#
# 1. first identify the types of quotes in use
# 2. then the concatenation sequence
# 3. then identify whether function calls are possible
# 4. then send a sequence of language specific function in attempt to identify the backend language
