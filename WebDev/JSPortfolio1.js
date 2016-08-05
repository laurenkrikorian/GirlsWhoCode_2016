function initAlert() {
	alert("Welcome! Your are about to view a list of projects made by Lauren Krikorian.");
}

function changePicture() {
	var pic = document.getElementById("picture");
	if (pic.src.match("giraffe2")) {
		pic.src = "obamagiraffe.jpg";
	}
	else {
		pic.src = "giraffe2.jpg";
	}	
}

function aboutMe(){
	var ah3 = document.getElementById("clickThis");
	var info = document.getElementById("showUp");
	info.style.display = "block";
}
function enlarge(){
	document.getElementById("bigger").height = '250px';
	document.getElementById("bigger").width = '500px';
}