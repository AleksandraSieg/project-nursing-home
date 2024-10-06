/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Wszystkie szablony HTML w katalogu templates
    './**/templates/**/*.html' // Jeśli masz wiele aplikacji Django
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}


