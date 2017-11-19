import csv
import pandas as pd
from itertools import chain

VARIATIONS = (('native.tcp', 'native.unix'),
              ('native.unix', 'docker.local.unix'),
              ('native.tcp', 'docker.local.tcp'),
              ('docker.local.tcp', 'docker.local.unix'),
              ('docker.local.tcp', 'docker.remote.tcp'),
              )

TEST_NAME = ("PING_INLINE",
             "PING_BULK",
             "SET",
             "GET",
             "INCR",
             "LPUSH",
             "RPUSH",
             "LPOP",
             "RPOP",
             "SADD",
             "HSET",
             "SPOP",
             "LPUSH (needed to benchmark LRANGE)",
             "LRANGE_100 (first 100 elements)",
             "LRANGE_300 (first 300 elements)",
             "LRANGE_500 (first 450 elements)",
             "LRANGE_600 (first 600 elements)",
             "MSET (10 keys)")

def read_csv(name):
    a = pd.read_csv('benchmark.{}.csv'.format(name),
                    names=('test', name))
    return a[name]

def main():
    for i,v in enumerate(VARIATIONS):
        df = pd.concat([read_csv(a) for a in v], axis=1)
        dfm = df.as_matrix()
        for i, raw in enumerate(dfm):
            print('|{}|{}|'.format(TEST_NAME[i], '|'.join(str(v) for v in raw)))
        df.plot.bar().get_figure().savefig('fig{}.png'.format(i))


if __name__ == '__main__':
    main()
