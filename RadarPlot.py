import webbrowser

# Create the HTML content

def Radar(data,mode):
    if mode == 'r':
        data_string = """
                var data = [[       { axis: "Health", value:"""+f'{data[0]}'+""" },
                                    { axis: "Education", value:"""+f'{data[1]}'+""" },
                                    { axis: "Entertainment", value:"""+f'{data[2]}'+""" },
                                    { axis: "Business", value:"""+f'{data[3]}'+""" },
                                    { axis: "Lifestyle", value:"""+f'{data[4]}'+""" },
                                ]
                                ];
                var color = d3.scale.ordinal()
                    .range(['#39FF14']);
                """
    elif mode=='s':   
        data_string = """
                var data = [
                                [
                                    { axis: "Negative", value:"""+f'{data[0]}'+""" },
                                    { axis: "Neutral", value:"""+f'{data[1]}'+""" },
                                    { axis: "Positive", value:"""+f'{data[2]}'+""" }
                                ]
                                ];
                var color = d3.scale.ordinal()
                    .range(["#EDC951"]);
                """

    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/ >
            <title>Smoothed D3.js Radar Chart</title>

            <!-- Google fonts -->
            <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>

            <!-- D3.js -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js" charset="utf-8"></script>
            
            <style>
                body {
                    font-family: 'Open Sans', sans-serif;
                    font-size: 11px;
                    font-weight: 300;
                    fill: #dce4ee; /* Text color */
                    text-align: center;
                    text-shadow: 0 0 3px rgba(255, 255, 255, 0.2), 0 0 3px rgba(255, 255, 255, 0.2); /* Adjusted text shadow for dark theme */
                    cursor: default;
                    background-color: #333333; /* Background color */
                }

                .legend {
                    font-family: 'Raleway', sans-serif;
                    fill: #dce4ee; /* Text and plot color */
                }

                .tooltip {
                    fill: #dce4ee; /* Text and plot color */
                }

            </style>
        
        </head>
        <body>

            <div class="radarChart"></div>

            <script src="radarChart.js"></script>	
            <script>
        
        /* Radar chart design created by Nadieh Bremer - VisualCinnamon.com */
        
                ////////////////////////////////////////////////////////////// 
                //////////////////////// Set-Up ////////////////////////////// 
                ////////////////////////////////////////////////////////////// 

                var margin = {top: 20, right: 20, bottom: 20, left: 20},
                width = 281 - margin.left - margin.right,
                height = 151 - margin.top - margin.bottom;
                            
                ////////////////////////////////////////////////////////////// 
                ////////////////////////// Data ////////////////////////////// 
                ////////////////////////////////////////////////////////////// 
    """+data_string+"""
                    
                var radarChartOptions = {
                w: width,
                h: height,
                margin: margin,
                maxValue: 0.5,
                levels: 5,
                roundStrokes: true,
                color: color
                };
                //Call function to draw the Radar chart
                RadarChart(".radarChart", data, radarChartOptions);
            </script>
        </body>
    </html>
    """

    # Write the HTML content to an HTML file
    if mode=='r':
        with open('radar_chart_R.html', 'w') as html_file:
            html_file.write(html_content)

    elif mode=='s':
        with open('radar_chart_S.html', 'w') as html_file:
            html_file.write(html_content)
'''
Radar([3, 2, 1],mode='s')
Radar([0.15904396772384644, 0.1771761178970337, 0.2583504915237427, 0.22244824469089508, 0.1829812228679657],mode='r')
'''