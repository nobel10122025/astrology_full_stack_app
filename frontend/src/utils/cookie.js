import Cookies from "universal-cookie";

function checkCookieEnabled() {
    if (typeof window !== "undefined" && window.document && navigator && navigator.cookieEnabled) {
        return true;
    } else {
        return false;
    }
}

function getCookie(key, cookieOptions = {}) {
    let value = null;
    if (checkCookieEnabled()) {
        const cookies = new Cookies();
        value = cookies.get(key, cookieOptions);
        if (value && value !== "null") return value;
    }
    return value;
}

function setCookie(key, value, expiryDate = false) {
    try {
        const cookies = new Cookies();
        if (expiryDate) {
            cookies.set(key, value, {
                maxAge: expiryDate,
            });
        } else cookies.set(key, value);
        return true;
    } catch {
        return false;
    }
}

function deleteCookie(key, isDeletePath) {
    try {
        const cookies = new Cookies();
        if (isDeletePath) {
            cookies.remove(key, {
                path: constants.cookieDetails.path,
                maxAge: 0,
                domain: constants.cookieDetails.domain,
                expires: new Date(1990, 1, 1, 1, 1, 1, 1),
            });
        } else cookies.remove(key);
        return true;
    } catch {
        return false;
    }
}

export default {
    checkCookieEnabled,
    getCookie,
    setCookie,
    deleteCookie,
};
