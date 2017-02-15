> php中为什么trait不能实现interface? 有时候，我们可能会需求使用我们的trait T的所有class都必须实现某interface I,毕竟在每个class中implement I 总没有使用 trait T implements I {} 方便。

#### 具体代码

```
<?php
interface I {
    function foo();
}
trait T implements I {
    function foo() {
    }
}
class C {
    use T;
}
```

要弄明白这个问题，首先要理解interface和trait都是什么。

interface是class的一个约束条件，指定某个class必须实现哪些方法，但不需要定义这些方法的具体内容。

trait出现的比interface要晚，官方定义是：[自 PHP 5.4.0 起，PHP 实现了一种代码复用的方法，称为 trait。Trait 是为类似 PHP 的单继承语言而准备的一种代码复用机制。Trait 为了减少单继承语言的限制，使开发人员能够自由地在不同层次结构内独立的类中复用 method。Trait 和 Class 组合的语义定义了一种减少复杂性的方式，避免传统多继承和 Mixin 类相关典型问题。](https://secure.php.net/manual/zh/language.oop5.traits.php)

简单来说：Trait是部分class的实现，让我们能将部分class注入到其他class。

trait有两个功能 :

1. 提供如interface的。
1. 提供如class的实现。

所以trait是一个看起来像interface，但用起来像class的东西。

我们来看一下，php是如何实现trait的。

在php中当使用Trait时，只是告诉编译器将Trait中的代码复制并粘贴到正在使用的类中，因为interface必须在类外面，所以就不能在trait中实现有关interface的代码了。

 Traits实际上只是一个语言结构（告诉编译器将trait代码复制并粘贴到此类中），而不是可以由代码引用的对象或类型，所以trait也不能被实例化。

综上，如果想在代码中每个类使用我的trait都必须实现相应的接口，确实不怎么简单。

不过还可以通过使用抽象类来实现，以使用trait然后从它扩展类。

#### 具体参考代码

```
interface SomeInterface{
    public function someInterfaceFunction();
}

trait SomeTrait {
    function sayHello(){
        echo "Hello my secret is ".static::$secret;
    }
}

abstract class AbstractClass implements SomeInterface{
    use SomeTrait;
}

class TestClass extends AbstractClass {
    static public  $secret = 12345;

    function someInterfaceFunction(){
        # some code
    }
}

$test = new TestClass();

$test->sayHello();
```
