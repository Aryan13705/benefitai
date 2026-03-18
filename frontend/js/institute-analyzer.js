// ─────────────────────────────────────────────
//  institute-analyzer.js — matching students to institutes
// ─────────────────────────────────────────────

function openInstituteAnalyzer() {
    const modal = document.getElementById('analyzerModal');
    modal.style.display = 'flex';
    
    // Populate states if not already done
    const statesList = document.getElementById('analyzerStatesList');
    if (statesList.children.length === 0 && typeof allStates !== 'undefined') {
        statesList.innerHTML = allStates.map(s => `
            <label style="display:flex; align-items:center; gap:.4rem; background:#f1f5f9; padding:.3rem .6rem; border-radius:.5rem; font-size:.85rem; cursor:pointer;">
                <input type="checkbox" name="analyzerState" value="${s.name}">
                ${s.emoji} ${s.name}
            </label>
        `).join('');
    }
}

function closeInstituteAnalyzer() {
    document.getElementById('analyzerModal').style.display = 'none';
}

async function runInstituteAnalyzer(e) {
    e.preventDefault();
    
    const income = document.getElementById('analyzerIncome').value;
    const marks_10 = document.getElementById('analyzerMarks10').value;
    const marks_12 = document.getElementById('analyzerMarks12').value;
    const jee_score = document.getElementById('analyzerJee').value;
    const category = document.getElementById('analyzerCategory').value;
    const stateCheckboxes = document.querySelectorAll('input[name="analyzerState"]:checked');
    const states = Array.from(stateCheckboxes).map(cb => cb.value);
    
    const resultsDiv = document.getElementById('analyzerResults');
    const resultsList = document.getElementById('analyzerResultsList');
    
    resultsDiv.style.display = 'block';
    resultsList.innerHTML = '<div class="loader"><div class="spinner"></div> Calculating best options...</div>';
    
    try {
        const data = await apiFetch('/suggest-institutes', {
            method: 'POST',
            body: JSON.stringify({ 
                income: parseInt(income), 
                marks_10: parseInt(marks_10),
                marks_12: parseInt(marks_12),
                jee_score: parseInt(jee_score) || 0,
                states, 
                category 
            })
        });
        
        if (data.status === 'success' && data.suggestions.length > 0) {
            resultsList.innerHTML = data.suggestions.map(inst => `
                <div style="background:#f8fafc; border-left:4px solid ${inst.match_score >= 90 ? '#10b981' : '#8b5cf6'}; border-radius:.75rem; padding:1.25rem;">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:.5rem;">
                        <div>
                            <h4 style="margin:0; font-size:1.1rem;">${inst.name}</h4>
                            <p style="margin:0; font-size:.85rem; color:#64748b;">📍 ${inst.location}, ${inst.state_name}</p>
                        </div>
                        <span style="background:${inst.match_score >= 90 ? '#d1fae5' : '#ede9fe'}; color:${inst.match_score >= 90 ? '#065f46' : '#5b21b6'}; padding:.2rem .6rem; border-radius:1rem; font-size:.7rem; font-weight:700; text-transform:uppercase;">
                        ${inst.match_score >= 90 ? 'Perfect Match' : 'Highly Recommended'}
                        </span>
                    </div>
                    <div style="margin:.75rem 0; font-size:.85rem; padding:.5rem .75rem; background:rgba(139, 92, 246, 0.05); border-radius:.5rem; border:1px solid rgba(139, 92, 246, 0.1);">
                        🎯 <strong>Why this match:</strong> ${inst.match_reason}
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:.8rem; color:#64748b;">${inst.type} | ${inst.category}</span>
                        <a href="${inst.website}" target="_blank" style="color:#8b5cf6; font-size:.85rem; font-weight:600; text-decoration:none;">Visit Website →</a>
                    </div>
                </div>
            `).join('');
        } else {
            resultsList.innerHTML = '<p style="text-align:center; padding:2rem; color:#64748b;">No direct matches found. Try broading your state or income criteria.</p>';
        }
    } catch (err) {
        console.error(err);
        resultsList.innerHTML = '<p style="color:#ef4444;">Error finding match. Please try again.</p>';
    }
}
