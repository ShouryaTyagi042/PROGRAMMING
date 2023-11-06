# var,let,const
IIFEs prevent pollution of the global JS scope. In a traditional function, if you create a variable within the function, it is accessible in the global object. If you define a variable in an IIFE, it is accessible only directly within the function. 

The scope is the current context of execution in which values and expressions are "visible" or can be referenced

```JavaScript
{
  var x = 1;
}
console.log(x); // 1
```

# Closures

The module pattern allows you to split up your code into smaller, reusable pieces. Besides being able to split your code into smaller reusable pieces, modules allow you to keep certain values within your file private. Declarations within a module are scoped (encapsulated) to that module , by default.

A “higher-order function” is a function that accepts functions as parameters and/or returns a function.

# Objects
In the first implementation of JavaScript, JavaScript values were represented as a type tag and a value. The type tag for objects was 0. null was represented as the NULL pointer (0x00 in most platforms). Consequently, null had 0 as type tag, hence the typeof return value "object".

Spread operator clones the object 

