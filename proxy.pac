function FindProxyForURL(url, host) {
    if (
      dnsDomainIs(host, "www.instagram.com")
      || dnsDomainIs(host, "instagram.com")
      || dnsDomainIs(host, "www.human-nonhuman.info")
      || dnsDomainIs(host, "linktr.ee")
      || dnsDomainIs(host, "anilibria.top")
      || dnsDomainIs(host, "gosuslugi.ru")
      || dnsDomainIs(host, "tr.anidub.com")
      || dnsDomainIs(host, "rutracker.org")
      || dnsDomainIs(host, "gramsnap.com")
      || dnsDomainIs(host, "fansly.com")
      || dnsDomainIs(host, "imdb.com")
      || dnsDomainIs(host, "goodreads.com")
      ) {
        return "SOCKS5 127.0.0.1:9150";
    }
}
