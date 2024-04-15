import { Api } from './Api'

interface Register {
    nazwa_uzytkownika: string;
    email: string;
    haslo: string;
}

export default {
    register(credentials: Register) {
        return Api().post('/register', credentials);
    }
}