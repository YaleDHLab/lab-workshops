#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os, glob, codecs, json, urllib2, regex

"""
Notes: 

Blok: example of poetry page with collection of poems
Mayakovsky: example of poet page with direct links to poems
"""

def remove_punctuation(text):
  """Helper function to remove punctuation from an input text"""
  return regex.sub(ur"\p{P}+", "", text)


def get_poetry_page_links(html):
  """Read in the html from a poetry page and return an array of links"""
  clean_links = []

  html_soup = BeautifulSoup(html, 'html.parser')

  # remove the table of contents
  try:
    [e.extract() for e in html_soup.find("div", {"id": "toc"})]
  except:
    pass  


  # parse out the links
  for list_type in ["ol", "ul"]:
    ol_elements = html_soup.findAll(list_type)
    for ol_element in ol_elements:
      links = ol_element.findAll("a")
      for link in links:

        # links with .new class are not written, so skip them
        if link.has_attr("class"):
          if "new" in link["class"]:
            continue

        clean_links.append(link["href"])

  return clean_links


def parse_poem(poetry_page_index, poem_index, link, author_name):
  """Read in a link with form /wiki/link-to-poem and return plaintext from the poem"""

  try:
    full_link = root + link
    poem_response = urllib2.urlopen(full_link)
    poem_html     = poem_response.read()
    poem_soup     = BeautifulSoup(poem_html, 'html.parser')

    poem_container = get_poem_container(poem_soup)

    if poem_container:
      poem_text = get_poem_text(poem_container)
      poem_title = get_poem_title(poem_container)
      poem_date = get_poem_date(poem_container)

      # if the poem title contains "* * *", use the first line of the poem as the title
      if "* * *" in poem_title:
        for line in poem_text.split("\n"):
          if len(line) > 10:
            poem_title = "_".join(line.split())
            break
        print "replaced * * * title with", poem_title

      poem_title = remove_punctuation(poem_title)

      poem_metadata = {
        "id": poem_index,
        "title": poem_title,
        "date": poem_date,
        "link": root + link
      }

      outfile_name = author_name + "_" + "_".join(poem_title.split())

      # write the poem content to disk
      with codecs.open(outdir + "/txt/" + outfile_name + ".txt", "w", "utf-8") as outfile:
        outfile.write(poem_text)

      # write the metadata to disk
      with open(outdir + "/metadata/" + outfile_name + ".json", "w") as jsonout:
        json.dump(poem_metadata, jsonout)

  except Exception as exc:
    if failfast == 1:
      raise Exception(exc)

    print exc, poetry_page_index, poem_index, "".join(c for c in link if ord(c) < 128)
    

def get_poem_container(soup):
  """Read in the html from a wikisource poem and return soup with the poem's container"""
  poetry_table = soup.findAll("table", { "class" : "poetry" })
  center_table = soup.findAll("table", { "align" : "center" })

  for i in [poetry_table, center_table]:
    if len(i) == 1:
      return i[0]

  if failfast == 1:
    raise Exception("couldn't find a poem container")
  return


def get_poem_text(poem_container_soup):
  """Read in a soup object containing a poem and return the poem plaintext"""
  poem_text = ""
  poem_soup = poem_container_soup.findAll("div", { "class" : "poem" } )[0]

  for node in poem_soup.findAll('p'):
    poem_text += ''.join(node.findAll(text=True)) + "\n\n"
  
  return poem_text


def get_poem_title(poem_container_soup):
  """Read in a soup object containing a poem and return the poem's title"""
  poem_title = ""
  title_soup = poem_container_soup.findAll("span", { "class" : "mw-headline" } )[0]
  title = ''.join(title_soup.findAll(text=True))
  return title


def get_poem_date(poem_container_soup):
  """Read in a soup object containing a poem and return the poem's date"""
  try:
    date_soup = poem_container_soup.findAll("div", { "style" : "text-align:right" } )[0]
    date = ''.join(date_soup.findAll(text=True))
  except:
    date = "undated"
  return date


def make_outdirs():
  """Prepare the outfiles in which data will be stored"""
  if not os.path.exists(outdir):
    os.makedirs(outdir)

  for subdir in subdirs:
    new_dir = outdir + "/" + subdir
    if not os.path.exists(new_dir):
      os.makedirs(new_dir)


