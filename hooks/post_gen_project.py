def check(name):
    if name == "":
        return 'project name is blank'
    return

def output(message):
    if message:
        print(message)
    else:
        print('complete')
    return

if __name__ == '__main__':
    project_name = '{{cookiecutter.project_name}}'
    output(check(project_name))
    
