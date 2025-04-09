# DOI Resolver Updater for DataCite

This Python script updates the target URLs of DOIs registered via DataCite.

It reads a CSV file containing DOIs and their corrected URLs, and sends updates to the DataCite API.

---

## ✅ Features

- Reads DOIs and new URLs from a CSV file
- Sends `PUT` requests to the DataCite REST API to update the `url` field
- Includes:
  - Logging to a file
  - Progress bar via `tqdm`
  - Dry run mode (to preview changes without sending updates)

---

## 📄 CSV Format

The input file should contain the following headers:

```
doi;url
10.xxxx/abcde;https://correct.link/abcde
10.xxxx/fghij;https://correct.link/fghij
```

_Note: Use `;` as the separator (common in Excel exports)._

---

## ⚙️ Configuration

Edit the following variables in the script:

```python
USERNAME = "your_datacite_username"
PASSWORD = "your_datacite_password"
CSV_FILE = "dois_to_update.csv"
DRY_RUN = True  # Set to False to make real changes
```

---

## ▶️ Running the Script

1. Install dependencies:

```bash
pip install pandas requests tqdm
```

2. Run the script:

```bash
python buddu.py
```

3. Check `doi_update_log.txt` for a full log of updates.

---

## 🛑 Safety Tip

Start with `DRY_RUN = True` to preview what would be updated before making changes.

---

## 🙌 Contributions

Contributions and improvements are welcome!  
Feel free to open a pull request or fork the repo: [github.com/svidmar](https://github.com/svidmar)

---

## 📜 License

MIT License – see `LICENSE` file.