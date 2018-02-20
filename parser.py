#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree


route_author="/dblpperson/person/author"
route_coauthor="/dblpperson/r/article/author"
route_title ="/dblpperson/r/article/title"
route_pages ="/dblpperson/r/article/page"
route_article="/dblpperson/r/article"


tree = etree.parse("auteurs/Fabregat.xml")


#file = autheur
def get_article(File):
    List = []
    tree = etree.parse(File)
    for user in tree.xpath(route_author):
        List.append(user.text)
    return List
    


if __name__ == '__main__':


    tree = etree.parse("auteurs/Fabregat.xml")
    print("authore")
    for user in tree.xpath(route_author):
        print(user.text)

    print("coauthore")
    for user in tree.xpath(route_coauthor):
        print(user.text)
    print("titre")
    for user in tree.xpath(route_title):
        print(user.text)
