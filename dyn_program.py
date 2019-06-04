import random
TEST_ITEMS_CNT = 40

EACH_WEIGHT_MAX = 1000
EACH_VALUE_MAX = 1000
MAX_WEIGHT = EACH_WEIGHT_MAX*TEST_ITEMS_CNT
MAX_VALUE = EACH_VALUE_MAX*TEST_ITEMS_CNT


class Item:

    def __init__(self, name, value, weight):
        self._name = name
        self._value = value
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def weight(self):
        return self._weight

    @property
    def density(self):
        return self._value / self._weight

    def __str__(self):
        return " <%s> %u %u" % (self._name, self._value, self._weight)


def items_2_str(items):
    res_ = ""
    for itm in items:
        res_ += "%s" % itm
        res_ += " "
    return res_


def maximize_val(item_list, avail):
    if not item_list or not avail:
        print("END")
        return 0, []
    itm = item_list.pop(0)
    print("%s | %s < %u" % (itm, items_2_str(item_list), avail))
    if itm.weight > avail:
        return maximize_val(list(item_list), avail)
    else:
        with_val, with_items = maximize_val(list(item_list), avail - itm.weight)
        without_val, without_items = maximize_val(list(item_list), avail)
        if with_val + itm.value > without_val:
            return with_val + itm.value, [itm] + with_items
        else:
            return without_val, list(without_items)


def fast_maximize_val(item_list, avail, memo={}):
    try:
        return memo[(len(item_list), avail)]
    except KeyError:
        pass
    
    if not item_list or not avail:
        ret_val, ret_list = 0, []
    else:
        itm = item_list.pop(0)
        
        if itm.weight > avail:
            ret_val, ret_list = fast_maximize_val(list(item_list), avail)
        else:
            with_val, with_list = fast_maximize_val(list(item_list), avail - itm.weight)
            without_val, without_list = fast_maximize_val(list(item_list), avail)
            if with_val + itm.weight > without_val:
                ret_val, ret_list = itm.value + with_val, [itm] + with_list
            else:
                ret_val, ret_list = without_val, list(without_list)
    
    memo[(len(ret_list), avail)] = (ret_val, ret_list)
    return ret_val, ret_list
    
    
def build_items(itm_cnt):
    return [Item(str(i), random.randint(1, EACH_VALUE_MAX), random.randint(1, EACH_WEIGHT_MAX)) for i in range(itm_cnt)]


def small_testing():
    names = ['a', 'b', 'c', 'd']
    values = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    items = [Item(n, v, w) for n, v, w in zip(names, values, weights)]
    print("         | %s < %u" % (items_2_str(items), 5))
    val, token = maximize_val(items, 5)
    print("MAX VAL:", val)
    print("TOKEN:", items_2_str(token))


def big_testing():
    val, token = fast_maximize_val(build_items(TEST_ITEMS_CNT), MAX_WEIGHT)
    print("MAX VAL:", val)
    print("TOKEN:", items_2_str(token))


if __name__ == '__main__':
    big_testing()
