from app import db
from models import Class, Subject, Teacher, Learningactivities


def add_class_to_db():
    class_list = ['Пятый', 'Шестой', 'Седьмой', 'Восьмой', 'Девятый']
    for i in class_list:
        to_db = Class(i)
        db.session.add(to_db)

    db.session.commit()


def add_subject_to_db():
    subject_list = ['Математика', 'Статистика', 'Биология', 'География', 'Садоводство', 'Спорт', 'Пение']
    for i in subject_list:
        to_db = Subject(i)
        db.session.add(to_db)

    db.session.commit()


def add_teachers_to_db():
    teachers_list = [
        {"fullname": "ПетроваПП", "qualification": "Стажер"},
        {"fullname": "СидоровСС", "qualification": "Оператор"},
        {"fullname": "ДенисоваДД", "qualification": "Выпускник"},
        {"fullname": "ЛенинЛЛ", "qualification": "Практикант"}
    ]
    for i in teachers_list:
        fullname = i["fullname"]
        qualification = i["qualification"]
        to_db = Teacher(fullname, qualification)
        db.session.add(to_db)

    db.session.commit()


def add_learningactivities_to_db():
    activities_list = [
        {"class": "Пятый", "subject": "Биология", "teacher_name": "СидоровСС"},
        {"class": "Шестой", "subject": "Математика", "teacher_name": "ПетроваПП"},
        {"class": "Девятый", "subject": "Статистика", "teacher_name": "ПетроваПП"},
        {"class": "Седьмой", "subject": "География", "teacher_name": "ДенисоваДД"},
        {"class": "Восьмой", "subject": "Садоводство", "teacher_name": "СидоровСС"},
        {"class": "Девятый", "subject": "Спорт", "teacher_name": "ЛенинЛЛ"},
        {"class": "Шестой", "subject": "Пение", "teacher_name": "ЛенинЛЛ"}
    ]
    for i in activities_list:
        idclass = Class.query.filter(Class.name == i['class']).first()
        idteacher = Teacher.query.filter(Teacher.fullname == i['teacher_name']).first()
        idsubject = Subject.query.filter(Subject.name == i['subject']).first()
        to_db = Learningactivities(idclass, idteacher, idsubject)
        db.session.add(to_db)

    db.session.commit()


if __name__ == '__main__':
    add_class_to_db()
    add_subject_to_db()
    add_teachers_to_db()
    add_learningactivities_to_db()
    print("Database filled")
