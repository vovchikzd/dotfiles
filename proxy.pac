function FindProxyForURL(url, host) {
    if (
      dnsDomainIs(host, "www.instagram.com")
      || dnsDomainIs(host, "instagram.com")
      || dnsDomainIs(host, "www.human-nonhuman.info")
      || dnsDomainIs(host, "linktr.ee")
      || dnsDomainIs(host, "anilibria.tv")
      || dnsDomainIs(host, "anilibria.top")
      || dnsDomainIs(host, "tiktok.com")
      || dnsDomainIs(host, "x.com")
      || dnsDomainIs(host, "gosuslugi.ru")
      ) {
        return "SOCKS5 127.0.0.1:9150";
    }
}
