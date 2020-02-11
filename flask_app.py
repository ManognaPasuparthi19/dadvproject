import pandas as pd
from flask import Flask, Markup, render_template
import re

app = Flask(__name__)

#redaing data from csv file
af = pd.read_csv('medals.csv')
labels=list(af['0'].head(50))
no_sumer=list(af['1'].head(50))
summer_1=list(af['2'].head(50))
summer_2=list(af['3'].head(50))
summer_3=list(af['4'].head(50))
summer_total=list(af['5'].head(50))
no_winter=list(af['6'].head(50))
winter_1=list(af['7'].head(50))
winter_2=list(af['8'].head(50))
winter_3=list(af['9'].head(50))

#type casting
def cleaning(l):
    for i in range(0, len(l)):
        l[i]=float(l[i])
    return l

no_sumer=cleaning(no_sumer)
summer_1=cleaning(summer_1)
summer_2=cleaning(summer_2)
summer_3=cleaning(summer_3)

no_winter=cleaning(no_winter)
winter_1=cleaning(winter_1)
winter_2=cleaning(winter_2)
winter_3=cleaning(winter_3)

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/no_of_summer')
def no_of_summer():
    print("in summer")
    bar_labels=labels
    bar_values=no_sumer
    m = max(no_sumer)
    t="No of summer games played"
    return bar(bar_labels,bar_values,m,t)

@app.route('/no_of_winter')
def no_of_winter():
    print("in winter")
    bar_labels=labels
    bar_values=no_winter
    m = max(no_winter)
    t="No of winter games played"
    return bar(bar_labels,bar_values,m,t)

@app.route('/summer_gold')
def no_of_summer_gold():
    print("in summer")
    bar_labels=labels
    bar_values=summer_1
    m = max(summer_1)
    t="Goald Medals"
    return bar(bar_labels,bar_values,m,t)


@app.route('/winter_gold')
def winter_gold():
    print("in winter")
    bar_labels=labels
    bar_values=winter_1
    m = max(winter_1)
    t="Gold Medals"
    return bar(bar_labels,bar_values,m,t)

@app.route('/summer_silver')
def summer_silver():
    print("in summer")
    bar_labels=labels
    bar_values=summer_2
    m = max(summer_2)
    t="Silver Medals"
    return bar(bar_labels,bar_values,m,t)

@app.route('/winter_silver')
def winter_silver():
    print("in winter")
    bar_labels=labels
    bar_values=winter_2
    m = max(winter_2)
    t="Winter Medals"
    return bar(bar_labels,bar_values,m,t)

@app.route('/summer_bronze')
def summer_bronze():
    print("in winter")
    bar_labels=labels
    bar_values=summer_3
    m = max(summer_3)
    t="Summer Bronze"
    return bar(bar_labels,bar_values,m,t)

@app.route('/winter_bronze')
def winter_bronze():
    print("in winter")
    bar_labels=labels
    bar_values=winter_3
    m = max(winter_3)
    t="Winter Bronze"
    return bar(bar_labels,bar_values,m,t)


@app.route('/one_two_three_summer')
def no_of_1_2_3_summer():
    print("in summer")
    bar_labels=labels
    bar_values1=summer_1
    bar_values2 = summer_2
    bar_values3=summer_3
    m1 = max(summer_1)
    m2=max(summer_2)
    m3=max(summer_3)
    m=max(m1,m2,m3)
    t="No of summer games played"
    return mulbar(bar_labels,bar_values1,bar_values2,bar_values3,m,t)


@app.route('/one_two_three_winter')
def no_of_1_2_3_winter():
    print("in winter")
    bar_labels=labels
    bar_values1 = winter_1
    bar_values2 = winter_2
    bar_values3=winter_3
    m1 = max(winter_1)
    m2 = max(winter_2)
    m3=max(winter_3)
    m = max(m1, m2,m3)
    t = "No of winter games played"
    return mulbar(bar_labels, bar_values1, bar_values2,bar_values3, m, t)


@app.route('/bar')
def bar(label,value,m,t):
    print("in bar")
    bar_labels=label
    bar_values=value
    maxvalue=m
    ti=t
    return render_template('all_charts_html.html', title=ti, max=maxvalue, labels=bar_labels, values=bar_values)



@app.route('/multibar')
def mulbar(label,value1,value2,value3,m,t):
    print("in bar")
    bar_labels=label
    bar_values1=value1
    bar_values2 = value2
    bar_values3=value3
    maxvalue=m
    ti=t
    return render_template('multiplebar.html', title=ti, max=maxvalue, labels=bar_labels, values=[bar_values1,bar_values2,bar_values3])

@app.route('/line')
def line(label,value,m,t):
    line_labels=labels
    line_values = value
    maxvalue = m
    ti = t
    return render_template('line.html', title='WAR', max=55000, labels=line_labels, values=line_values)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
