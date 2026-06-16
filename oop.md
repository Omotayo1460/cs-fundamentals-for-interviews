# 🧩 Object-Oriented Programming — Interview Q&A

[← Back to index](README.md) · Related: [OS](operating-systems.md) · [DBMS](dbms.md) · [Networks](computer-networks.md)

---

## Core concepts (1-line each)

- **OOP** models software as objects that bundle **data** (attributes) and **behavior** (methods).
- **Class** = a blueprint; **object** = an instance of a class.

---

## Top questions

**1. What are the four pillars of OOP?**
- **Encapsulation** — bundle data + methods, hide internals behind an interface.
- **Abstraction** — expose *what* something does, hide *how*.
- **Inheritance** — a class derives properties/behavior from another.
- **Polymorphism** — one interface, many forms (same call, different behavior).

**2. Encapsulation vs Abstraction?**
Encapsulation is about **hiding data** (access modifiers, getters/setters).
Abstraction is about **hiding complexity/implementation** (abstract classes, interfaces).
Encapsulation = how; abstraction = what.

**3. Overloading vs Overriding?**
- **Overloading** (compile-time / static polymorphism) — same method name, different
  parameters, same class.
- **Overriding** (run-time / dynamic polymorphism) — subclass redefines a parent method
  with the same signature.

**4. Abstract class vs Interface?**
- **Abstract class** — can have both abstract and concrete methods, fields, constructors;
  single inheritance; use for "is-a" with shared code.
- **Interface** — a contract of method signatures (modern languages allow defaults);
  multiple inheritance of type; use to define capability ("can-do").

**5. Compile-time vs Run-time polymorphism?**
Compile-time = method **overloading** (resolved by the compiler). Run-time = method
**overriding** (resolved via dynamic dispatch / virtual table at execution).

**6. Types of inheritance?**
Single, Multilevel, Hierarchical, Multiple (via interfaces in Java/C#), and Hybrid.
Multiple class inheritance causes the **diamond problem** — solved by interfaces or C++'s
virtual inheritance.

**7. What is the diamond problem?**
When a class inherits from two classes that share a common base, the compiler can't decide
which path to use. Java avoids it (no multiple class inheritance); C++ uses virtual base
classes.

**8. Association vs Aggregation vs Composition?**
- **Association** — a general "uses-a" relationship.
- **Aggregation** — "has-a", weak ownership; parts can outlive the whole (Team ↔ Players).
- **Composition** — "has-a", strong ownership; parts die with the whole (House ↔ Rooms).

**9. What are the SOLID principles?**
- **S**ingle Responsibility — one reason to change.
- **O**pen/Closed — open for extension, closed for modification.
- **L**iskov Substitution — subtypes must be usable as their base type.
- **I**nterface Segregation — many small interfaces over one fat one.
- **D**ependency Inversion — depend on abstractions, not concretions.

**10. Constructor vs Method? Constructor overloading?**
A **constructor** initializes a new object, shares the class name, has no return type, and
is called automatically. **Overloading** = multiple constructors with different parameters.

**11. What is `this`?**
A reference to the current object — used to disambiguate fields from parameters and to
chain constructors/methods.

**12. Static vs Instance members?**
**Static** belongs to the class (shared across all objects, accessed via the class name).
**Instance** belongs to each object separately.

**13. Shallow copy vs Deep copy?**
**Shallow** copies references — nested objects are shared. **Deep** copies recursively, so
the copy is fully independent.

**14. What is method hiding vs overriding?**
Overriding works on instance methods via dynamic dispatch. **Hiding** happens with static
methods or fields — resolved by the reference type, not the object.

**15. Cohesion vs Coupling?**
**Cohesion** = how focused a module is (want **high**). **Coupling** = how dependent
modules are on each other (want **low**). Good design: high cohesion, low coupling.

**16. What is a virtual function (C++)?**
A method declared `virtual` so the call is resolved at run time based on the actual object
type (enables overriding/polymorphism via the vtable).

**17. Pass by value vs pass by reference?**
**By value** copies the argument (changes don't affect the original). **By reference**
passes the actual object/address (changes are visible to the caller).

**18. Why use OOP? Advantages?**
Reusability (inheritance), maintainability (encapsulation), flexibility (polymorphism),
and modeling real-world entities clearly. Trade-off: can be over-engineered for simple tasks.
