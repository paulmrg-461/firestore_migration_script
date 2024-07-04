# Instructions to Migrate Firebase Tables to a New Project

## 1. Preparations

1. **Download Admin Credentials:**
   - Go to the [Firebase Console](https://console.firebase.google.com/).
   - Select your original project.
   - Navigate to Project Settings > Service accounts.
   - Generate a new private key and download the JSON file (`serviceAccountKey.json`).
   - Repeat the steps for the new Firebase project.

---

## 2. Update the Credential Paths

Replace `'path/to/original/serviceAccountKey.json'` and `'path/to/new/serviceAccountKey.json'` in the script with the correct paths to the credential files downloaded in the previous step.

---

## 3. Install Dependencies

1. **Install Dependencies:**
   Run the following command in your terminal to install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---

## 4. Run the Script
1. **Update tables to migrate:**
    Ensure you add the list of tables you want to migrate in the script under the `tables` variable.
   ```python
   # Collections to migrate
    tables = [
        'client',
        'company',
        ...
    ]
   ```
2. **Run the Script:**
    Run the following command in your terminal to start the migration:
   ```bash
   python app.py
   ```
---

## 5. Verify the Migration

- After running the script, verify in the Firebase console that the collections and documents have been successfully migrated to the new project.

## Summary

These instructions will allow you to migrate the specified collections from your original Firebase project to a new project using a Python script. This method is efficient and provides you with complete control over the migration process.