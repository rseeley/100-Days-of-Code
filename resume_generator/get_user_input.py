name = input('Enter your full name: ').strip()

schools = {}
while True:
    school = input('Enter a school name ("q" to quit): ').strip()

    if school == 'q':
        break
    else:
        years = input('Enter a date range for ' + school + ': ').strip()
        degree = input('Enter your degree from ' + school + ': ').strip()
        schools[school] = {
            "School": school,
            "Years": years,
            "Degree": degree
        }

jobs = {}
while True:
    job = input(
        'Enter your employment history, starting from the most recent ("q" to '
        'quit): '
    ).strip()

    if job == 'q':
        break
    else:
        years = input('Enter a date range for ' + job + ': ').strip()

        responsibilities = []
        while True:
            responsibility = input(
                'Describe a responsibility you had during your employment at ' +
                job + ' ("q" to quit): '
            ).strip()

            if responsibility == 'q':
                break
            else:
                responsibilities.append(responsibility)

        jobs[job] = {
            "Job": job,
            "Years": years,
            "Responsibilities": responsibilities
        }


# Prints the values in a list, tabbed once
# This is used in the dict_print() for job responsibilities
def list_print(l):
    for i in l:
        print('\t' + i)


# Recursively prints the key and value of a dictionary
# In this case, it will print the name of the school/job,
# years, and degree/responsibilities, respectively
def dict_print(d):
    for k, v in d.items():
        if isinstance(v, list):
            print(k + ':')
            list_print(v)
        elif isinstance(v, dict):
            dict_print(v)
        else:
            print(f"{k}: {v}")
