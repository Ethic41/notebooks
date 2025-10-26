# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: notebooks
#     language: python
#     name: python3
# ---

# %%
# #!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-08-02 18:09:10
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

from PyPDF2 import PdfReader
from docx import Document

# %%
reader = PdfReader("sample_file.pdf")
number_of_pages = len(reader.pages)

print(f"Number of pages in PDF: {number_of_pages}")

# %%
page = reader.pages[0]
text = page.extract_text()
print(f"Text from the first page: {text}")

# %%
