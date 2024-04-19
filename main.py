from flask import Flask, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    # if request.method == "POST":
    #     if 'submit' in request.form:
    #         result = calculate(request.form)
    #         return render_template('index.html', result=result, form=request.form)
    #     elif 'clear' in request.form:
    #         return render_template("index.html", result=None, form={})
    #
    # else:
    #     return render_template('index.html', result=None, form={})
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    form = request.form
    hw = [form.get(f"hw{i}", 0, type=int) for i in range(1,7)]
    hw.remove(min(hw))
    finalexam = form.get("finalexam", 0, type=int)
    midterm1 = form.get("midterm1", 0, type=int)
    midterm2 = form.get("midterm2", 0, type=int)


    avg_hw = sum(hw)/len(hw)
    midterm1 = avg_hw * 0.6 + max(avg_hw, midterm1) * 0.4
    midterm2 = avg_hw * 0.6 + max(avg_hw, midterm2) * 0.4

    grade = avg_hw * 0.5 + finalexam * 0.3 + max(midterm1, midterm2, avg_hw) * 0.2
    if 'survey' in form:
        grade += 1

    if 60 <= grade <= 69:
        letter = "D"
    elif 70 <= grade <= 79:
        letter = "C"
    elif 80 <= grade <= 89:
        letter = "B"
    elif 90 <= grade:
        letter = "A"
    else:
        letter = "F"


    # return f"{letter} ({grade})"
    return jsonify(result=f"{letter} ({round(grade, 2)})")

if __name__ == '__main__':
    app.run(debug=True)