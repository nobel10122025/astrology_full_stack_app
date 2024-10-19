export const createPayload = (userRes) => {
    const date = userRes["date"]
    const time = userRes["time"]
    const payload = {
        year: parseInt(date.split("-")[2]),
        month: parseInt(date.split("-")[1]),
        date: parseInt(date.split("-")[0]),
        hours: parseInt(time.split(":")[0]),
        minutes: parseInt(time.split(":")[1]),
        seconds: parseInt(time.split(":")[2]),
        latitude: parseFloat(userRes['lat']),
        longitude: parseFloat(userRes['long'])
    }
    return payload
}

export const payload_constants =  {
    "timezone": 5.5,
    "settings": {
    "observation_point": "topocentric",
    "ayanamsha": "lahiri"
    }
}

export const chart_color_constants = {
    "chart_config": {
        "font_family": "Mallanna", /* Mallanna / Roboto */
        "hide_time_location": "False", /* True / False */
        "hide_outer_planets": "False", /* True / False */
        "chart_style": "south_india", /* south_india / north_india */
        /*"sign_number_font_color":"#A5243D", */ /* works for north_india chart only */
        "native_name_font_size": "20px",
        "native_details_font_size": "15px",
        "chart_border_width": 1,
        "planet_name_font_size": "20px",
        "chart_heading_font_size": "25px",
        "chart_background_color": "#FEE1C7",
        "chart_border_color": "#B5A886",
        "native_details_font_color": "#000",
        "native_name_font_color": "#231F20",
        "planet_name_font_color": "#BC412B",
        "chart_heading_font_color": "#2D3319",
        "native_name": ""
    }
}