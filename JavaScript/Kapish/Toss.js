var tails = 0 ;
var head = 0 ;
function toss() {
    // alert("Function is runing") ;
    var option = Math.floor(Math.random() * 2);
    if (option== 1) {
        head++ ;
    }
    else{
        tails++ ;
    }
    var total = head + tails ;
    var Hpercent = 100 * head / total ;
    var Tpercent = 100 * tails / total ;
    document.getElementById("Fheads").innerHTML = head ;
    document.getElementById("Ftails").innerHTML = tails ;
    document.getElementById("Pheads").innerHTML = Hpercent ;
    document.getElementById("Ptails").innerHTML = Tpercent ;



}