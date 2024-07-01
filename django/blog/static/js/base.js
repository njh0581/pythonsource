//로그아웃 클릭시 a 태그 기능 중지
document.querySelector("#logout").addEventListener("click", (e) => {
  e.preventDefault();
  form = document.querySelector("#logoutForm");
  // console.log(form);
  form.submit();
});
