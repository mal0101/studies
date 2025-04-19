/**
 * @type {import('tailwindcss').Config}
 */
module.exports = {
    content: ["./*.html"],
    darkMode: 'class', // Active le mode sombre
    theme: {
      extend: {
        colors: {
          // Couleurs personnalisées pour l'université
          'univ': {
            primary: '#1E40AF',    // Bleu principal
            secondary: '#1D4ED8',  // Bleu secondaire
            accent: '#3B82F6',     // Bleu accent
            light: '#EFF6FF',      // Fond clair
            dark: '#1E293B',       // Fond sombre
          },
        },
      },
    },
    plugins: [],
  }