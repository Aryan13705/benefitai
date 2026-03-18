// ─────────────────────────────────────────────
//  api.js  —  shared API helpers for BenefitAI
// ─────────────────────────────────────────────

// Backend URL is hardcoded for simplicity
// Detect if we are running locally or on Netlify
// Backend URL is relative for Firebase integration
// Backend URL is relative for deployment, absolute for local dev
const API_BASE = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" 
    ? "http://localhost:5002"
    : "/api";

// Note: if you ever change backend location update the string above.

/**
 * Wrapper around fetch that always sends cookies (session), sets JSON headers,
 * and returns parsed JSON. Throws on non-2xx responses.
 */
async function apiFetch(path, options = {}) {
    const isFormData = options.body instanceof FormData;
    const fetchOptions = {
        credentials: "include",
        ...options,
    };

    if (!isFormData) {
        fetchOptions.headers = { "Content-Type": "application/json", ...(options.headers || {}) };
    } else {
        fetchOptions.headers = { ...(options.headers || {}) }; // Let browser set multipart boundary
    }

    const res = await fetch(`${API_BASE}${path}`, fetchOptions);
    const data = await res.json();
    if (!res.ok) throw { status: res.status, ...data };
    return data;
}

/** Redirect the entire page to a frontend URL returned by the backend. */
function handleRedirect(redirect) {
    if (!redirect) return;
    // backend returns paths like "/dashboard.html" or "/profile_setup.html"
    window.location.href = redirect;
}

/** Log a user action to the backend asynchronously (fire-and-forget). */
function logActivity(action, details = {}) {
    apiFetch("/log-activity", {
        method: "POST",
        body: JSON.stringify({ action, details, page: window.location.pathname }),
    }).catch(() => { });
}

// Log every page view automatically
window.addEventListener("load", () => logActivity("page_view"));

// Log every click on interactive elements
document.addEventListener("click", (e) => {
    const t = e.target.closest("a, button, select");
    if (t) {
        logActivity("click", {
            text: t.innerText || t.value || t.placeholder,
            id: t.id,
            tag: t.tagName,
        });
    }
});

// ─────────────────────────────────────────────
//  Security & Data Protection
// ─────────────────────────────────────────────

// Disable right-click to hinder inspection
document.addEventListener("contextmenu", (e) => {
    if (window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1") {
        e.preventDefault();
    }
});

// Disable key combos commonly used for DevTools
document.addEventListener("keydown", (e) => {
    if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") return;

    // F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C, Ctrl+U
    if (e.key === "F12") e.preventDefault();
    if ((e.ctrlKey || e.metaKey) && (e.key === "u" || e.key === "U")) e.preventDefault();
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === "I" || e.key === "J" || e.key === "C" || e.key === "i" || e.key === "j" || e.key === "c")) e.preventDefault();
});

// Selection Blocking for sensitive displays
document.addEventListener("DOMContentLoaded", () => {
    const sensitiveElements = document.querySelectorAll(".scheme-card, .stat-box, .responsive-table");
    sensitiveElements.forEach(el => {
        el.style.userSelect = "none";
        el.style.webkitUserSelect = "none";
        el.style.msUserSelect = "none";
    });
});

