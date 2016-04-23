__author__ = 'rcj1492'
__created__ = '2015.10'

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from server.config import *
from server.resources import *
from flask import request, jsonify, url_for, render_template

@app.route('/')
def dashboard_page():
    request_dict = {'headers': {}, 'body': request.form}
    for key, value in request.headers.items():
        request_dict['headers'][key] = value
    app.logger.debug('Headers: %s' % request_dict)
    return render_template('landing.html'), 200

@app.route('/v1/operation/model')
def operation_validate():
    valid_response, code = operationResource.request.validate(request)
    if code:
        return jsonify(valid_response), code
    request_dict = {'headers': {}, 'body': request.form}
    for key, value in request.headers.items():
        request_dict['headers'][key] = value
    app.logger.debug('Headers: %s' % request_dict)
    model_details = operationResource.model.schema
    model_title = operationResource.model.title
    return render_template('model.html', modelTitle=model_title, modelDetails=model_details), 200

@app.route('/v1/catch/model')
def operation_validate():
    valid_response, code = operationResource.request.validate(request)
    if code:
        return jsonify(valid_response), code
    request_dict = {'headers': {}, 'body': request.form}
    for key, value in request.headers.items():
        request_dict['headers'][key] = value
    app.logger.debug('Headers: %s' % request_dict)
    model_details = operationResource.model.schema
    model_title = operationResource.model.title
    return render_template('model.html', modelTitle=model_title, modelDetails=model_details), 200

@app.route('/v1/specimen/model')
def operation_validate():
    valid_response, code = operationResource.request.validate(request)
    if code:
        return jsonify(valid_response), code
    request_dict = {'headers': {}, 'body': request.form}
    for key, value in request.headers.items():
        request_dict['headers'][key] = value
    app.logger.debug('Headers: %s' % request_dict)
    model_details = operationResource.model.schema
    model_title = operationResource.model.title
    return render_template('model.html', modelTitle=model_title, modelDetails=model_details), 200

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

config_args = {
    'host': '0.0.0.0',
    'port': 5000
}

# initialize flask wsgi dev server
if __name__ == '__main__':
    app.run(**config_args)
