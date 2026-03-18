// ─────────────────────────────────────────────
//  auth.js  —  Firebase auth + backend sync
// ─────────────────────────────────────────────

const firebaseConfig = {
    apiKey: "AIzaSyDU8Ug5BiFzAocXXAuLIgD6aUI-oKUf-CE",
    authDomain: "benefitai.firebaseapp.com",
    projectId: "benefitai",
    storageBucket: "benefitai.firebasestorage.app",
    messagingSenderId: "949080252632",
    appId: "1:949080252632:web:f5930b6ad70896e7e777ad",
    measurementId: "G-S6KDVW4VV3",
};

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}
const auth = firebase.auth();

/**
 * After Firebase auth succeeds, sync the user into our backend
 * and follow the redirect the backend returns.
 */
async function syncWithBackend(user) {
    try {
        const data = await apiFetch("/firebase-login", {
            method: "POST",
            body: JSON.stringify({
                email: user.email,
                name: user.displayName || user.email.split("@")[0],
                uid: user.uid,
            }),
        });
        if (data.status === "success") handleRedirect(data.redirect);
        else showMessage(data.message);
    } catch (err) {
        showMessage("Failed to connect to backend: " + (err.message || JSON.stringify(err)));
    }
}
