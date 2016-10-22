twt
====

**The Whitespace Thing: indentation-based blocks for any language.**

Example:

```js
function hello(a):
    console.log("Hello, ", a, "!")

class Polygon:
    constructor(height, width):
        this.height = height
        this.width = width
```

becomes:

```js
function hello(a) {
    console.log("Hello, ", a, "!");
}

class Polygon {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
}
```

---

```go
import "math"

type Shape interface:
    Area() float64

type Square struct:
    // Note: no "implements" declaration
    side float64
```

becomes (with `insert_semi=False`):

```go
import "math"

type Shape interface {
    Area() float64
}

type Square struct {
    // Note: no "implements" declaration
    side float64
}
```

---

Want to put an end to Ruby's `end`s?

```rb
hash.each_pair do |key, value|:
  puts "#{key} is #{value}"
```

becomes (`block_begin="", block_end="end", insert_semi=False`):

```rb
hash.each_pair do |key, value|
  puts "#{key} is #{value}"
end
```
