const themeToggle = document.getElementById('themeToggle')
const root = document.documentElement
let light = false
themeToggle.addEventListener('click', () => {
    light = !light
    if (light) {
        root.style.setProperty('--bg', '#f4f6f5')
        root.style.setProperty('--bg-soft', '#eceeed')
        root.style.setProperty('--panel', '#ffffff')
        root.style.setProperty('--border', 'rgba(0,0,0,0.08)')
        root.style.setProperty('--text', '#101312')
        root.style.setProperty('--text-dim', '#5b635f')
    } else {
        root.style.setProperty('--bg', '#0a0d0c')
        root.style.setProperty('--bg-soft', '#0e1211')
        root.style.setProperty('--panel', '#121615')
        root.style.setProperty('--border', 'rgba(255,255,255,0.08)')
        root.style.setProperty('--text', '#eef1ef')
        root.style.setProperty('--text-dim', '#9aa39e')
    }
})