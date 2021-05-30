## Unit Testing and Test Driven Development in Python

### Chapter 2: Overview of Test Driven Development Quiz

---

1. At what level of the software is unit testing normally performed?

    A. System Level
   
    B. Component Level
   
    C. Class and Function Level  `<--- My Answer`

    - Unit testing is preformed at the code level of the software

---

2. Who typically implements and runs unit tests?
   
    A. System Test Engineers
   
    B. Software Developers `<--- My Answer`

    - The developers are the ones that implement and run the unit test to ensure their code is functioning properly and to catch any bugs that may happen before it reaches the public.
   
    C. Integration Team
   
    D. Product Owners

---

3. In test driven development, you write all the unit tests first and then write all the production code.
   
    A. True
   
    B. False `<--- My Answer`

    - This is **False** because you do **not** want to write **All** the unit test and then write **All** the production code. You want to **write it in "bits"**. Write one test that you know will fail, then write the code to pass that test. Then write the next test that you know will fail, then the code to pass that test, and so on until all functionality is written.

---

4. What are the three phases of Test Driven Development?
   
    A. Red, Green, and Refactor `<--- My Answer`

    - **Red** = Write the test for the functionality you want, knowing it will fail.
    
    - **Green** = Write the production code to pass the failing test from the Red phase.
    
    - **Refactor** = Can the code be refactored? Any duplicates? Can anything be combined to make the code more readable?
   
    B. Test, Code, and Release
   
    C. User Stories, Tests, and Coding

---

5. What are one of the benefits of Test Driven Development?

    A. Documents the code
    
    - Unit test act as a documentation for your code because you are writing the code to pass the tests.
   
    B. Drives good object-oriented design

    - Forces you to be mindful of your classes, scopes, and functions
   
    C. All of these `<--- My Answer`

    - All the above are correct. 
