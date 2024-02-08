from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')




@app.route('/comenzar_action_2', methods=['POST'])
def comenzar_action_2():
    return redirect(url_for('https://www.uber.com/co/en/business/getting-started/?ad_id=687156507569&campaign_id=20931062371&gclid=EAIaIQobChMIsLD-8OichAMV16NaBR1--wgXEAAYASAAEgLTifD_BwE&kw=uber&kwid=kwd-12633382&uclick_id=7281013b-4666-4290-8636-5649eff4ed7d&utm_campaign=CM2358409-search-google-brand_38_-99_CO-National_r_web_acq_cpc_es_T2_Generic_BM_uber_kwd-12633382_687156507569_156813381559_b_c&utm_source=AdWords_Brand'))


@app.route('/comenzar_action', methods=['POST'])
def comenzar_action():
    return redirect(url_for('https://auth.uber.com/v2/?breeze_local_zone=dca24&next_url=https%3A%2F%2Fdrivers.uber.com%2F%3F_ga%3D2.112422337.49619806.1707432277-1173105979.1707432276%26_gac%3D1.175245974.1707433490.EAIaIQobChMIsLD-8OichAMV16NaBR1--wgXEAAYASAAEgLTifD_BwE%26_gl%3D1%252Ah2eikf%252A_ga%252AMTE3MzEwNTk3OS4xNzA3NDMyMjc2%252A_ga_XTGQLY6KPT%252AMTcwNzQzMjI3NS4xLjEuMTcwNzQzMzQ5Mi4wLjAuMA..%26ad_id%3D687156507569%26campaign_id%3D20931062371%26gclid%3DEAIaIQobChMIsLD-8OichAMV16NaBR1--wgXEAAYASAAEgLTifD_BwE%26kw%3Duber%26kwid%3Dkwd-12633382%26marketing_vistor_id%3Da7b84fbb-686b-4b7d-a51e-fcddc24537f3%26uclick_id%3D7281013b-4666-4290-8636-5649eff4ed7d%26utm_campaign%3DCM2358409-search-google-brand_38_-99_CO-National_r_web_acq_cpc_es_T2_Generic_BM_uber_kwd-12633382_687156507569_156813381559_b_c%26utm_source%3DAdWords_Brand&state=Zft2kDLsa9Y11Bie4D7x0U7Yi8tSenLMFmNEG-mGxxw%3D'))







if __name__ == '__main__':
    app.run(debug=True, port=5001)