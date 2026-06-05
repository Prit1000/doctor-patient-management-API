from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form and result
template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Multiplication Table</title>
  </head>
  <body>
    <div class="container">
      <h1>Multiplication Table</h1>
      <form method="POST">
        <div class="form-group">
          <label for="number">Enter a number:</label>
          <input type="number" class="form-control" id="number" name="number" required>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
      {% if table %}
      <h2>Table of {{ number }}</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Multiplier</th>
            <th>Result</th>
          </tr>
        </thead>
        <tbody>
          {% for i in range(1, 11) %}
          <tr>
            <td>{{ number }} x {{ i }}</td>
            <td>{{ number * i }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            return render_template_string(template, number=number, table=True)
        except ValueError:
            pass
    return render_template_string(template, number=None, table=False)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)