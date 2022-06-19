function main() {
    var depth = parseInt(readLine(), 10);
    //your code goes here
    var counter = 0 ;
    var d = 0 ;
    while (d <= depth) {
        d += 7 ;
        if (d > depth) {
            counter++ ;
            break ;
        }
        d -= 2 ;
        counter ++ ;
    }
    console.log(counter) ;

    
    
}
