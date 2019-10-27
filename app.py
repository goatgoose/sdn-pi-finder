from flask import Flask, request, render_template

app = Flask(__name__)

hosts = {}


@app.route("/")
def index():
    return render_template("pifinder.html", hosts=hosts)


@app.route("/submit/<host>", methods=["POST"])
def submit(host):
    ifconfig = request.get_data().decode("UTF-8")
    host_dict = {"ifconfig": ifconfig, "wlan_ip": None}

    wlan0_position = ifconfig.find("wlan0")
    if wlan0_position > -1:
        inet_position = ifconfig.find("inet ", wlan0_position)
        if inet_position > -1:
            host_dict["wlan_ip"] = ifconfig[inet_position + 5:ifconfig.find(" ", inet_position + 5)]

    hosts[host] = host_dict
    print(hosts)
    return "ok"


if __name__ == '__main__':
    app.run()
