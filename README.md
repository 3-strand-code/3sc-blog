[3sc-blog](blog.3strandcode.com)
========

## Install

```
pip install -r requirements.txt
npm install
```

## Start

```
npm start
```
>live reload included

## Write

Place your article in the `content/` folder with the following format at the top:

```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

Article content

# A heading

More content
```

>(more details on writing articles can be found [here](http://docs.getpelican.com/en/3.6.3/content.html))


## Publish

```
make github
```
