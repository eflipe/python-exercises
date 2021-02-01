url = 'www.codewars.com#about'


def remove_url_anchor(url):
    without_anchor = ''
    for let in url:
        if let == '#':
            break
        without_anchor += let

    return without_anchor

print(remove_url_anchor(url))


def remove_url_anchor(url):
  return url.split('#')[0]


def remove_url_anchor(url):
  try:
    return url[:url.index('#')]
  except:
    return url
