export const LoginProps = [
    {
        key: "username",
        label: "Username",
        type: "string",
        max_len: 50,
        regex_exp: /^[A-Za-z0-9_@$#]+$/,
        reason: "Please add the proper Username"
    },
    {
        key: "password",
        label: "Password",
        type: "password",
        max_len: 50,
        regex_exp: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,15}$/,
        reason: "1 capital letter, 1 small letter, 1 number and min length of 8 "
    }
]

export const SignUpProps = [
    {
        key: "name",
        label: "Name",
        type: "string",
        max_len: 50,
        regex_exp: /^[A-Za-z ]+$/,
        reason: "Please add the proper name"
    },
    {
        key: "email",
        label: "Email",
        type: "string",
        max_len: 50,
        regex_exp: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
        reason: "Please add the proper email"
    },
    {
        key: "username",
        label: "Username",
        type: "string",
        max_len: 50,
        regex_exp: /^[A-Za-z0-9_@$#]+$/,
        reason: "Please add the proper username"
    },
    {
        key: "password",
        label: "Password",
        type: "password",
        max_len: 50,
        regex_exp: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,15}$/,
        reason: "1 capital letter, 1 small letter, 1 number and min length of 8."
    },
    {
        key: "confirm_password",
        label: "Confirm password",
        type: "password",
        max_len: 50,
        regex_exp: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,15}$/,
        reason: "1 capital letter, 1 small letter, 1 number and min length of 8."
    },
]