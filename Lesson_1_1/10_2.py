c_sharp = 375
java = 546
javascript = 915
php = 288
python = 603

value = [c_sharp , java , javascript , php , python]

def analyze_jobs():
    
    total_jobs = c_sharp + java + javascript + php + python
    
    python_percent = python / total_jobs * 100
    python_percent = round(python_percent,2)
    
    print('Общее число исследованных вакансий, в тысячах:', total_jobs)
    print('Вакансии для Python-разработчиков, в %:', python_percent)

analyze_jobs()