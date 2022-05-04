def get_user_entry():
    while True:
        try:
            code = int(input('Enter the four digit passcode.'))
        except ValueError:
            print('Please enter a four digit passcode.')
            continue
        if len(str(code)) != 4:
            print('Passcode must be four digits.')
        else:
            return code