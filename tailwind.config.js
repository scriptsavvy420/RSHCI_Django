/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        "./templates/*.html",
        "./templates/**/*.html",
        "./templates/**/**/*.html",
    ],
    darkMode: "class",
    theme: {
        screens: {
            xs: "450px",
            sm: "640px",
            md: "768px",
            tb: "992px",
            lg: "1024px",
            xl: "1280px",
            "2xl": "1536px",
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
        //    */
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
        require('@tailwindcss/line-clamp'),
    ],
};