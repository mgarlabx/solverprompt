const Language = {

    set(lng) {
        App.obj.language = lng;
        App.storageSet();
        this.headerRefresh();
    },

    getBrowserLanguage() {
        const browserLanguage = navigator.language || navigator.userLanguage;
        if (browserLanguage.startsWith('en-')) {
            return 'en';
        } else if (browserLanguage.startsWith('pt-')) {
            return 'pt';
        } else if (browserLanguage.startsWith('es-')) {
            return 'es';
        } else {
            return 'en';
        }
    },

    get(key) {
        if (key == "menu-about-txt") return Language.getAbout();
        const obj = this.dictionay.find(item => item.key === key);
        if (obj) {
            return obj[App.obj.language];
        } else {
            return `{{{${key}}}}`;
        }
    },

    headerRefresh() {
        Z.html('#header-title', Language.get('header-title'));
        Z.html('#menu-caption-terms', Language.get('menu-caption-terms'));
        Z.html('#button-analyze', Language.get('Analisar'));
        Z.html('#button-submit', Language.get('Submeter'));
        Z.html('#button-clear', Language.get('Limpar'));
        Z.get('#prompt-input').setAttribute('placeholder', Language.get('Digite seu prompt aqui...'));
    },

    dictionay: [
        {
            "key": "header-title",
            "pt": "Solverprompt - Analisador de prompts",
            "en": "Solverprompt - Prompt Analyzer",
            "es": "Solverprompt - Analizador de prompts",
        },
        {
            "key": "menu-caption-terms",
            "pt": "Termos",
            "en": "Terms",
            "es": "Términos",
        },
        {
            "key": "Sim",
            "pt": "Sim",
            "en": "Yes",
            "es": "Sí",
        },
        {
            "key": "Não",
            "pt": "Não",
            "en": "No",
            "es": "No",
        },
        {
            "key": "Analisar",
            "pt": "Analisar",
            "en": "Analyze",
            "es": "Analizar",
        },
        {
            "key": "Submeter",
            "pt": "Submeter",
            "en": "Submit",
            "es": "Enviar",
        },
        {
            "key": "Limpar",
            "pt": "Limpar",
            "en": "Clear",
            "es": "Limpiar",
        },
        {
            "key": "Digite seu prompt aqui...",
            "pt": "Digite seu prompt aqui...",
            "en": "Enter your prompt here...",
            "es": "Introduce tu prompt aquí...",
        },
        {
            "key": ""
        },
        {
            "key": ""
        },
        {
            "key": ""
        },



    ],


};
