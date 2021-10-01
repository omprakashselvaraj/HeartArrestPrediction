from flask import Flask, request, render_template
import pickle

from werkzeug import datastructures


path='hd.pkl'
model = pickle.load(open(path, 'rb'))

app=Flask(__name__)

@app.route('/input',methods=['GET','POST'])
def input():
    if request.method=="POST":
        details=request.form
        age=int(details['age'])
        sex=int(details['sex'])
        cp=int(details['cp'])
        fbs=int(details['fbs'])
        res=int(details['res'])
        exng=int(details['exng'])
        pp=float(details['pp'])
        sl=int(details['sl'])
        caa=int(details['caa'])
        prediction=model.predict([[age,sex,cp,fbs,res,exng,pp,sl,caa]])
        val=prediction[0]
        if val==0:
            msg="No Heart Arrest"
        else:
            msg="Heart Arrest"
    return render_template('output.html', msg=msg)


@app.route('/')
def submit():
    return render_template('input.html')
#main function
if __name__ == '__main__':
    app.run(debug=True)