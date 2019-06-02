import pylab
from decimal import Decimal


def find_payment(load, r, m):
    return load * (r * (1 + r) ** m) / ((1 + r) ** m - 1)


class Mortgage:
    def __init__(self, load, annual_rate, years):
        self._load = load
        self._tot_months = years * 12
        self._month_rate = Decimal(annual_rate) / 12
        self._out_standing = [self._load]
        self._paids = list()
        self._payment = find_payment(load, self._month_rate, self._tot_months)

    def make_payment(self):
        self._paids.append(self._payment)
        reduction = self.payment - self._out_standing[-1] * self._month_rate
        self._out_standing.append(self._out_standing[-1] - reduction)

    def get_total_paid(self):
        return sum(self._paids)

    @property
    def payment(self):
        return self._payment

    def __iter__(self):
        for i in range(self._tot_months + 1):
            self.make_payment()
            yield self._out_standing[i]

    def payment_sum(self):
        for i, p in enumerate(self._paids[1:], start=1):
            yield sum(self._paids[: i])


class Fixed(Mortgage):

    def __init__(self, load, annual_rate, years):
        super().__init__(load, annual_rate, years)

    def __str__(self):
        return "Fixed: " + str(round(self._month_rate * 100, 2)) + '%'


def main():
    load = 45*10000
    rate = 0.0325
    years = 10

    mortgage = Fixed(load, rate, years)
    print("Each moth pay: ", mortgage.payment)
    print("Outstanding:")
    [print("%u: %s" % (i, str(m))) for i, m in enumerate(mortgage)]
    print("Accumulated payments:")
    [print("%u: %r" % (i, str(m))) for i, m in enumerate(list(mortgage.payment_sum()))]
    print("Total interest: ", years * 12 * mortgage.payment - load)
    pylab.plot(list(mortgage.payment_sum()))
    pylab.show()


if __name__ == '__main__':
    main()
