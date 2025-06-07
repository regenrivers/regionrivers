function postComment() {
    const commentInput = document.getElementById("comment-input");
    const commentText = commentInput.value.trim();
    
    if (commentText !== "") {
        const commentList = document.getElementById("comment-list");
        const newComment = document.createElement("div");
        newComment.classList.add("comment");
        newComment.innerText = commentText;
        commentList.appendChild(newComment);
        
        commentInput.value = ""; // Clear input after posting
    }
}
