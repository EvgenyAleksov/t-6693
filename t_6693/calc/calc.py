from django.core.exceptions import ObjectDoesNotExist  # type: ignore

from t_6693.comms.models import Comm  # type: ignore
from t_6693.comps_comms.models import Comp_Comm  # type: ignore
from t_6693.comps_miss.models import Comp_Miss  # type: ignore
from t_6693.inspirations.models import Inspiration  # type: ignore
from t_6693.missions.models import Mission  # type: ignore


def get_insp(bd):
    res = []
    num_day = red_sum(bd.day)
    res.append(num_day)
    num_month = red_sum(bd.month)
    if num_month not in res:
        res.append(num_month)
    num_comm = red_sum(num_day + num_month)
    if num_comm not in res:
        res.append(num_comm)
    return res


def red_sum(num):
    if num > 22:
        return int(str(num)[0]) + int(str(num)[1])
    else:
        return num


def calc_num(bd):
    num_consc = red_single(bd.day)
    num_comm = red_single(num_consc + bd.month)
    num_miss = red_single(num_comm + bd.year)
    num_insp = get_insp(bd)

    result = {
        "num_consc": num_consc,
        "comm": get_data(Comm, num_comm),
        "miss": get_data(Mission, num_miss),
        "insp": get_data(Inspiration, num_insp),
    }
    return result


def get_comp(comp):
    result = {
        "comp_comm": get_data(Comp_Comm, comp),
        "comp_miss": get_data(Comp_Miss, comp),
    }
    return result


def red_single(num):
    n = num
    while True:
        if n > 9:
            n = n // 10 + n % 10
        else:
            return n


def get_data(model, data):
    try:
        if model in [Comm, Mission]:
            return model.objects.get(id=data)
        elif model in [Comp_Comm, Comp_Miss]:
            d = data if data[0] < data[1] else data[::-1]
            return model.objects.get(name=d)
        elif model in [Inspiration]:
            return model.objects.filter(id__in=data)
    except ObjectDoesNotExist:
        pass
