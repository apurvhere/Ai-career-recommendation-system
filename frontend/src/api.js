const BASE='http://127.0.0.1:8000/api';
async function call(path,opts={}){const r=await fetch(BASE+path,opts);const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.error||Object.values(d).flat().join(' ')||'Request failed');return d}
export function parseResume(file){const f=new FormData();f.append('resume',file);return call('/resume/parse/',{method:'POST',body:f})}
export function getRecommendations(skills){return call('/recommend/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({skills})})}
export function getSkillGap(skills,career){return call('/skill-gap/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({skills,career})})}
