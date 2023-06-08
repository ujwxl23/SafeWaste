from flask import Flask, render_template, request

app = Flask(__name__)
 
@app.route('/')
@app.route('/home')
def home():
    return render_template("pythonback.html")

@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]


    return render_template('pythonback.html', name = name)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # from firebase import firebase
    # firebase = firebase.FirebaseApplication( "https://fir-718ed-default-rtdb.firebaseio.com/",None)

    # result = firebase.get('/Peoples','')
    # print(result)

    # # Calculate tokens
    # for i in result:
    #     names= result.keys()
    #     namesl= list(names)
    #     print(namesl)
    #     for i in namesl:
    #         L = (result[i])
    #         drytoken = int(L['Drywaste'])* 0.05
    #         mixedtoken = int(L['Mixedwaste'])* 0.03
    #         sponsortoken = int(L['Sponsorwaste'])*0.07
    #         wettoken = int(L['Wetwaste'])*0.06
    #         totaltoken = drytoken + mixedtoken + sponsortoken + wettoken
    #         print(totaltoken)
    #         totaltokenstr = str(totaltoken)
    #         n = i
    #         print(n)
    #         firebase.put(("/Peoples/" + i ),'Totaltokens',totaltokenstr)
    #     d = dict()
    #     for i in namesl:
    #         Lo = (result[i])
    #         d[Lo['Totaltokens']]= i
    #     print(d)
    #     newd = sorted(d.items(),reverse= True)
    #     print(newd)

    # firebase.post(("/Leaderboard/" ),newd)