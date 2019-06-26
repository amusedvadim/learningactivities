from flask import render_template, request
from app import app, db
from models import Class, Teacher


@app.route('/')
def index():
    all_teachers = Teacher.query.all()
    return render_template('index.html', all_teachers=all_teachers)


@app.route(('/classes'))
def classes():
    all_classes = Class.query.all()
    return render_template('allclasses.html', all_classes=all_classes)


@app.route('/teachers')
def teachers():
    all_teachers = Teacher.query.all()
    return render_template('allteachers.html', all_teachers=all_teachers)


@app.route('/byid', methods=['GET'])
def teacher_by_id():
    idteacher = request.args.get('teacher')

    res = db.session.execute(' \
    SELECT Class.name, Subject.name \
    FROM Learningactivities \
    LEFT JOIN Class on Learningactivities.idclass=Class.idclass \
    LEFT JOIN Subject on Learningactivities.idsubject=Subject.idsubject \
    WHERE idteacher = :idteacher',{'idteacher':idteacher})

    rows = res.fetchall()
    teacher_name = Teacher.query.filter_by(idteacher=idteacher).first().fullname

    return render_template('teacher.html', rows=rows, teacher_name=teacher_name)
