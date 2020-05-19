from bokeh.models import Slider, Label, SingleIntervalTicker, NumeralTickFormatter,RadioButtonGroup
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.layouts import column, row, layout
from bokeh.io import output_file, show, curdoc
import numpy as np

# import 2020 mortality tables
mtables=np.genfromtxt("CDC2017 life tables.csv",delimiter=",",skip_header=1)
maleprob=mtables[1:,1]
maleprob2=list(maleprob)
femprob=mtables[1:,2]
femprob2=list(femprob)

#set defaults for age and new event mortality rate
age=21
EventMortality=0.0
#male=0, female=1
sex=0

def MortalityCalc(age,EventMortality,sex):
    # callback as age changes to return age range, survival probability through that age, 50% survival           
    agerange=np.arange(age-1,101)
    #reset maleprob2 to maleprob
    maleprob2=list(maleprob)
    femprob2=list(femprob)
    if sex:
        mp=([np.prod(femprob[age-1:val]) for val in agerange])[1:]
        femprob2[age-1]=femprob2[age-1]*(1-EventMortality)
        mp2=([np.prod(femprob2[age-1:val]) for val in agerange])[1:]
    else:
        mp=([np.prod(maleprob[age-1:val]) for val in agerange])[1:]
        maleprob2[age-1]=maleprob2[age-1]*(1-EventMortality)
        mp2=([np.prod(maleprob2[age-1:val]) for val in agerange])[1:]
    agerange=agerange[1:]
    # source = ColumnDataSource(data=dict(x=agerange, y=mp))
    # below are all "1+" because age in agerange is current age, age+1 is the first next year to survive to
    m50=1+np.interp(0.5,mp[::-1],agerange[::-1])
    m75=1+np.interp(0.75,mp[::-1],agerange[::-1])
    m25=1+np.interp(0.25,mp[::-1],agerange[::-1])
    m502=1+np.interp(0.5,mp2[::-1],agerange[::-1])
    m752=1+np.interp(0.75,mp2[::-1],agerange[::-1])
    m252=1+ np.interp(0.25,mp2[::-1],agerange[::-1])
    return agerange,mp,mp2,m50,m75,m25,m502,m752,m252

agerange,mp,mp2,MedianAge,Age75,Age25,MA2,A72,A22=MortalityCalc(age,EventMortality,sex)
source = ColumnDataSource(data=dict(x=agerange, y=mp))
#source = ColumnDataSource(data=dict(x=agerange, y1=np.repeat(0,len(mp)), y2=mp))
source2 = ColumnDataSource(data=dict(x=agerange, y1=np.repeat(0,len(mp2)), y2=mp2))
plot = figure(x_range=(0, 100),y_range=(0,1), plot_width=700, plot_height=400,title='Life Expectancy (based on United States Life Tables, 2017 CDC/NVSS)')
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
# plot.varea('x', 'y1','y2', source=source2,fill_color='#CFEBE6')
plot.varea('x', 'y1','y2', source=source2,fill_color='#F4D8D8')
plot.xaxis.ticker = SingleIntervalTicker(interval=10)
plot.xgrid.ticker = SingleIntervalTicker(interval=10)
plot.xaxis.axis_label = "Projected Age"
plot.yaxis.ticker = SingleIntervalTicker(interval=0.25)
plot.ygrid.ticker = SingleIntervalTicker(interval=0.25)
plot.yaxis.axis_label = "Expected Survival rate at projected age"
plot.yaxis.formatter = NumeralTickFormatter(format='0 %')
label50 = Label(x=5, y=0.5, text=('50% probability still alive at age = '+str(np.around(MedianAge,decimals=1))),text_font_size='15px',text_color='#0000E6')
label75 = Label(x=5, y=0.75, text=('75% probability still alive at age = '+str(np.around(Age75,decimals=1))),text_font_size='15px',text_color='#0000E6')
label25 = Label(x=5, y=0.25, text=('25% probability still alive at age = '+str(np.around(Age25,decimals=1))),text_font_size='15px',text_color='#0000E6')
label1y = Label(x=5,y=0.1,text=("1 year survival rate = "+str(np.around(100*mp[0],decimals=2))+"%"),text_font_size='15px',text_color='#0000E6')
label1ya = Label(x=5,y=0.05,text=("reduced to = "+str(np.around(100*mp2[0],decimals=2))+"%"),text_font_size='15px',text_color='#FF0000')
label50a = Label(x=5, y=0.45, text=('reduced to = '+str(np.around(MA2,decimals=1))),text_font_size='15px',text_color='#FF0000')
label75a = Label(x=5, y=0.70, text=('reduced to = '+str(np.around(A72,decimals=1))),text_font_size='15px',text_color='#FF0000')
label25a = Label(x=5, y=0.20, text=('reduced to = '+str(np.around(A22,decimals=1))),text_font_size='15px',text_color='#FF0000')

# label = Label(x=1.1, y=18, text=str(MedianAge), text_font_size='93px', text_color='#eeeeee')
plot.add_layout(label50)
plot.add_layout(label1y)
plot.add_layout(label1ya)
plot.add_layout(label75)
plot.add_layout(label25)
plot.add_layout(label50a)
plot.add_layout(label25a)
plot.add_layout(label75a)

#set up age slider
AgeSlider = Slider(title="Current Age", value=21, start=1, end=99, step=1)
#AgeSlider = Slider(title="Current Age", value=21, start=1, end=99, step=1, orientation = "vertical")
# set up one time mortality slider
EventMortalitySlider = Slider(title="One-time event death rate, %", value=0, start=0, end=10, step=0.1)
#set up gender radio button group
GenderRadioButtons = RadioButtonGroup(labels=["Male", "Female"], active=0)

#set up callback
def update_data(attrname, old, new):
    # Get the current slider values
    age=AgeSlider.value
    EventMortality=0.01*EventMortalitySlider.value
    sex=GenderRadioButtons.active
    # Generate the new results
    agerange,mp,mp2,MedianAge,Age75,Age25,MA2,A72,A22=MortalityCalc(age,EventMortality,sex)
    source.data=dict(x=agerange,y=mp)
    source2.data=dict(x=agerange,y1=np.repeat(0,len(mp2)), y2=mp2)
    label50.text='50% probability still alive at age = '+str(np.around(MedianAge,decimals=1))
    label1y.text="1 year survival rate = "+str(np.around(100*mp[0],decimals=2))+"%"
    label75.text='75% probability still alive at age = '+str(np.around(Age75,decimals=1))
    label25.text='25% probability still alive at age = '+str(np.around(Age25,decimals=1))
    label1ya.text="reduced to = "+str(np.around(100*mp2[0],decimals=2))+"%"
    label50a.text='reduced to = '+str(np.around(MA2,decimals=1))
    label75a.text='reduced to = '+str(np.around(A72,decimals=1))
    label25a.text='reduced to = '+str(np.around(A22,decimals=1))
    
for w in [AgeSlider, EventMortalitySlider]:
    w.on_change('value', update_data)
    
GenderRadioButtons.on_change('active',update_data)  
    
inputs = column(AgeSlider,EventMortalitySlider,GenderRadioButtons)

# layout=row(plot,AgeSlider)
# curdoc().add_root(row(plot, AgeSlider, width=800))
curdoc().add_root(row(inputs,plot))
curdoc().title = "LifeExpectancy"


