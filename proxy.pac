function FindProxyForURL(url, host) {
    if (dnsDomainIs(host, "www.instagram.com") || dnsDomainIs(host, "www.human-nonhuman.info") || dnsDomainIs(host, "linktr.ee")) {
        return "SOCKS5 127.0.0.1:9150";
    }
}
