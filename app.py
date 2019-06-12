"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
  #  json_data = {'Hello': 'World!'}
  #  return" น.ส.ลักษณาวดี อิ่มเสมอ เลขที่14 ม.4/1"

if __name__ == '__main__':
    app.run()