def get_poetry_pages():
  """Return an array of poetry pages to crawl"""
  poetry_pages = [
    
    {
      "path": "/wiki/Владимир_Владимирович_Маяковский",
      "author_name": "Mayakovsky"
    },

    {
      "path": "/wiki/Стихотворения_Блока_1897-1904",
      "author_name": "Blok"
    },

    {
      "path": "/wiki/Стихотворения_Блока_1904-1916",
      "author_name": "Blok"
    },

    {
      "path": "/wiki/Осип_Эмильевич_Мандельштам",
      "author_name": "Mandelshtam"
    },

    {
      "path": "/wiki/Стихотворения_1906-1920_(Цветаева)",
      "author_name": "Tsvetaeva"
    },

    {
      "path": "/wiki/Стихотворения_1921-1941_(Цветаева)",
      "author_name": "Tsvetaeva"
    },

    {
      "path": "/wiki/Алексей_Елисеевич_Кручёных",
      "author_name": "Kruchenykh"
    },

    {
      "path": "/wiki/Велимир_Хлебников",
      "author_name": "Khlebnikov"
    },

    {
      "path": "/wiki/Андрей_Белый",
      "author_name": "Bely"
    },

    {
      "path": "/wiki/Сергей_Александрович_Есенин/Стихотворения_1910—1915",
      "author_name": "Esenin"
    },

    {
      "path": "/wiki/Сергей_Александрович_Есенин/Стихотворения_1916—1923",
      "author_name": "Esenin"
    },

    {
      "path": "/wiki/Сергей_Александрович_Есенин/Стихотворения_1924—1925",
      "author_name": "Esenin"
    },

    {
      "path": "/wiki/Валерий_Яковлевич_Брюсов",
      "author_name": "Briusov"
    },

    {
      "path": "/wiki/Зинаида_Николаевна_Гиппиус",
      "author_name": "Gippius"
    },

    {
      "path": "/wiki/Константин_Дмитриевич_Бальмонт",
      "author_name": "Balmont"
    },

    {
      "path": "/wiki/Дмитрий_Сергеевич_Мережковский",
      "author_name": "Merezhkovsky"
    },

    {
      "path": "/wiki/Вячеслав_Иванович_Иванов",
      "author_name": "Ivanov"
    },

    {
      "path": "/wiki/Михаил_Алексеевич_Кузмин",
      "author_name": "Kuzmin"
    },

    {
      "path": "/wiki/Анна_Андреевна_Ахматова",
      "author_name": "Akhmatova"
    },

    {
      "path": "/wiki/Николай_Степанович_Гумилёв/Стихотворения_1902—1913",
      "author_name": "Gumilev"
    },

    {
      "path": "/wiki/Николай_Степанович_Гумилёв/Стихотворения_1914—1921",
      "author_name": "Gumilev"
    },

    {
      "path": "/wiki/Борис_Леонидович_Пастернак",
      "author_name": "Pasternak"
    },

    {
      "path": "/wiki/Фёдор_Кузьмич_Сологуб",
      "author_name": "Sologub"
    },

    {
      "path": "/wiki/Василий_Васильевич_Каменский",
      "author_name": "Kamensky"
    },

    {
      "path": "/wiki/Давид_Давидович_Бурлюк",
      "author_name": "Burliuk"
    },

    {
      "path": "/wiki/София_Яковлевна_Парнок",
      "author_name": "Parnok"
    }
    
  ]

  return poetry_pages


if __name__ == "__main__":

  # setting failfast to 1 will raise exceptions if parsing fails
  failfast = 0

  # specify the outfile locations
  outdir = "wikimedia_russian_texts"
  subdirs = ["txt", "metadata"]
  make_outdirs()

  # identify the domain to crawl
  root         = "https://ru.wikisource.org"
  poetry_pages = get_poetry_pages()

  for poetry_page_index, poetry_page in enumerate(poetry_pages):
    print "collecting from", poetry_page["path"]

    # start the request process
    response    = urllib2.urlopen(root + poetry_page["path"])
    html        = response.read()
    links       = get_poetry_page_links(html)
    print "found", len(links), "links"

    # fetch the content from each link
    for link_index, link in enumerate(links):
      parse_poem(poetry_page_index, link_index, link, poetry_page["author_name"])
