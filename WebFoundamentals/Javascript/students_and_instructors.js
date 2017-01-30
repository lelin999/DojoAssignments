 var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];

var simpleOutput = function (arr) {
	for (var i = 0; i < arr.length; i++) {
		console.log(arr[i].first_name + " " + arr[i].last_name);
	}
};

simpleOutput(students);

var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 };

 var harderOutput = function (obj) {
 	for (var prop in obj) {
 		console.log(prop);
 		for (var i = 0; i < obj[prop].length; i++) {
 			console.log(i + ' - ' + (obj[prop][i].first_name + " " + obj[prop][i].last_name).toUpperCase() + ' - ' + (obj[prop][i].first_name + obj[prop][i].last_name).length);
 		}
 	}
 };

 harderOutput(users);