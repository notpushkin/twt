twt
====

**The Whiespace Thing: indentaion-based blocks for any language.**

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
    console.log("Hello, ", a, "!")
}

class Polygon {
    constructor(height, width) {
        this.height = height
        this.width = width
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

becomes:

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
