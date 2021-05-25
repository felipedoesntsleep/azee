        // Initialize Firebase
        // TODO: Replace with your project's customized code snippet
        var config = {
            apiKey: "<API_KEY>",
            authDomain: "azee-614e8.firebaseapp.com",
            databaseURL: "https://azee-614e8-default-rtdb.firebaseio.com/",
            // storageBucket: "<BUCKET>.appspot.com",
            // messagingSenderId: "<SENDER_ID>",
          };
          firebase.initializeApp(config);
        
          // Get a reference to the database service
          var database = firebase.database();
          console.log("start");
          var uid = firebase.auth().currentUser;
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
        
          // update the variable when the starCount is changed in the database
          // var starCountRef = database.ref('posts/' + postId + '/starCount');
          // starCountRef.on('value', function(snapshot) {
          //   updateStarCount(postElement, snapshot.val());
          // });
        
          // // update the UI
          // function updateStarCount(el, val) {
          //   el.innerHtml(`${val} Stars!`);
          // }