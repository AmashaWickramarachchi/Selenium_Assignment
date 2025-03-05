## **Selenium Automation Project with Python for Entgra Endpoint Management Website**

### **Overview of the Project**  
This is a Selenium-based automation project that automates testing for the **Entgra Endpoint Management** website using Python. The project follows the **Page Object Model (POM)** design pattern, utilizes the `unittest` framework for test execution, and generates reports using `HTMLTestRunner`.

---

## **1. Installation Guide**  

### **1.1 Clone the Repository**  

```sh
git clone https://github.com/AmashaWickramarachchi/Selenium_Assignment.git
cd Selenium_Assignment
```

### **1.2 Set Up a Virtual Environment(optional)**  

```sh
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### **1.3 Install Dependencies**  

```sh
pip install -r requirements.txt
```

---

## **2. Running the Tests**  

### **To Run All Test Cases**  

```sh
python test_suite.py
```

### **To Run a Specific Test**  

```sh
python -m unittest Tests/test01_CreateGroup.py
python -m unittest Tests/test02_EditGroup.py
python -m unittest Tests/test03_DeleteGroup.py
```

---

## **3. Report Generation**  

After running the test suite, reports will be generated in the **Reports/** directory.

To open the reports, navigate to the directory and open the generated HTML file in a browser.

```sh
python test_suite.py
```

---

## **4. Technology Used**  

- **Python**  
- **Selenium WebDriver**  
- **Unittest Framework**  
- **HTMLTestRunner** for test reports  

---

## **5. Author**  

**Amasha Wickramarachchi**  
amashasewwandi7@gmail.com  

