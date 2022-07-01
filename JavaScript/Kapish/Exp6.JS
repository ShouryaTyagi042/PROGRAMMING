function getSeries() {
    var input = parseInt(prompt("Enter your desired number")) ;
    var output = "" ;
    while (input > 0) {
        var digit = input % 10 ;
        var add = " " + digit ;
        output += add ;
        input = parseInt(input/10);
    }
    var splitstring = output.split("");
    var revstring = splitstring.reverse("") ;
    var joinarray = revstring.join("") ;

    alert("Your series is "+joinarray) ;

    // alert("Your Series is " + output) ;
    
}