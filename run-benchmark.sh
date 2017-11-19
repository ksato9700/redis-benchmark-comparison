#!/bin/sh

run_benchmark="redis-benchmark -q --csv"

# run test on local native redis (tcp socket)
${run_benchmark} > benchmark.native.tcp.csv

# run test on local native redis (unix socket)
${run_benchmark} -s /tmp/redis.sock > benchmark.native.unix.csv
