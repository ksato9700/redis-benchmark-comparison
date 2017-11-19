docker-compose build 
docker-compose up -d
sleep 5

run_benchmark_local="docker exec -it redis redis-benchmark -q --csv"

# run test on local docker redis (tcp socket)
${run_benchmark_local} > benchmark.docker.local.tcp.csv

# run test on local docker redis (unix socket)
${run_benchmark_local} -s /tmp/redis.sock > benchmark.docker.local.unix.csv

run_benchmark_remote="docker exec -it redis_benchmark redis-benchmark -q --csv"

# run test on remote docker redis (tcp socket)
${run_benchmark_remote} -h redis > benchmark.docker.remote.latest.csv

# run test on remote docker redis (tcp socket)
${run_benchmark_remote} -h redis_alpine > benchmark.docker.remote.alpine.csv

