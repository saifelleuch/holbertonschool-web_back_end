#!/usr/bin/env python3
""" 5. Implementing an expiring web cache and tracker """
import redis
import requests
rds = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ uses the requests module to obtain
    the HTML content of a particular URL
    and returns it. """
    rds.set(f"cached:{url}", count)
    resp = requests.get(url)
    rds.incr(f"count:{url}")
    rds.setex(f"cached:{url}", 10, rds.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
