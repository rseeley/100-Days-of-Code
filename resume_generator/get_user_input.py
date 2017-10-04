name = input('Enter your full name: ')

print('Your name is ' + str(name))

schools = {}
while True:
    school = input('Enter a school name ("q" to quit): ').strip()

    if school == 'q':
        break
    else:
        years = input('Enter a date range for ' + school + ': ')
        degree = input('Enter your degree from ' + school + ': ')
        schools[school] = {
            "Years": years,
            "Degree": degree
        }

for school in schools:
    print(str.ljust("School:", 10), school)

    for detail in schools[school]:
        print(str.ljust(detail + ':', 10), schools[school][detail])
