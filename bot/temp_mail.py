import email
import sys

import redis

from bot import settings


def main():
    r = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
    )
    msg = email.message_from_file(sys.stdin)
    print(msg)
    print(msg.items())
    r.set('foo', msg)
    print(r.get('foo'))


if __name__ == '__main__':
    main()
