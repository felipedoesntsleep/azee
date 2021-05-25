// const functions = require('firebase-functions');

// // The Firebase Admin SDK to access Firestore.
// const admin = require('fi

import {firebase} from "firebase/app";
import "firebase/database";


var database = firebase.database();

function writeUserData(userId, name, email, imageUrl) {
    var postData = {
        uid: userId,
        name: name,
        email: email,
        imageUrl: imageUrl,
      };
    
      // Get a key for a new Post.
      var newPostKey = firebase.database().ref().child('posts').push().key;
    
      // Write the new post's data simultaneously in the posts list and the user's post list.
      var updates = {};
      updates['/posts/' + newPostKey] = postData;
      updates['/user-posts/' + uid + '/' + newPostKey] = postData;
    
      return firebase.database().ref().update(updates);
  }

  let updateButton = document.getElementById("update");
  updateButton.addEventListener('click', function(){
      console.log("in button");
      writeUserData(1, "felipe420", "email", "image");
  });