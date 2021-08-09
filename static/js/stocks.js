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
  
  
  
  
  
  
    document.querySelector(".Stock-form").addEventListener("submit", submitForm);
    
    function submitForm(e) {
      e.preventDefault();
    
  
      let s1= document.querySelector(".s1").value;
      let s2 = document.querySelector(".s2").value;
      let s3 = document.querySelector(".s3").value;
      
    
      console.log( s1,s2,s3);
    
      var newData = {
        s1: s1,
        s2: s2,
        s3: s3
        
    }
    var firebaseRef = firebase.database().ref('Stocks/')
    firebaseRef.update(newData)
      alert("Your Message has been sent Successfully. Thank You!");
     
    }
    
  