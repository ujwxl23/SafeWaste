import { initializeApp } from "firebase/app";
import { getDatabase, ref , set} from "firebase/database"; 

const firebaseConfig = {
    'apiKey': "AIzaSyAj14TDiqs8txI5vnY5jWfkHiPsvbIqMOU",
    'authDomain': "fir-718ed.firebaseapp.com",
    'databaseURL':"https://fir-718ed-default-rtdb.firebaseio.com/",
    'projectId': "fir-718ed",
    'storageBucket': "fir-718ed.appspot.com",
    'messagingSenderId': "374081504573",
    'appId': "1:374081504573:web:153d18a9e9ad2d9598f154",
    'measurementId': "G-JQVKR5SZB5"
};

const app =initializeApp(firebaseConfig);

function writeUserData(userId, name, email, imageUrl) {
    const db = getDatabase();
    const reference = ref(db, 'user/' + userId);

    set(reference, {
        username: name,
        email: email,
        profile_picture : imageUrl
    });
}

writeUserData("andreawu","awu","myemail@me.com","myimageurl");