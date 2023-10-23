/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')


module.exports = {
  content: ["./encuesta/templates/*.{html,js}", "./encuesta/static/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'sans': ['Montserrat', ...defaultTheme.fontFamily.sans],
    },

    extend: {

    },
  },
  plugins: [],
}



// npx tailwindcss -i ./encuesta/static/css/input.css -o ./encuesta/static/css/styles.css --watch