import pandas as pd
def main():
    x = pd.read_json('test_cases_input.json')
    ls = create_dict(x)

    for i in range(30):
        try:
            dict_test(ls[i])
        except AssertionError as e:
            print(f"Dict{ls[i]['case_id']}: {e}")

def dict_test(dict):

    #region CASE_ID (extra)
    id = dict['case_id']
    type = dict['type']

    assert id >= 1 and id <= 30, \
        f"Invalid case_id {id} is not between 1 and 30"

    assert type == 'unit_conversion' or \
           type == 'required_field' or \
           type == 'type_check', \
        f"Invalid type of {type}"
    #endregion'''

    # region UNIT CONVERSION
    if(dict['type'] == 'unit_conversion'):
        lb = 453.59237     # 1 lbs = 453.59237 g

        assert dict['data']['value'] is not None, "Value is None."
        assert dict['data']['unit'] is not None, "Unit is None."
        assert dict['config']['expected_unit'] is not None, "Expected unit is None."
        assert dict['config']['min'] is not None, "Expected unit is None."



        value = dict['data']['value']
        unit = dict['data']['unit']
        expected_unit = dict['config']['expected_unit']
        min = dict['config']['min']


        if(unit == 'lb' and expected_unit == 'lb'):
            assert value > min,\
            f"{value} lb is not bigger than {min} lb"

        if(unit == 'kg' and expected_unit== 'kg'):
            assert value > min,\
            f"{value} kg is not bigger than {min} kg"

        if(unit == 'g' and expected_unit == 'g'):
            assert value > min,\
            f"{value} g is not bigger than {min} g"




        if(unit == 'lb' and expected_unit == 'g'):
            assert value*lb > min,\
            f"{value} lb is not bigger than {min} g"

        if(unit == 'lb' and expected_unit == 'kg'):
            assert value*(lb/1000) > min,\
            f"{value} lb is not bigger than {min} kg"




        if(unit == 'g' and expected_unit == 'lb'):
            assert value/lb > min,\
            f"{value} g is not bigger than {min} lb"


        if(unit == 'kg' and expected_unit == 'lb'):
            assert (value/lb)*1000 > min,\
            f"{value} kg is not bigger than {min} lb"


        if(unit == 'kg' and expected_unit == 'g'):
            assert value*1000 > min,\
            f"{value} kg is not bigger than {min} g"

        if(unit == 'g' and expected_unit == 'kg'):
            assert value/1000 > min,\
            f"{value} g is not bigger than {min} kg"

    #endregion

    print(dict['config']['expected_type'])
    # region TYPE CHECK
    '''if(dict['type'] == 'type_check'):
        if (dict['config']['expected_type'] == 'int'):
            assert type(dict['data']) is int,\
            f"{dict['data']} is not {dict['config']['expected_type']} ({type(dict['data'])})"

        if (dict['config']['expected_type'] == 'str'):
            assert type(dict['data']) is str,\
            f"{dict['data']} is not {dict['config']['expected_type']} ({type(dict['data'])})"

        if (dict['config']['expected_type'] == 'float'):
            assert type(dict['data']) is float,\
            f"{dict['data']} is not {dict['config']['expected_type']} ({type(dict['data'])})"'''

    #endregion

    #region REQUIRED FIELD
    '''if dict['type'] == 'required_field':
        if (dict['data'] is None):
            assert type(dict['config']) is not float and dict['config']['allow_null'] == True,\
            f"Data is {dict['data']}, while config does not exist or allow it."'''

    #endregion

def create_dict(df):
    types = df.type.unique()

    list = []

    for idx, row in df.iterrows():
        if row.iloc[1] == types[0]:
            dict = {
                "case_id": row.iloc[0],
                "type": row.iloc[1],
                "data": row.iloc[2],
                "config": row.iloc[3],
            }
            list.append(dict)

        if row.iloc[1] == types[1]:
            dict = {
                "case_id": row.iloc[0],
                "type": row.iloc[1],
                "data": row.iloc[2],
                "config": row.iloc[3],
            }
            list.append(dict)

        if row.iloc[1] == types[2]:
            dict = {
                "case_id": row.iloc[0],
                "type": row.iloc[1],
                "data": row.iloc[2],
                "config": row.iloc[3],
            }
            list.append(dict)

    return list

main()