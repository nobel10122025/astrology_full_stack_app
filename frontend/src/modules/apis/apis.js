const backend_endpoint = "http://127.0.0.1:5000"
export const generate_horoscope = (payload) => {
    return fetch(`${backend_endpoint}/get_house_details`, 
        {
            method: "POST", 
            body: JSON.stringify(payload),
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json;charset=UTF-8'
            },
            mode: 'cors',
        })
}