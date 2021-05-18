from validate_IK import validate_IK

def test_cases(): #Функция со всеми тест кейсами из задания

    correct_code = "50303020010" #Корректный код
    
    cases = ['474111203', '47411120355', ' 474111203',
             'a474111203', '-474111203', '77411120356',
             '08411120351', '52313210045', '52013220021',
             '52001320024', '52002300026', '30002290055',
             '41911120019']

    for case in cases:
        print(case)
        print(validate_IK(case))
        print()

test_cases()