Z.ready(() => {
    App.load();
});


const App = {

    prompt: null,

    obj: {},

    load() {

        this.storageGet();

        const appName = 'solverprompt';
        Z.terms(appName, App.obj.language, res => {
            if (res === false) {
                Z.termsError(App.obj.language);
                return;
            } else {
                Z.recordAccess(appName);
            }
        });

        // Exibe menu
        document.getElementById('menu-toggle').addEventListener('click', () => this.menuShow());

        // Clique nos itens do menu
        document.querySelectorAll('.menu-item').forEach(item => {
            item.addEventListener('click', event => {
                const action = event.target.closest('.menu-item').id;
                this.menuClick(action);
            });
        });

        // Oculta menu
        document.getElementById('header-left').addEventListener('click', () => this.menuHide());
        document.getElementById('menu-dropdown').addEventListener('mouseleave', () => this.menuHide());

        // Exibe cabeçalho e botões na linguagem correta
        Language.headerRefresh()

        // Inicializa prompt
        this.prompt = new Prompt();
        Z.get('#button-analyze').addEventListener('click', () => this.prompt.analyze());
        Z.get('#button-submit').addEventListener('click', () => this.prompt.submit());
        Z.get('#button-clear').addEventListener('click', () => this.prompt.clear());

    },


    storageGet() {
        const storage = localStorage.getItem('solverprompt');
        if (storage === null) {
            this.obj = {
                language: Language.getBrowserLanguage(),
            }
            this.storageSet();
        } else {
            this.obj = JSON.parse(storage);
        }
    },

    storageSet() {
        localStorage.setItem('solverprompt', JSON.stringify(this.obj));
    },


    error(message) {
        Z.processing.hide();
        Z.hide('.all-div');
        Z.html('#error', message);
        Z.show('#error');
    },


    menuShow() {
        document.getElementById('menu-dropdown').style.display = 'block';
    },

    menuHide() {
        document.getElementById('menu-dropdown').style.display = 'none';
    },

    menuClick(action) {
        this.menuHide();
        if (action === 'menu-en') {
            Language.set('en');
        } else if (action === 'menu-pt') {
            Language.set('pt');
        } else if (action === 'menu-es') {
            Language.set('es');
        } else if (action === 'menu-te') {
            Language.set('te');
        } else if (action === 'menu-terms') {
            this.terms();
        }
    },

    terms() {
        Z.termsShow('solverpoll', App.obj.language, res => {
            if (res === false) {
                Z.termsError(App.obj.language);
                return;
            }
        });
    },


}






