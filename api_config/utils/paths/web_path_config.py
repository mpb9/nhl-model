from enum import Enum, unique


# MARK: WebPage
@unique
class WebPage(Enum):
    HOME = "/api"
    TOC = HOME + "/paths"
    GLOSSARY = HOME + "/glossary"


# MARK: WebPageHtml
@unique
class WebPageHtml(Enum):
    HOME = "pages/home.html"
    TOC = "pages/toc.html"
    GLOSSARY = "pages/glossary.html"
