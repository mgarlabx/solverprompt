class Prompt {
    constructor() {
        this.prompts = [];
        this.apiPath = 'https://swz5opnuzja6zvyn5irv2mt5ki0htnji.lambda-url.us-west-2.on.aws/';
    
    }

    analyze() {
        this.run('analyze');
    }

    submit() {
        this.run('submit');
    }

    run(path) {
        Z.processing.show();
        const prompt_input = Z.getInputTextarea('prompt-input');
        if (prompt_input) {
            fetch(this.apiPath + path, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 
                    language: App.obj.language,
                    prompt_input: prompt_input 
                })
            })
            .then(response => response.json())
            .then(data => {
                Z.processing.hide();
                const text = marked.parse(data.text);
                Z.html('#response', text);
            })
            .catch(error => {
                Z.processing.hide();
                console.error('Error:', error);
                Z.html('#response', error.message);
            });
        } else {
            Z.processing.hide();
            Z.html('#response', 'Please enter a prompt.');
        }
        
    }

    clear() {
        Z.get('#prompt-input').value = '';
        Z.html('#response', '');
    }


}
