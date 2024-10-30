function scrollToBottom(log) {
    log.scrollTop = log.scrollHeight;
}
window.onload = scrollToBottom(document.querySelector('#activities-log'));