from flask import Flask
from flask import render_template
import blink
import time

app= Flask(__name__)

led1,led2,led3= 11,13,15


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/A')
def led1on():
    #rpi.output(led1,1)
    blink.blink1(led1)
    return render_template('index.html')

"""
@app.route('/a')
def led1off():
    rpi.output(led1,0)
    return render_template('index.html')
"""
@app.route('/B')
def led2on():
    #rpi.output(led2,1)
    blink.blink1(led2)
    return render_template('index.html')
"""
@app.route('/b')
def led2off():
    rpi.output(led2,0)
    return render_template('index.html')
"""
@app.route('/C')
def led3on():
    #rpi.output(led3,1)
    blink.blink1(led3)
    return render_template('index.html')
"""
@app.route('/c')
def led3off():
    rpi.output(led3,0)
    return render_template('index.html')
"""
if __name__=="__main__":
    print("Start")
    app.run(debug=False, host='192.168.1.131')
