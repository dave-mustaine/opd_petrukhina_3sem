import json


def get_variant_data_1():
    # global variant
    n = int(input('Введите номер варианта: '))

    with open('task_rcs_01.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    found = False
    for item in data['data']:

        if item['variant']['number'] == n:
            v = item['variant']
            find_variant = list()
            find_variant.append(float(v['D']))
            find_variant.append(float(v['fmin']))
            find_variant.append(float(v['fmax']))
            found = True
            break

    if not found:
        print('Вариант не найден')

    return find_variant
