def get_operator(phone_number):

    indic_numbers = []

    indic_numbers.append(phone_number[0:6])
    indic_numbers.append(phone_number[0:5])
    indic_numbers.append(phone_number[0:4])

    with open('modules\indic.txt','r') as indic_file:
        lines = indic_file.readlines()
        indic_file.close()

    for indicatif_target in indic_numbers:
        for line in lines:
            phone_indic = line.split(':')[0]
            operator    = line.split(':')[1]
            if indicatif_target == phone_indic:
                return operator

def get_phone_by_name(name,pren):

    data        = []

    found_lines = []

    paths = [
        r'C:\Users\dalun\OneDrive\Bureau\PC\000\Countrys\France_01.txt',
        r'C:\Users\dalun\OneDrive\Bureau\PC\000\Countrys\France_02.txt',
        r'C:\Users\dalun\OneDrive\Bureau\PC\000\Countrys\France_03.txt',
        r'C:\Users\dalun\OneDrive\Bureau\PC\000\Countrys\France_04.txt',
        r'C:\Users\dalun\OneDrive\Bureau\PC\000\Countrys\France_05.txt',
    ]

    for path in paths:
        with open(path,'r',encoding="utf8") as database:
            lines = database.readlines()
            for i in lines:
                if pren.lower()+','+name.lower() in i.lower():
                    found_lines.append(i)
    
    for i in found_lines:
        phone_number   = i.split(',')[0]
        male_or_female = i.split(',')[4]
        city           = i.split(',')[5]

        if len(city) == 0:
            city = None


        if "Single" in i:
            situation = "   Single / Célib."
        elif "In a Relation" in i:
            situation = "Relationship / En Couple."
        else:
            situation = "Situation amoureuser introuvable"

        phone_number = phone_number.replace('33','0')
        operator = get_operator(phone_number=phone_number)
        if operator == None:
            operator = "Not Found"

        phone_number = phone_number[0:2]+" "+phone_number[2:4]+" "+phone_number[4:6]+" "+phone_number[6:8]+" "+phone_number[8:10]
        just_data = {
            'Phone_Number':phone_number,
            "Provider":operator,
            'Male_O_Female':male_or_female,
            'City':city,
            "Situation":situation
        }

        data.append(just_data)
    if len(just_data) == 0:
        return None
    else:
        return data
