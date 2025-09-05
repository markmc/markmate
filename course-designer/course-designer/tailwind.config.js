/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  safelist: [
    'text-green-600',
    'underline',
    'font-semibold'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}