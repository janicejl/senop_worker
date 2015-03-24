# controller

from . import app

from flask import render_template, jsonify, url_for

@app.route('/')
def index():
  return render_template('index.html')

from .tasks import long_task

@app.route('/longtask', methods=['POST'])
def longtask():
  task = long_task.apply_async()
  response = {
      'Location': url_for('taskstatus', task_id = task.id)
      }
  #return jsonify({}), 202, {'Location': url_for('taskstatus',
  #                                              task_id=task.id)}
  return jsonify(response)

@app.route('/status/<task_id>')
def taskstatus(task_id):
  task = long_task.AsyncResult(task_id)
  if task.state == 'PENDING':
    # job did not start yet
    response = {
      'state': task.state,
      'current': 0,
      'total': 1,
      'status': 'Pending...'
    }
  elif task.state != 'FAILURE':
    response = {
      'state': task.state,
      'current': task.info.get('current', 0),
      'total': task.info.get('total', 1),
      'status': task.info.get('status', '')
    }
    if 'result' in task.info:
      response['result'] = task.info['result']
  else:
    # something went wrong in the background job
    response = {
      'state': task.state,
      'current': 1,
      'total': 1,
      'status': str(task.info),  # this is the exception raised
    }
  return jsonify(response)

