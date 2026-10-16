const STORAGE_KEY = 'metaestudo-theme'
const root = document.documentElement
const savedTheme = localStorage.getItem(STORAGE_KEY)
let theme = savedTheme === 'light' ? 'light' : 'dark'

function applyTheme() {
    const light = theme === 'light'
    root.dataset.theme = theme

    if (light) {
        root.style.setProperty('--bg', '#f4f6f5')
        root.style.setProperty('--bg-soft', '#eceeed')
        root.style.setProperty('--panel', '#ffffff')
        root.style.setProperty('--border', 'rgba(0,0,0,0.08)')
        root.style.setProperty('--text', '#101312')
        root.style.setProperty('--text-mid', '#38423c')
        root.style.setProperty('--text-dim', '#5b635f')
        root.style.setProperty('--field', '#ffffff')
        root.style.setProperty('--field-focus', '#f3f8f5')
    } else {
        root.style.setProperty('--bg', '#0a0d0c')
        root.style.setProperty('--bg-soft', '#0e1211')
        root.style.setProperty('--panel', '#121615')
        root.style.setProperty('--border', 'rgba(255,255,255,0.08)')
        root.style.setProperty('--text', '#eef1ef')
        root.style.setProperty('--text-mid', '#c4cec8')
        root.style.setProperty('--text-dim', '#9aa39e')
        root.style.setProperty('--field', '#101413')
        root.style.setProperty('--field-focus', '#162019')
    }

    document.querySelectorAll('[data-theme-toggle]').forEach((toggle) => {
        toggle.setAttribute('aria-pressed', String(light))
    })
}

function initializeThemeToggles() {
    document.querySelectorAll('[data-theme-toggle]').forEach((toggle) => {
        toggle.addEventListener('click', () => {
            theme = theme === 'light' ? 'dark' : 'light'
            localStorage.setItem(STORAGE_KEY, theme)
            applyTheme()
        })
    })
    applyTheme()
}

applyTheme()
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeThemeToggles)
} else {
    initializeThemeToggles()
}
