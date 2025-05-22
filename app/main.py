from flask import Flask, request, jsonify, render_template
from osint import get_dns, get_whois, get_ssl_info
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    domain = request.args.get("domain")
    result = None
    check_time = None
    if domain:
        result = {
            "dns": get_dns(domain),
            "whois": get_whois(domain),
            "ssl": get_ssl_info(domain)
        }
        check_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    return render_template("index.html", result=result, domain=domain, check_time=check_time)

@app.route("/osint", methods=["GET"])
def api():
    domain = request.args.get("domain")
    if not domain:
        return jsonify({"error": "domain parameter required"}), 400

    result = {
        "domain": domain,
        "dns": get_dns(domain),
        "whois": get_whois(domain),
        "ssl": get_ssl_info(domain)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)