# PDF OM Parser API

This is a **FastAPI** application that parses **real estate Offering Memorandums (OMs)** in PDF format to extract key information such as:

- **Property Name**
- **Address** (extracted from the second line of the first page)
- **Total Rentable Square Footage**

The application is designed to be easily extended and can be used to parse various formats of Offering Memorandums.

---

### 1. Clone the Repository

```bash
git clone https://github.com/Hammad-1/pdf-parsing-api
cd pdf-parsing-ap
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Running app locally

```bash
uvicorn main:app --reload
```


### Example Curl Request

curl -X POST "http://127.0.0.1:8000/api/parse-pdf" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path_to_your_file.pdf"


### Example Response

{
  "property_name": "Sunset Office Plaza",
  "address": "1234 Main St, Dallas, TX 75201",
  "total_rentable_sqft": "85,000"
}