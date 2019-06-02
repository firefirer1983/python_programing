import time
import py_compile
import pylab


def main():
    years = 20
    interest_rate = 0.02
    principal = 100000
    values = list()
    for r in range(years):
        principal += principal * interest_rate
        values.append(principal)
    pylab.title("2% Growth, Compounded Annually")
    pylab.xlabel("Years", fontsize='xx-large')
    pylab.ylabel("Principal")
    pylab.plot(list(range(years)), values, 'ko')
    pylab.show()


if __name__ == '__main__':
    main()


