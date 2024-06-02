import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate
from datetime import datetime
from app import app
from apps import commonmodule as cm
from apps import dbconnect as db
from dash_iconify import DashIconify as di

# Define the form layout
comms=[
        "Academic Affairs Committee",
        "External Affairs Committee",
        "Finance Committee",
        "Internal Affairs Committee",
        "Membership and Recruitment Committee",
        "Publications and Records Committee"
]
reaffiliation_form = dbc.Form(
    [
        html.H5(html.B('Personal Information')),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "First Name ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='first_name', value='', disabled=False),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Middle Name ",
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='middle_name', disabled=False),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Surname ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='last_name', disabled=False),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Suffix ",
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='suffix', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "ID Number ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='valid_id',
                              placeholder="20XXXXXXX", maxLength=9, disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Birthday ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="date", id='birthdate', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),

        html.Br(),
        html.H5(html.B('Contact Information')),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Contact Number ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='contact_number',
                              placeholder="09XXXXXXXXX", maxLength=11, disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Emergency Contact Number ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='emergency_contact_number',
                              placeholder="09XXXXXXXXX", maxLength=11, disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Email Address ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="email", id='email', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Present Address ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="text", id='present_address', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Permanent Address ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="text", id='permanent_address', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),

        html.Br(),
        html.H5(html.B('Basic Information')),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Degree Program ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='degree_program',
                        options=[
                            {'label': "BS Industrial Engineering", 'value': "BS Industrial Engineering"},
                            {'label': "BS Chemical Engineering", 'value': "BS Chemical Engineering"},
                            {'label': "BS Civil Engineering", 'value': "BS Civil Engineering"},
                            {'label': "BS Computer Science", 'value': "BS Computer Science"},
                            {'label': "BS Computer Engineering", 'value': "BS Computer Engineering"},
                            {'label': "BS Electronics Engineering", 'value': "BS Electronics Engineering"},
                            {'label': "BS Electrical Engineering", 'value': "BS Electrical Engineering"},
                            {'label': "BS Geodetic Engineering", 'value': "BS Geodetic Engineering"},
                            {'label': "BS Mechanical Engineering", 'value': "BS Mechanical Engineering"},
                            {'label': "BS Materials Engineering", 'value': "BS Materials Engineering"},
                            {'label': "BS Metallurgical Engineering", 'value': "BS Metallurgical Engineering"},
                            {'label': "BS Mining Engineering", 'value': "BS Mining Engineering"}
                        ],
                        value='BS Industrial Engineering',
                        searchable=False,
                        clearable=False
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Year Standing ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='year_standing',
                        options=[{'label': str(i), 'value': i} for i in range(1, 6)],
                        value=1,
                        searchable=False,
                        clearable=False
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Membership Type ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='membership_type',
                        options=[{'label': mt, 'value': mt} for mt in ["Regular", "Non-Regular", "Honorary", "Probationary"]],
                        value='Regular',
                        searchable=False,
                        clearable=False
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "App Batch ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='app_batch',
                        options=[{'label': ab, 'value': ab} for ab in ["23B", "23A", "22B", "22A", "21B", "21A", "20B", "20A", "19B", "19A", "18B", "18A"]],
                        value="23B",
                        searchable=False,
                        clearable=False
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "GWA ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='gwa',
                        options=[{'label': str(i), 'value': i} for i in range(1, 6)],
                        value=1,
                        searchable=False,
                        clearable=False
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        html.Br(),
        html.H5(html.B('Committee Prefference')),
        dbc.Row(
            [
                html.P('This is a multi-select dropdown. Select with first being most preferred and last being least preferred'),
                dbc.Col(
                    dcc.Dropdown(id='ranking-dropdown', options=[{'label': choice, 'value': choice} for choice in comms], multi=True,style={'width':'100%'})
                )
            ]
        ),
        html.Br(),
        html.H5(html.B('Reaffiliation Fee')),

        dbc.Row(
            [
                dbc.Col(
                    html.P(
                        "The Finance Committee has decided to set the reaffiliation fee to Php 120. "
                        "Payment of the reaffiliation fee upon submission of reaff form is highly encouraged (but not required) as you will only have to pay ₱100 and get a committee choice priority! "
                        "You may still opt to pay on a later date within the semester and pay ₱120."
                        "You can pay your reaffiliation fee through: "
                        "GCash/Paymaya: 0995 973 6273 (Jericho Joshua De Jesus) "
                        "PNB: 6334 1001 2523 (Jericho Joshua De Jesus) "
                        "For other concerns, you may message Johann Daniel Alvarez or Jericho Joshua De Jesus through Facebook Messenger."
                    ),
                    width={"size": 10, "offset": 1},
                )
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "When will you pay the Reaff Fee? ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='reaff_fee',
                        options=[
                            {'label': "Pay as I Submit the Reaff Form", 'value': "Pay as I Submit the Reaff Form"},
                            {'label': "Pay at a later date", 'value': "Pay at a later date"}
                        ],
                        value='Pay as I Submit the Reaff Form',
                        searchable=False,
                        clearable=False
                    ),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button("Submit", id="submit-button", color="primary", className="mb-3", style={'display': 'none'}),
                    width={"size": 6, "offset": 3}
                )
            ]
        ),
        dbc.Button('Submit', id='reaf-submit'),
        html.Div(id='output-message')  # For displaying output messages
    ]
)

