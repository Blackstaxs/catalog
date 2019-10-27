#!/usr/bin/env python

from flask import (Flask, render_template, request,
                   redirect, jsonify, url_for, flash)

from flask import session as login_session
import random
import string

import httplib2
import json
from flask import make_response
import requests


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Job, Ability
app = Flask(__name__)

APPLICATION_NAME = "ff"


engine = create_engine('sqlite:///ff14jobs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()





@app.route('/jobs/<int:job_id>/')
def restaurantMenu(job_id):
    job = session.query(Job).filter_by(id=job_id).one()
    items = session.query(Ability).filter_by(job_id=job.id)
    return render_template('class.html', job=job, items=items)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return render_template('index.html')


@app.route('/all')
def testhello():
    job = session.query(Job).all()
    output = ''
    for i in job:
        output += i.name
        output += '</br>'
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
        output += '</br>'
    return output

@app.route('/healer')
def test1():
    job1 = session.query(Job).filter_by(role='Healer')
    return render_template('classes.html', job=job1)


@app.route('/tank')
def test2():
    job2 = session.query(Job).filter_by(role='Tank')
    return render_template('classes.html', job=job2)


@app.route('/dps')
def test3():
    job3 = session.query(Job).filter_by(role='Dps')
    return render_template('classes.html', job=job3)


@app.route('/jobs/<int:job_id>/delete',
           methods=['GET', 'POST'])
def deleteJob(job_id):
    jobToDelete = session.query(Job).filter_by(id=job_id).one()
    if request.method == 'POST':
        session.delete(jobToDelete)
        session.commit()
        return redirect('/')
    else:
        return render_template('delete.html', item=jobToDelete)
   


@app.route('/JSON')
def ffJSON():
    jobs = session.query(Job).all()
    return jsonify(ffItems=[i.serialize for i in jobs])


@app.route('/jobs/<int:job_id>/ability/JSON')
def ffAbilityJSON(job_id):
    job = session.query(Job).filter_by(id=job_id).one()
    items = session.query(Ability).filter_by(
        job_id=job_id).all()
    return jsonify(ffItems=[i.serialize for i in items])


@app.route('/jobs/<int:job_id>/ability/<int:ability_id>/JSON')
def abilityJSON(job_id, ability_id):
    ability = session.query(Ability).filter_by(id=ability_id).one()
    return jsonify(Ability=ability.serialize)


@app.route('/jobs/<int:job_id>/<int:ability_id>/edit',
           methods=['GET', 'POST'])
def editAbility(job_id, ability_id):
    editedAbility = session.query(Ability).filter_by(id=ability_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedAbility.name = request.form['name']
            editedAbility.level = request.form['level']
            editedAbility.description = request.form['description']
        session.add(editedAbility)
        session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', job_id=job_id,
                                ability_id=ability_id, item=editedAbility)
  


@app.route('/jobs/<int:job_id>/new', methods=['GET', 'POST'])
def newAbility(job_id):
    if request.method == 'POST':
        newAbility = Ability(name=request.form['name'],
                             description=request.form['description'],
                             level=request.form['level'],
                             Cast=request.form['Cast'],
                             job_id=job_id)
        session.add(newAbility)
        session.commit()
        return redirect('/')
    else:
        return render_template('new.html', job_id=job_id)

if __name__ == '__main__':
    app.secret_key = 'ia1yTpinkCIgnkt_H8bHqswe'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
