// function copy_to_clipboard() {
//     document.querySelector("code").addEventListener("click", async event => {
//         if (!navigator.clipboard) {
//             return;
//         }
//         const text = event.target.innerText;
//         try {
//             await navigator.clipboard.writeText(text);
//             event.target.textContent = "Copied to clipboard!";
//         } catch (err) {
//             console.error("Copy failed!", err);
//         }
//     })
// }

function copy_to_clipboard() {
    const buttons = document.querySelectorAll('.fa-clipboard');
    for (const button of buttons) {
        button.addEventListener('click', function(event) {
            const parent = event.target.closest('.code-snippet');
            const snippet = parent.querySelector('code');
            const range = document.createRange();
            range.selectNode(snippet);
            window.getSelection().addRange(range);
            try {
                const successful = document.execCommand('copy');
                const msg = successful ? 'successful' : 'unsuccessful';
                console.log('Copy snippet command was ' + msg);
            } catch(err) {
                console.log('Sorry, unable to copy snippet');
            } window.getSelection().removeAllRanges();
        })
    }   
}

document.addEventListener('DOMContentLoaded', function(){
    copy_to_clipboard()
})