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
# #!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-06-09 02:41:50
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as ap:
        browser = await ap.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://web.archive.org/web/20200130202825/http://www.devttys0.com/2014/02/wrt120n-fprintf-stack-overflow/", timeout=300000)
        # take a screenshot
        await page.screenshot(path="sample_file.png")
        await page.pdf(path="sample_file.pdf")
        await browser.close()


await main()

# %%
