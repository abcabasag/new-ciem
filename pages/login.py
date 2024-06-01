from dash_iconify import DashIconify as di
from dash import html
from apps import commonmodule as cm
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from datetime import datetime
import dash_bootstrap_components as dbc
from app import app
layout=html.Div([
        dbc.Card([
            dbc.CardBody(
                [
                html.Div([
                    dbc.CardHeader(html.H1("LOGIN")),
                        dbc.Input(id='uname', type='text', className='input', placeholder='Username'),
                        dbc.Input(type='password', id='pword', className='input', placeholder='Password'),
                        html.H4(id='errormessage', className='error'),
                        dbc.Button('Log In', id='submit-val', className='loginbutton', n_clicks=0),

                ],className='half left'),
                html.Div([
                     dbc.Carousel(
                    items=[
                        {"key": "1", "src": "/assets/A1.jpg"},
                        {"key": "2", "src": "/assets/A2.jpg"},
                        {"key": "3", "src": "/assets/A3.jpg"},
                        {"key": "4", "src": "/assets/A4.jpg"},
                        {"key": "5", "src": "/assets/A5.jpg"},
                        {"key": "6", "src": "/assets/A6.jpg"},
                        {"key": "7", "src": "/assets/A7.jpg"},
                        {"key": "8", "src": "/assets/A8.jpg"},
                        {"key": "9", "src": "/assets/A79.jpg"},
                    ],
                    controls=False,
                    indicators=False,
                    interval=1000,
                    ride="carousel",
                    style={'aspect-ratio':'16/9','height':'450px','overflow-y':'hidden'})
                ],className='half')
                ],
            ),
        ], class_name='flex small')
    ],className='FullScreen')

@app.callback(
    [Output('errormessage','children'),Output('login-auth','data')],
    [Input('submit-val','n_clicks')],
    [State('uname','value'),State('pword','value')]
)
def try_log(submit,uname,pword):
    if submit>0: 
                    print('This is triggered')
                    sql="SELECT account_password FROM user_account WHERE user_name="
                    if uname:
                        sql+="'"+uname+"'"
                    else:
                        sql+='0'
                    print(sql)
                    values=[]
                    cols=['pass']
                    df = db.querydatafromdatabase(sql, values, cols)
                    if df.shape[0]:
                        if (df['pass'][0]==pword):
                            print('authenticated')
                            return dash.no_update,{'isAuthenticated':True,'acc':uname}
                        else:
                            return ["Account or Password mismatch"],dash.no_update
    raise PreventUpdate