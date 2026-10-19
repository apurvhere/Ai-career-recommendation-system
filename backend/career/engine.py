import json, re
from pathlib import Path
DATASET_PATH = Path(__file__).resolve().parents[2] / "dataset" / "careers.json"
ALIASES = {"js":"JavaScript","ml":"Machine Learning","sklearn":"scikit-learn","powerbi":"Power BI","apis":"REST API"}
def load_careers():
    with open(DATASET_PATH, encoding="utf-8") as f: return json.load(f)
def detect_skills(text):
    text = text.lower()
    skills = set(s for c in load_careers() for s in c["skills"])
    skills.update(["Pandas","NumPy","NLP","Deep Learning","Figma","UI Design","UX Research","Prototyping","JavaScript","React","Django","HTML","CSS","C++","Java"])
    found = []
    for skill in sorted(skills, key=len, reverse=True):
        if re.search(r"(?<![a-z0-9+#])"+re.escape(skill.lower())+r"(?![a-z0-9+#])", text): found.append(skill)
    for alias, canonical in ALIASES.items():
        if re.search(r"(?<![a-z0-9+#])"+re.escape(alias)+r"(?![a-z0-9+#])", text) and canonical not in found: found.append(canonical)
    return sorted(set(found), key=str.lower)
def recommend(skills, limit=5):
    known = {s.lower() for s in skills}; results=[]
    for c in load_careers():
        matched=[s for s in c["skills"] if s.lower() in known]
        score=round(100*len(matched)/max(1,len(c["skills"])))
        missing=[s for s in c["skills"] if s.lower() not in known]
        results.append({"title":c["title"],"score":score,"description":c["description"],"matching_skills":matched,"missing_skills":missing,"resources":[{"skill":r[0],"name":r[1],"url":r[2]} for r in c["resources"]],"next_step":f"Start with {missing[0]}" if missing else "Build a portfolio project","explanation":f"{len(matched)} of {len(c['skills'])} listed skills matched. Score uses simple skill overlap."})
    return sorted(results,key=lambda r:(-r["score"],r["title"]))[:limit]
def skill_gap(skills, title):
    c=next((x for x in load_careers() if x["title"].lower()==title.lower()),None)
    if not c:return None
    known={s.lower() for s in skills}; resources={r[0]:{"name":r[1],"url":r[2]} for r in c["resources"]}
    matched=[s for s in c["skills"] if s.lower() in known]
    missing=[{"name":s,"priority":"High" if i < 3 else "Medium","resource":resources.get(s,{"name":f"Free beginner {s} tutorial","url":"https://www.google.com/search?q=free+beginner+"+s.replace(" ","+")+"+course"})} for i,s in enumerate(c["skills"]) if s.lower() not in known]
    return {"career":c["title"],"matched_skills":matched,"missing_skills":missing,"match_percent":round(100*len(matched)/max(1,len(c["skills"]))),"roadmap":[{"step":i+1,"skill":m["name"],"priority":m["priority"],"action":f"Learn {m['name']} basics, complete a guided exercise, and build a small project."} for i,m in enumerate(missing)]}
