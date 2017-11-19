FROM redis:latest
COPY redis.conf /usr/local/etc/redis.conf
ENTRYPOINT ["redis-server", "/usr/local/etc/redis.conf"]
