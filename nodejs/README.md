# 设置国内安装源

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
npm config set registry https://registry.npm.taobao.org
```

---

# javascript call apply bind

this是javascript的一个关键字，随着函数使用场合不同，this的值会发生变化。但是总有一个原则，那就是this指的是调用函数的那个对象。  
this一般指向的是当前被调用者，但也可以通过其它方式来改变它的指向，下面将介绍三种方式：  
1.call用作继承时：

```
function Parent(age){
this.name=['mike','jack','smith'];
this.age=age;
}
function Child(age){
Parent.call(this,age);//把this指向Parent,同时还可以传递参数
}
var test=new Child(21);
console.log(test.age);//21
console.log(test.name);
test.name.push('bill');
console.log(test.name);//mike,jack,smith,bill
```

2.call和apply都可以改变this指向，不过apply的第二个参数是散列分布，call则可以是一个数组

```
console.log(Math.max.apply(null,[1,2,3,4]));//4
```

apply\(\) 方法接收两个参数：一个是在其中运行函数的作用域，另一个是参数数组。其中，第二个参数可以是 Array 的实例，也可以是arguments 对象。call\(\) 方法与 apply\(\) 方法的作用相同，它们的区别仅在于接收参数的方式不同。对于 call\(\)  
方法而言，第一个参数是 this 值没有变化，变化的是其余参数都直接传递给函数。换句话说，在使用call\(\) 方法时，传递给函数的参数必须逐个列举出来。  
3.ES5还定义了一个方法：bind\(\)，它会创建一个函数的实例，其this值会被绑定到传给bind\(\)函数的值。如

```
window.color='red';
var o={color:'blue'};

function sayColor(){
    console.log(this.color);
}
var objectSaycolor=sayColor.bind(o);
//var objectSaycolor=sayColor.bind();
objectSaycolor();//blue
```

在这里sayColor\(\)调用bind\(\)并传入对象o,创建了objectSayColor\(\)函数。objectSayColor\(\)函数的this值等于o,因此即使是在全局作用域中调用这个函数，也会看到blue。  
以上所述是小编给大家介绍的JS中改变this指向的方法\(call和apply、bind\)，希望对大家以上帮助！  
下面还有点时间给大家补充点基础知识有关：call\(\)与apply\(\)区别  
一、方法的定义  
call方法:  
语法：call\(thisObj，Object\)  
定义：调用一个对象的一个方法，以另一个对象替换当前对象。  
说明：  
call 方法可以用来代替另一个对象调用一个方法。call 方法可将一个函数的对象上下文从初始的上下文改变为由 thisObj 指定的新对象。   
如果没有提供 thisObj 参数，那么 Global 对象被用作 thisObj。  
apply方法：  
语法：apply\(thisObj，\[argArray\]\)  
定义：应用某一对象的一个方法，用另一个对象替换当前对象。  
说明：  
如果 argArray 不是一个有效的数组或者不是 arguments 对象，那么将导致一个 TypeError。   
如果没有提供 argArray 和 thisObj 任何一个参数，那么 Global 对象将被用作 thisObj， 并且无法被传递任何参数。  
代码示例：

```
function Animal(name) {
   this.name = name;
   this.showName = function() {
     console.log(this.name);
   };
 }
 function Cat(name) {
   Animal.call(this, name);
 }
 Cat.prototype = new Animal();
 function Dog(name) {
   Animal.apply(this, name);
 }
 Dog.prototype = new Animal();
 var cat = new Cat("Black Cat"); //call必须是object
 var dog = new Dog(["Black Dog"]); //apply必须是array
 cat.showName();
 dog.showName();
 console.log(cat instanceof Animal);
 console.log(dog instanceof Animal);
```

模拟call, apply的this替换

```
function Animal(name) {
  this.name = name;
  this.showName = function() {
    alert(this.name);
  };
};
function Cat(name) {
  this.superClass = Animal;
  this.superClass(name);
  delete superClass;
}
var cat = new Cat("Black Cat");
cat.showName();
```

---



