console.log("JS OK");

// SAFE SUPABASE INIT
if (!window.supabaseClient) {
  window.supabaseClient = window.supabase.createClient(
    "https://ebhbpaxdpifelnxixgfy.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImViaGJwYXhkcGlmZWxueGl4Z2Z5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUyNTE3NzksImV4cCI6MjA5MDgyNzc3OX0.H6NTHRDu0HMXBBNbQjg2uJGnxqJbPqJYNWBlTpn00Eo"
  );
}

const supabase = window.supabaseClient;


// INIT
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM READY");

  const btn = document.getElementById("btnLogin");

  if (btn) {
    console.log("BUTTON ADA");

    btn.addEventListener("click", () => {
      console.log("CLICK DETECTED");
      alert("SIAP LOGIN");
    });

  } else {
    console.log("BUTTON TIDAK ADA");
  }
});