import pandas as pd


def main():
    df = pd.read_json('test_cases_input.json')
    ls = create_dict(df)

    # region success
    print("----------------------------")
    print("--------- SUCCESS ----------")
    print("----------------------------")
    for i in range(30):
        try:
            print(dict_test(ls[i]))
        except AssertionError as e:
            continue
    # endregion

    # region error
    print("----------------------------")
    print("---------- ERROR -----------")
    print("----------------------------")

    errors = []
    for i in range(30):
        try:
            dict_test(ls[i])
        except AssertionError as e:
            errors.append(str(e))

    errors.sort()
    for error in errors:
        print(error)
    # endregion


def dict_test(d):
    id = d['case_id']
    dict_type = d['type']

    # region UNIT CONVERSION
    if dict_type == 'unit_conversion':
        # 1 lbs = 453.59237 g
        lb = 453.59237

        # region missing data assert
        assert d['data']['value'] is not None, \
            f"[MISSING DATA ({id})]: Value is None."
        assert d['data']['unit'] is not None, \
            f"[MISSING DATA ({id})]: Unit is None."
        assert d['config']['expected_unit'] is not None, \
            f"[MISSING DATA ({id})]: Expected unit is None."
        assert d['config']['min'] is not None, \
            f"[MISSING DATA ({id})]: Expected unit is None."
        # endregion

        # region frequently used data to variables
        value = d['data']['value']
        unit = d['data']['unit']
        expected_unit = d['config']['expected_unit']
        min = d['config']['min']
        # endregion

        # region lb -> lb
        if unit == 'lb' and expected_unit == 'lb':
            assert value > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} lb is not bigger than {min} lb"
        # endregion

        # region kg -> kg
        if unit == 'kg' and expected_unit == 'kg':
            assert value > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} kg is not bigger than {min} kg"
        # endregion

        # region g -> g
        if unit == 'g' and expected_unit == 'g':
            assert value > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} g is not bigger than {min} g"
        # endregion

        # region lb -> g
        if unit == 'lb' and expected_unit == 'g':
            assert value * lb > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} lb is not bigger than {min} g"
        # endregion

        # region lb -> kg
        if unit == 'lb' and expected_unit == 'kg':
            assert value * (lb / 1000) > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} lb is not bigger than {min} kg"
        # endregion

        # region g -> lb
        if unit == 'g' and expected_unit == 'lb':
            assert value / lb > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} g is not bigger than {min} lb"
        # endregion

        # region kg -> lb
        if unit == 'kg' and expected_unit == 'lb':
            assert (value / lb) * 1000 > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} kg is not bigger than {min} lb"
        # endregion

        # region kg -> g
        if unit == 'kg' and expected_unit == 'g':
            assert value * 1000 > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} kg is not bigger than {min} g"
        # endregion

        # region g -> kg
        if unit == 'g' and expected_unit == 'kg':
            assert value / 1000 > min, \
                f"[CONFIGURATION ERROR ({id})]: {value} g is not bigger than {min} kg"
        # endregion

        return f"[SUCCESS ({id})]: Unit conversion check"

    # endregion

    # region TYPE CHECK
    elif dict_type == 'type_check':
        # region frequently used data to variables
        expected_type = d['config']['expected_type']
        data = d['data']
        # endregion

        # region int
        if expected_type == 'int':
            assert type(data) is int, \
                f"[TYPE MISMATCH ({id})]: {data} is not {expected_type} ({type(data)})"
        # endregion

        # region string
        if expected_type == 'str':
            assert type(data) is str, \
                f"[TYPE MISMATCH ({id})]: {data} is not {expected_type} ({type(data)})"
        # endregion

        # region float
        if expected_type == 'float':
            assert type(data) is float, \
                f"[TYPE MISMATCH ({id})]: {data} is not {expected_type} ({type(data)})"
        # endregion
        return f"[SUCCESS ({id})]: Type check"

    # endregion

    # region REQUIRED FIELD
    elif dict_type == 'required_field':
        # region frequently used data to variables
        data = d['data']
        config = d['config']
        # endregion

        # region assert
        if data is None:
            assert type(config) is not float and d['config']['allow_null'] == True, \
                f"[CONFIGURATION ERROR ({id})]: Not allowed None"
        # endregion
        return f"[SUCCESS ({id})]: Required field check"

    # endregion
    return "Unknown ending"


def create_dict(df):
    types = df.type.unique()
    list = []

    for idx, row in df.iterrows():
        if row.iloc[1] == types[0]:
            d = {
                "case_id": row.iloc[0],
                "type": row.iloc[1],
                "data": row.iloc[2],
                "config": row.iloc[3],
            }
            list.append(d)

        elif row.iloc[1] == types[1]:
            d = {
                "case_id": row.iloc[0],
                "type": row.iloc[1],
                "data": row.iloc[2],
                "config": row.iloc[3],
            }
            list.append(d)

        elif row.iloc[1] == types[2]:
            d = {
                "case_id": row.iloc[0],
                "type": row.iloc[1],
                "data": row.iloc[2],
                "config": row.iloc[3],
            }
            list.append(d)

    return list


main()
