module.exports = {
  mode:"jit",
  darkMode: false, // or 'media' or 'class'
  purge:{
    content:["**/*.html","**/*.jsx"],
    safelist: ["sm:px-8"]
  },
  corePlugins: {
  	 preflight: false,
  },

  variants: {
    extend: {},
  },
  plugins: [],
}
