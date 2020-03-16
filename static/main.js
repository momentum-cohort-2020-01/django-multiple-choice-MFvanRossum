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
    let buttons = document.querySelectorAll('.fa-clipboard');
    for (let button of buttons) {
        button.addEventListener('click', function(event) {
            let parent = event.target.closest('.code-snippet');
            let snippet = parent.querySelector('code');
            let range = document.createRange();
            range.selectNode(snippet);
            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);
            try {
                let successful = document.execCommand('copy');
                let msg = successful ? 'successful' : 'unsuccessful';
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