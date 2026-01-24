import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.4/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCLok8BHG6i4gQppuJZQu4pzUDTvcZva9M",
  authDomain: "game-credentials-67d37.firebaseapp.com",
  projectId: "game-credentials-67d37",
  storageBucket: "game-credentials-67d37.firebasestorage.app",
  messagingSenderId: "929391853931",
  appId: "1:929391853931:web:f80633f2bc491a7bb10c2e",
  measurementId: "G-G4DS24Z00T"
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
