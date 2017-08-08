from flask import Flask, render_template,jsonify,request
from pws import Google,Bing
import json

app=Flask(__name__)

@app.route("/")
def main():
	return render_template('start.html')


@app.route('/search',methods=["GET"])
def search():
	 engine = request.args.get('engine')
	 query = request.args.get('query')
	 num = request.args.get('num')
	 start = request.args.get('start')
	 recent = request.args.get('recent')
	 country_code = request.args.get('country_code')
	 if engine==None:
	 	return jsonify({"message": "engine is a required parameter"}), 400
	 if query==None:
	 	return jsonify({"message": "query is a required parameter"}), 400
	 if engine!="google" and engine!="bing":
	 	return jsonify({"message": "engine takes only either of two values; google or bing"}), 400 

	 if num==None:
	 	num=10
	 else:
	 	if num.isdigit():
	 		num=int(num)
	 		if(num>40):
	 			return jsonify({"message": "num should be < 40"}), 400
	 	else:
	 		return jsonify({"message": "num type should be int"}), 400
	 if start==None:
	 	start=0
	 else:
	 	if start.isdigit():
	 		start=int(start)
	 	else:
	 		return jsonify({"message": "start type should be int"}), 400
	 if country_code!=None:
	 	if len(country_code)!=2:
	 		return jsonify({"message": "country code should be 2 characters"}), 400
	 if engine=="google":
	 	if num!=None or start!=None or recent!=None or country_code!=None:
	 		res=Google.search(query=query,num=num,start=start,recent=recent,country_code=country_code)
	 		return jsonify(res)			 
	 	else:
	 		res=Google.search(query=query)
	 		return jsonify(res)
	 else:
	 	if num!=None or start!=None or recent!=None or country_code!=None:
	 		res=Bing.search(query=query,num=num,start=start,recent=recent,country_code=country_code)
	 		return jsonify(res)			 
	 	else:
	 		res=Bing.search(query=query)
	 		return jsonify(res)

	
if __name__ == "__main__":
    app.run(debug=True)