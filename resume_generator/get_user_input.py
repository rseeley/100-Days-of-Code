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


def mylistprint(l):
    for i in l:
        print('\t', i, '\n')


def myprint(d):
    for k, v in d.items():
        if isinstance(v, list):
            print(k + ': \n')
            mylistprint(v)
        elif isinstance(v, dict):
            myprint(v)
        else:
            print(f"{k}: {v}")


myprint(schools)
myprint(jobs)
