# Vaibhav Dang — Interactive Resume (Streamlit)

A single-page interactive resume/portfolio site built with [Streamlit](https://streamlit.io).

## Repository structure

```
.
├── streamlit_resume_app.py     # Main app — all content lives in this file
├── requirements.txt            # Python dependencies for deployment
├── .streamlit/
│   └── config.toml             # Theme (colors matching the resume)
├── .gitignore
└── README.md
```

## Run locally

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run streamlit_resume_app.py
```

The app opens at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud (free)

1. Push this repo to GitHub (public or private — both work).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select this repository and branch, and set the main file
   path to `streamlit_resume_app.py`.
4. Click **Deploy**. Streamlit Cloud installs `requirements.txt` automatically
   and gives you a public URL like `https://<your-app>.streamlit.app`.
5. Any future `git push` to the connected branch auto-redeploys the app.

## Editing content

All resume content (contact info, summary, experience, projects, skills,
education, certifications, achievements) lives as plain Python
dictionaries/lists near the top of `streamlit_resume_app.py` — edit those
directly, no templating engine involved.

## Notes

- Update `CONTACT["linkedin"]` with your real LinkedIn URL before deploying.
- The contact form on the Contact page is a visual placeholder — wire it to
  a service like [Formspree](https://formspree.io) or
  [SendGrid](https://sendgrid.com) if you want it to actually send email.
- To add a downloadable resume PDF/DOCX, drop the file into the repo and add
  a `st.download_button` pointing to it.
