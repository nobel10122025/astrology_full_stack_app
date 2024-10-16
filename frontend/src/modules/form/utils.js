export const createPayload = (userRes) => {
    const date = userRes["date"]
    const dateOnly = date.split(" ")
    const payload = {
        year: parseInt(dateOnly[0].split("-")[2]),
        month: parseInt(dateOnly[0].split("-")[1]),
        date: parseInt(dateOnly[0].split("-")[0]),
        hours: parseInt(dateOnly[1].split(":")[0]),
        minutes: parseInt(dateOnly[1].split(":")[1]),
        seconds: parseInt(dateOnly[1].split(":")[2]),
        latitude: parseInt(userRes['lat']),
        longitude: parseInt(userRes['long'])
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