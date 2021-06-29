from dbutil import query_for_flc
from flask import Flask, request, send_from_directory

app = Flask(__name__)

# this api will be called like:
# /api/district?q=Kozhikode
# to get all district data, simply call:
# /api/district
@app.route('/api/district')
def get_flc_details():
    district = request.args.get('q') # getting request parameter
    from_db = query_for_flc(district)
    return from_db

@app.route('/<path:filename>')
def static_files(filename):
    print(filename)
    return send_from_directory('www', filename)




if __name__ == "__main__":
    app.run()