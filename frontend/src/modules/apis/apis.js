const backend_endpoint = "http://127.0.0.1:5000"
export const generate_horoscope = (payload) => {
    return fetch(`${backend_endpoint}/generate_horoscope`, 
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

export const get_cities_list = (query) => {
    const search = new URLSearchParams(query);
    return fetch(`${backend_endpoint}/cities?${search.toString()}`, 
        {
            method: "GET", 
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json;charset=UTF-8'
            },
            mode: 'cors',
        })
}

export const get_auth_token = (payload) => {
    return fetch(`${backend_endpoint}/login`, 
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

export const set_sign_up = (payload) => {
    return fetch(`${backend_endpoint}/register`, 
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