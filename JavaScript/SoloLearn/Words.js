class Add {
    constructor(...words) {
        this.words = words;
    }
    print() {
      let txt = "$" ;
      for (let v in this.words) {
        txt += v + "$" ;
        console.log(txt) ;
      }
    }
  
  }
  
  
  var x = new Add("hehe", "hoho", "haha", "hihi", "huhu");
  var y = new Add("this", "is", "awesome");
  var z = new Add("lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit");
  x.print();
  y.print();
  z.print();