layout = html.Div([
    cm.navigation,
    cm.top,
    html.Div([
        html.Div([
        dbc.Card([
            dbc.CardHeader("REAFFILIATION FORM", class_name='flex'),
            dbc.CardBody([
                dbc.Container(
                    [
                        reaffiliation_form,
                        html.Br(),
                    ], class_name='flex homeshow'
                )
            ]),
    ]),],className='body') 
], className='flex body-container')
        ])


@app.callback(
    [
     Output('first_name', 'value'),
     Output('middle_name', 'value'),
     Output('last_name', 'value'),
     Output('suffix', 'value'),
     Output('valid_id', 'value'),
     Output('birthdate', 'value'),
     Output('contact_number', 'value'),
     Output('emergency_contact_number', 'value'),
     Output('email', 'value'),
     Output('present_address', 'value'),
     Output('permanent_address', 'value'),
     Output('degree_program', 'value'),
     Output('year_standing', 'value'),
     Output('membership_type', 'value'),
     Output('app_batch', 'value'),
     Output('gwa', 'value'),
     Output('reaff_fee', 'value'),
     
     Output('output-message', 'children')
     ],
    [Input('reaf-submit', 'n_clicks')],
    [State('first_name', 'value'),
     State('middle_name', 'value'),
     State('last_name', 'value'),
     State('suffix', 'value'),
     State('valid_id', 'value'),
     State('birthdate', 'value'),
     State('contact_number', 'value'),
     State('emergency_contact_number', 'value'),
     State('email', 'value'),
     State('present_address', 'value'),
     State('permanent_address', 'value'),
     State('degree_program', 'value'),
     State('year_standing', 'value'),
     State('membership_type', 'value'),
     State('app_batch', 'value'),
     State('gwa', 'value'),
     State('reaff_fee', 'value'),
     State('ranking-dropdown','value')]
)
def submit_form(n_clicks, first_name, middle_name, last_name, suffix, valid_id, birthdate, contact_number,
                emergency_contact_number, email, present_address, permanent_address, degree_program,
                year_standing, membership_type, app_batch, gwa, reaff_fee,rank_dd):
    if n_clicks is None:
        raise PreventUpdate
    if not (first_name and last_name and valid_id and birthdate and contact_number and emergency_contact_number and email and present_address and permanent_address and degree_program and year_standing and membership_type and app_batch and gwa and reaff_fee):
        return dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,html.Div("Please fill in all required fields.", style={'color': 'red'})
    
    try:
        # Check if the person already exists
        sql = "SELECT valid_id FROM person WHERE valid_id=%s"
        df = db.querydatafromdatabase(sql, [valid_id], ['valid_id'])

        if df.shape[0]:
            # Update existing person's information
            sql = """
                UPDATE person
                SET
                    first_name=%s,
                    middle_name=%s,
                    last_name=%s,
                    suffix=%s,
                    birthdate=%s,
                    contact_number=%s,
                    emergency_contact_number=%s,
                    email=%s,
                    present_address=%s,
                    permanent_address=%s
                WHERE valid_id=%s
            """
            values = [first_name, middle_name, last_name, suffix, birthdate, contact_number, emergency_contact_number, email, present_address, permanent_address, valid_id]
            db.modifydatabase(sql, values)
            
            # Update affiliation information
            sql = """
                UPDATE affiliation 
                SET 
                    degree_program=%s,
                    membership_type=%s,
                    year_standing=%s,
                    app_batch=%s,
                    gwa=%s,
                    reaff_fee=%s
                WHERE valid_id=%s
            """
            values = [degree_program, membership_type, year_standing, app_batch, gwa, reaff_fee, valid_id]
            db.modifydatabase(sql, values)
            
            message = "Existing member information updated successfully."
        else:
            # Insert new person
            sql = """
            INSERT INTO person(valid_id, first_name, middle_name, last_name, suffix, birthdate, contact_number, emergency_contact_number, email, present_address, permanent_address)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = [valid_id, first_name, middle_name, last_name, suffix, birthdate, contact_number, emergency_contact_number, email, present_address, permanent_address]
            db.modifydatabase(sql, values)
            print('aff')
            # Insert new affiliation
            sql = """
            INSERT INTO affiliation(is_new,valid_id, degree_program, membership_type, year_standing, app_batch, gwa, reaff_fee,comm_firstchoice,comm_secondchoice,comm_thirdchoice, comm_fourthchoice,comm_fifthchoice, comm_sixthchoice)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = [True,valid_id, degree_program, membership_type, year_standing, app_batch, gwa, reaff_fee,rank_dd[0] if len(rank_dd)>0 else '',rank_dd[1] if len(rank_dd)>1 else '',rank_dd[2] if len(rank_dd)>2 else '',rank_dd[3] if len(rank_dd)>3 else '',rank_dd[4] if len(rank_dd)>4 else '',rank_dd[5] if len(rank_dd)>5 else '']
            db.modifydatabase(sql, values)
            #insert as member
            print('ednaff')
            sql="""
                INSERT INTO upciem_member(valid_id,active_status) VALUES(%s,'Active')
            """
            values=[valid_id]
            db.modifydatabase(sql,values)
            message = "New member successfully added."

        return '','','','','','','','','','','','','','','','','',html.Div(message, style={'color': 'green'})

    except Exception as e:
        return dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,html.Div(f"An error occurred: {str(e)}", style={'color': 'red'})

