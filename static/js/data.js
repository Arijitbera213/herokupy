// Initialize Firebase
// Initialize Firebase
var firebaseConfig = {
  apiKey: "AIzaSyBR5ADeIWMZ0YUSPhvCMT_IISCa-cmb4EE",
  authDomain: "stock-data-fc41e.firebaseapp.com",
  projectId: "stock-data-fc41e",
  storageBucket: "stock-data-fc41e.appspot.com",
  messagingSenderId: "31054906120",
  appId: "1:31054906120:web:6a511eb07276159eb0a2bd"
};
firebase.initializeApp(firebaseConfig);


  let contactInfo = firebase.database().ref("Analysis/");




  document.querySelector(".Date-form").addEventListener("submit", submitForm);
  
  function submitForm(e) {
    e.preventDefault();
  

    let sy= document.querySelector(".sy").value;
    let ey = document.querySelector(".ey").value;
    let sm= document.querySelector(".sm").value;
    let em = document.querySelector(".em").value; 
    let sd= document.querySelector(".sd").value;
    let ed = document.querySelector(".ed").value;
  
    console.log( sy,ey,sm,em,sd,ed);
  
    var newData = {
      sy: sy,
      ey: ey,
      sm: sm,
      em: em,
      sd: sd,
      ed: ed
  }
  var firebaseRef = firebase.database().ref('Analysis/')
  firebaseRef.update(newData)
    alert("Your Message has been sent Successfully. Thank You!");
   
  }
  
