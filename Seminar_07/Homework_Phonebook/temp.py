def create(self, first_name, second_name, phone_number):
    """Создает в БД новую запись с параметрами first_name = имя, second_name = фамилия, phone_number - телефон"""
    with sql.connect('database.db') as connection:
        cursor = connection.cursor()
        request = f'''
         INSERT INTO Phonebook 
             (FirstName, SecondName, Phonenumber) 
         VALUES 
             ("{first_name}", "{second_name}", "{phone_number}");
         '''
        cursor.execute(request).fetchall()
        return [str(f'Произведена запись {first_name} {second_name} {phone_number}')]