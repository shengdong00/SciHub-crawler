# SciHub-crawler

A crawler written in Python to automatically download papers from SciHub

一个用Python编写的爬虫，可以自动从SciHub下载论文.


The crawler is based on these packages: `pandas`, `selenium.webdriver`, `time`, `os`, `random`.

爬行器基于这些包：`pandas`、`selenium.webdriver`，`time`，`os`，`random`。


This is a script from my previous work for doing a mass literature review (about 800 papers). The document is [here](https://dong2000.xyz/post/crawl_papers_from_scihub/) on my blog website. Inputs needed are: first author names, publication years, DOI numbers. Here the data was extracted from Web of Science. You can modify this part for any other source.

这是我之前为了做大量文献（大约800篇论文）的综述而写的一份代码。文档见[此处](https://dong2000.xyz/post/crawl_papers_from_scihub/)。运行代码所需的输入包括：第一作者姓名、出版年份、DOI编号。这里的数据来自Web of Science，也可以是任何其他来源。


If successfully downloaded, the paper should be saved as: `No_xxx_Author_yyyy.pdf`, where `xxx` is paper number, `yyy` is publication year.

如果下载成功，论文应该被保存为：`No_xxx_Author_yyyy。pdf'，其中“xxx”是论文序号，“yyy”是出版年份。


**NOTE** that there are still bugs and the crawler is not 100% successful for [various reasons](https://dong2000.xyz/post/crawl_papers_from_scihub/#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9). Sometimes the renaming is wrong, yet to be fixed. Open to any corrections/suggestions.

**注意：**仍然存在bug，并且因为[各种问题](https://dong2000.xyz/post/crawl_papers_from_scihub/#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)，爬虫不是100%成功的。有时重命名是错误的，还没有修复。欢迎任何更正/建议。
