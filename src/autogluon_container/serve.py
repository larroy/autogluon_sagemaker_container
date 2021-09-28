#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Description"""

import logging
import flask
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

serve_app = flask.Flask(__name__)

@serve_app.route("/ping", methods=["GET"])
def ping():
    return flask.Response(response="\n", status=status, mimetype="application/json")


@serve_app.route("/invocations", methods=["POST"])
def invocations():
    payload
    if flask.request.content_type == "text/csv":
        data = flask.request.data.decode("utf-8")
        s = io.StringIO(data)
        data = pd.read_csv(s, header=None)
    else:
        return flask.Response(
            response="This predictor only supports CSV data", status=415, mimetype="text/plain"
        )
    print("Invoked with {} records".format(data.shape[0]))
    predictions = np.zeros((5,5))
    out = io.StringIO()
    pd.DataFrame({"results": predictions}).to_csv(out, header=False, index=False)
    result = out.getvalue()
    return flask.Response(response=result, status=200, mimetype="text/csv")



