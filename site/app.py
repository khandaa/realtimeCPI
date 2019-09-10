from flask import Flask, render_template, request, json
app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'cpidsadmin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CpiDsAdmin'
app.config['MYSQL_DATABASE_DB'] = 'cpi_ds'
app.config['MYSQL_DATABASE_HOST'] = 'eastern-archive-252417:asia-south1:cpi-ds'
mysql.init_app(app)
conn = mysql.connect();

@app.route("/")
def main():
    #return "Welcome!"
    return render_template('index.html');

@app.route("/CPIPrediction" , methods=['POST'])
def CPIPrediction():
    return render_template('CPIPrediction.html');
    $(function() {
        $('#btnGetCPIPrediction').click(function() {
     
            $.ajax({
                url: '/getCPIPrediction',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });
    });

@app.route("/getCPIPrediction" , methods=['POST'])
def getCPIPrediction():
    return render_template('getCPIPrediction.html');

if __name__ == "__main__":
    app.run()


