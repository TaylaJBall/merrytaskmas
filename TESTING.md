# Testing

This is the TESTING file for the [MerryTaskmas](https://merrytaskmas-e050025a1784.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents

- [Testing](#testing)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

---

## Validation

### HTML Validation

HTML pages were validated using the [W3C HTML Validator](https://validator.w3.org/). Minor errors related to **Django forms** or third-party tools were found but considered non-critical.

| Page                   | Errors | Warnings |
|------------------------|--------|----------|
| Home                   | 0      | 0        |
| Login                  | 0      | 0        |
| Logout                 | 0      | 0        |
| Register               | 0      | 0        |
| Add Gift List          | 0      | 0        |
| Edit Gift List         | 0      | 0        |
| Delete Gift List       | 0      | 0        |
| Add Item               | 0      | 0        |
| Edit Item              | 0      | 0        |
| Gift List Page         | 0      | 0        |
| Task List              | 0      | 0        |

<details>
  <summary>Example Screenshot - Register Page</summary>
  <img src="documentation/testing/html_register_errors.png">
</details>

---

### CSS Validation

The CSS file was validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), and no errors or warnings were found.

![CSS Validation](documentation/testing/css_validation.png)

---

### JavaScript Validation

The JavaScript files were validated using [JSHint](https://jshint.com/). All files passed without errors.

| File                 | Errors | Warnings |
|----------------------|--------|----------|
| `countdown.js`       | 0      | 0        |


<details>
  <summary>Example Screenshot - countdown.js</summary>
  <img src="documentation/testing/js_countdown.png">
</details>

---

### Python Validation

Python files were validated using [CI Python Linter](https://pep8ci.herokuapp.com/) for PEP8 compliance. There were no errors.

| File                 | Errors | Notes           |
|----------------------|--------|-----------------|
| `views.py`           | 0      | No issues       |
| `models.py`          | 0      | No issues       |
| `urls.py`            | 0      | No issues       |
| `forms.py`           | 0      | No issues       |

<details>
  <summary>Example Screenshot - views.py</summary>
  <img src="documentation/testing/python_views.png">
</details>

---

### Lighthouse Scores

Testing was conducted using **Google Lighthouse** for both **Desktop** and **Mobile** views.

**Desktop Results**:

![Lighthouse Desktop](documentation/testing/lighthouse_desktop.png)

**Mobile Results**:

![Lighthouse Mobile](documentation/testing/lighthouse_mobile.png)

---

### Wave Accessibility Evaluation

[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to test accessibility. A few minor **contrast errors** were found, but they are non-critical and will be addressed in future updates.

![Wave Results](documentation/testing/wave.png)

---

## Manual Testing

### User Input/Form Validation

Forms and user input were tested across the project to ensure proper behavior.

| Feature                        | User Input       | Expected Behavior                          | Result |
|--------------------------------|------------------|-------------------------------------------|--------|
| **Add Gift List**              | Name, Budget     | Gift List is added and displayed           | Pass   |
| **Edit Gift List**             | Update fields    | Changes are saved                          | Pass   |
| **Delete Gift List**           | Confirmation     | Gift List is removed                       | Pass   |
| **Add Item**                   | Description, Link| Item is added to Gift List                 | Pass   |
| **Edit Item**                  | Update fields    | Item changes are saved                     | Pass   |
| **Delete Item**                | Confirmation     | Item is removed from Gift List             | Pass   |
| **Task List**                  | Task Input       | Task is added, edited, or deleted          | Pass   |
| **Sign In/Out**                | Email, Password  | User signs in or out successfully          | Pass   |

---

### Browser Compatibility

Testing was conducted across modern browsers:

| Browser         | Version              | Result       |
|-----------------|----------------------|--------------|
| Chrome          | 131.0.x              | Pass         |
| Firefox         | 125.0.x              | Pass         |
| Safari          | 18.1.x               | Pass         |
| Edge            | 131.0.x              | Pass         |

---

### Testing User Stories

| User Story                               | Expected Outcome                          | Tested  | Result |
|-----------------------------------------|------------------------------------------|---------|--------|
| View countdown timer                    | See real-time countdown on Home page     | Yes     | Pass   |
| Add/edit/delete gift lists              | Manage gift lists for individuals        | Yes     | Pass   |
| Add/edit/delete items in gift lists     | Manage items with descriptions/links     | Yes     | Pass   |
| Sign up and log in                      | Register and log in with account         | Yes     | Pass   |
| View to-do list                         | Manage tasks for holiday planning        | Yes     | Pass   |
| Logout confirmation                     | Confirm logout with cancel option        | Yes     | Pass   |

---

### Dev Tools/Real World Device Testing

The site was tested on various devices:

| Device                  | Resolution | Result       |
|-------------------------|------------|--------------|
| iPhone 13 Mini          | 390x844    | Pass         |
| iPad Air                | 820x1180   | Pass         |
| MacBook Air             | 1440x900   | Pass         |
| Desktop (Full HD)       | 1920x1080  | Pass         |

---

## Bugs

| Bug Description                             | Status   | Fix/Action Taken                          |
|--------------------------------------------|----------|------------------------------------------|
| CSS styles not applying to buttons          | Solved   | Adjusted specificity for custom classes   |
| Task list item links overflowing            | Solved   | Added `word-wrap: break-word` to styles   |
| Logout confirmation button alignment issue  | Solved   | Used Flexbox for consistent alignment     |

---

### Known Bugs

- Minor contrast errors in footer links reported by **Wave Tool**.
- Placeholder images do not load consistently in Safari (related to Cloudinary).

---

## Conclusion

The **MerryTaskmas** website has been thoroughly tested for functionality, responsiveness, and accessibility. All major features work as intended, and minor bugs have been addressed.

For any issues, please [open an issue on GitHub](https://github.com/TaylaJBall/merrytaskmas/issues).

---