/**
 * suggestions.js
 * Handles the University Suggestion Modal and API calls
 */

function openSuggestionModal() {
    document.getElementById('suggestionModal').style.display = 'flex';
}

function closeSuggestionModal() {
    document.getElementById('suggestionModal').style.display = 'none';
    document.getElementById('suggestionResults').style.display = 'none';
    document.getElementById('suggestionForm').style.display = 'block';
}

async function getUniversitySuggestions(event) {
    event.preventDefault();
    
    const submitBtn = event.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Analyzing Profiles...';
    submitBtn.disabled = true;

    const payload = {
        marks_10: parseFloat(document.getElementById('marks10').value),
        marks_12: parseFloat(document.getElementById('marks12').value),
        income: parseInt(document.getElementById('annualIncome').value),
        occupation: document.getElementById('occupation').value
    };

    try {
        const results = await apiFetch('/suggest-universities', {
            method: 'POST',
            body: JSON.stringify(payload)
        });

        displaySuggestions(results);
    } catch (err) {
        alert(err.message || 'Failed to get suggestions. Please try again.');
    } finally {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }
}

function displaySuggestions(data) {
    const resultsDiv = document.getElementById('suggestionResults');
    const form = document.getElementById('suggestionForm');
    
    form.style.display = 'none';
    resultsDiv.style.display = 'block';
    resultsDiv.innerHTML = ''; // Clear for fresh render

    if (!data.suggestions || data.suggestions.length === 0) {
        const p = document.createElement('p');
        p.style.textAlign = 'center';
        p.style.color = 'var(--text-muted)';
        p.textContent = 'No specific matches found for your profile. Try adjusting your criteria.';
        resultsDiv.appendChild(p);

        const btn = document.createElement('button');
        btn.onclick = resetSuggestionForm;
        btn.className = 'btn btn-secondary';
        btn.style.width = '100%';
        btn.style.marginTop = '1rem';
        btn.textContent = 'Try Again';
        resultsDiv.appendChild(btn);
        return;
    }

    const title = document.createElement('h4');
    title.style.marginBottom = '1rem';
    title.textContent = 'Top Matches for You:';
    resultsDiv.appendChild(title);
    
    data.suggestions.forEach(univ => {
        let badgeColor = "#7c3aed";
        if (univ.match_type === "Elite") badgeColor = "#f59e0b";
        if (univ.match_type === "Match") badgeColor = "#10b981";

        const card = document.createElement('div');
        card.style.cssText = `background:#fff; border:1px solid #e2e8f0; padding:1rem; border-radius:0.75rem; margin-bottom:0.75rem; border-left:4px solid ${badgeColor};`;

        const header = document.createElement('div');
        header.style.cssText = "display:flex; justify-content:space-between; align-items:flex-start;";

        const name = document.createElement('h5');
        name.style.cssText = "margin:0; font-size:1rem; color:#1e293b;";
        name.textContent = univ.name;

        const badge = document.createElement('span');
        badge.style.cssText = `font-size:0.7rem; background:${univ.type === 'Central' ? '#dcfce7' : '#fef3c7'}; color:${univ.type === 'Central' ? '#166534' : '#92400e'}; padding:2px 8px; border-radius:10px; font-weight:700;`;
        badge.textContent = univ.type;

        header.appendChild(name);
        header.appendChild(badge);

        const subheader = document.createElement('div');
        subheader.style.cssText = "font-size:0.8rem; color:var(--text-muted); margin-top:0.25rem;";
        subheader.textContent = `${univ.location} • ${univ.category}`;

        const matchType = document.createElement('div');
        matchType.style.cssText = `margin-top:0.5rem; font-size:0.75rem; font-weight:600; color:${badgeColor};`;
        matchType.textContent = `${univ.match_type} Candidate`;

        const link = document.createElement('a');
        link.href = univ.website;
        link.target = "_blank";
        link.style.cssText = "display:inline-block; margin-top:0.5rem; font-size:0.75rem; color:#7c3aed; text-decoration:none; font-weight:700;";
        link.textContent = "Visit Website →";

        card.appendChild(header);
        card.appendChild(subheader);
        card.appendChild(matchType);
        card.appendChild(link);
        resultsDiv.appendChild(card);
    });

    const resetBtn = document.createElement('button');
    resetBtn.onclick = resetSuggestionForm;
    resetBtn.className = 'btn btn-secondary';
    resetBtn.style.width = '100%';
    resetBtn.style.marginTop = '1rem';
    resetBtn.textContent = 'Search Again';
    resultsDiv.appendChild(resetBtn);
}

function resetSuggestionForm() {
    document.getElementById('suggestionResults').style.display = 'none';
    document.getElementById('suggestionForm').style.display = 'block';
    document.getElementById('suggestionForm').reset();
}
