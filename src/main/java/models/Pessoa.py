class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

if __name__ == '__main__':
    pessoa = Pessoa(nome='Thiago')
    print pessoa.nome

    from jinja2 import Environment, FileSystemLoader, PackageLoader, Template
    import os
    from java.io import File
    
    template = Template('Hello {{ name }}!')
    print template.render(name='John Doe')
    #env = Environment(loader=PackageLoader('app', 'templates'))    
    file = File(".")
    path = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(path, 'app')
    path = os.path.join(path, 'templates')
    print path
    env = Environment(
        autoescape=True, 
        loader=FileSystemLoader('/home/thiago/workspace/jython-test/src/app/templates')
    )    
    template = env.get_template('base.html')
    print template.render(message='Java and Python Itegration by Jython!')
    

