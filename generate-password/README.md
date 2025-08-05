# 🔑 Python Secure Password Generator  

This script generates secure random passwords using Python’s `secrets` module, which is designed for cryptographic use. 

This script lets you specify:  
- Password length  
- Number of **digits** required  
- Number of **special characters** required  
- Minimum **uppercase** and **lowercase** letters  

---

## 🚀 Features
- Uses **`secrets`** instead of `random` for better security.
- Fully customizable password requirements.
- Ensures constraints (digits, symbols, uppercase, lowercase) are **always** met.
- Shuffles the characters to randomize the order.

---

## ⚡ Usage

### **1️⃣ Run directly from terminal**
```bash
python generate_password.py
```
Example output:
```
Generated password: aB7#kXw@9qLp
```

---

## 🛠 Parameters
| Parameter      | Type  | Default | Description |
|---------------|-------|---------|-------------|
| `length`       | int   | 16      | Total password length |
| `nums`         | int   | 1       | Minimum number of digits |
| `special_chars`| int   | 1       | Minimum number of special characters |
| `uppercase`    | int   | 1       | Minimum number of uppercase letters |
| `lowercase`    | int   | 1       | Minimum number of lowercase letters |

---


## 📂 File Structure
```
generate-password/
│── generate_password.py
│── README.md
```

---

## Related JavaScript Version
If you prefer a JavaScript implementation, check out this similar gist:  
https://gist.github.com/Cema2019/292c92a0eb2ca041db97db6b0123dac5
