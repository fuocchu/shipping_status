from flask import Flask, render_template,request
from models import get_status


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question1_shipping_status',methods=['POST'])
def shipping_status():
    ID = request.form.get('ID')
    if not ID:
        return "Vui long nhap ID", 400
    status =get_status(ID)
    if status:
        message = f"Trang Thai Cua Don Hang {ID} la : {status}"
    else:
        message = f"Khong tim thay ID don hang {ID} cua ban"
    
    return render_template('index.html',message=message)