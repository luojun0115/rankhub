(function() {
  var PASSWORD = 'rankhub2026';
  var gate = document.getElementById('passwordGate');
  var content = document.getElementById('passwordContent');
  var input = document.getElementById('passwordInput');
  var submit = document.getElementById('passwordSubmit');
  var error = document.getElementById('passwordError');

  if (!gate) return;

  if (sessionStorage.getItem('rankhub_auth') === 'true') {
    gate.style.display = 'none';
    content.style.display = 'block';
    return;
  }

  error.style.display = 'none';

  function checkPassword() {
    if (input.value === PASSWORD) {
      sessionStorage.setItem('rankhub_auth', 'true');
      gate.style.display = 'none';
      content.style.display = 'block';
    } else {
      error.style.display = 'block';
      input.value = '';
      input.focus();
    }
  }

  submit.addEventListener('click', checkPassword);
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') checkPassword();
  });
  input.focus();
})();
