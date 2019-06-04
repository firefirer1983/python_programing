#!/usr/bin/env python3
# @Author  : xy.zhang
# @Email   : zhangxuyi@wanshare.com
# @Time    : 19-6-3


def fast_fib(n, memo=dict()):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        return memo[n]


if __name__ == '__main__':
    print("fib(%u) = %u" % (120, fast_fib(120)))

    
    
    
    