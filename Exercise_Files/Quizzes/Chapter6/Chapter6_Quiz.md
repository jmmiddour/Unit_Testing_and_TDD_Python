# Unit Testing and Test Driven Development in Python

## Chapter 6: Test Doubles Quiz


### 1. Which of the following is not a type of test double?

    A. Singleton   <--- My Answer - This is not a Test Double!

    B. Dummy

    C. Fake

    D. Mock

---

### 2. A dummy provides a functional (and usually simplified) implementation, which may not be appropriate for production but works well for the unit testing.

    A. True

    B. False   <--- My answer - This is the simplest object but are not used in implementation.

---

### 3. A stub test double expects to be called and returns canned data.

    A. True   <--- My Answer - This is true and the data can be used in test implementation.

    B. False

---

### 4. This type of test double does not expect to be called and may actually throw an exception if it is called.

    A. Fake

    B. Spy

    C. Dummy   <--- My Answer - Not used for any test implementation.

    D. Mock

---

### 5. You should always implement your own test doubles and avoid using mock frameworks.

    A. True

    B. False   <--- My Answer - Making your own can be very time-consumming, tedious, and error-prone.
