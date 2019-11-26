import file_exp
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/report.html')
def report():
    path = request.args.get('path')
    wcfilter = request.args.get('wcfilter')
    list=file_exp.fuc(path,wcfilter)
    return(render_template('report.html',list=list))

if __name__ == '__main__':
    app.run(debug=True)
