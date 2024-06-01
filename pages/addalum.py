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
                    dbc.Input(type="text", id='email', disabled=False),
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
                            "BS Industrial Engineering",
                            "BS Chemical Engineering",
                            "BS Civil Engineering",
                            "BS Computer Science",
                            "BS Computer Engineering",
                            "BS Electronics Engineering",
                            "BS Electrical Engineering",
                            "BS Geodetic Engineering",
                            "BS Mechanical Engineering",
                            "BS Materials Engineering",
                            "BS Metallurgical Engineering",
                            "BS Mining Engineering"],
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
                        options=[1,2,3,4,5],
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
                        options=["Regular","Non-Regular","Honorary","Probationary"],
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
                        options=["23B", "23A", "22B", "22A", "21B", "21A", "20B", "20A", "19B", "19A", "18B", "18A"],
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
                        "GWA ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='gwa',
                        options=[1,2,3,4,5],
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
        html.H5(html.B('Reaffiliation Fee')),

        dbc.Row(
            [
                "The Finance Committee has decided to set the reaffiliation fee to Php 120."
                
                "Payment of the reaffiliation fee upon submission of reaff form is highly encouraged (but not required) as you will only have to pay ₱100 and get a committee choice priority! You may still opt to pay on a later date within the semester and pay ₱120."

                "You can pay your reaffiliation fee through:"
                "GCash/Paymaya: 0995 973 6273 (Jericho Joshua De Jesus)"
                "PNB: 6334 1001 2523 (Jericho Joshua De Jesus)"

                "For other concerns, you may message Johann Daniel Alvarez or Jericho Joshua De Jesus through Facebook Messenger."
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
                            "Pay as I Submit the Reaff Form",
                            "Pay at a later date"
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

    ]
)

layout = html.Div([
    cm.navigation,
    cm.top,
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
            dbc.CardFooter(
                [
                    dbc.Button([di(icon='mingcute:facebook-line', inline=True), dbc.Label("Facebook Page")], href="https://www.facebook.com/upciem", external_link=True),
                    dbc.Button([di(icon='bi:instagram', inline=True), dbc.Label("Instagram")], href="https://www.instagram.com/upciem/", external_link=True),
                    dbc.Button([di(icon='iconoir:twitter', inline=True), dbc.Label("Twitter")], href="https://twitter.com/upciem", external_link=True),
                    dbc.Button([di(icon='lucide:linkedin', inline=True), dbc.Label("LinkedIn")], href="https://ph.linkedin.com/company/upciem1976", external_link=True),
                ], style={'display': 'flex', 'justify-content': 'space-evenly'}
            )
        ])
    ], className="body"),
], className='flex body-container')