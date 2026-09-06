const projects = document.querySelectorAll(".project-card");

projects.forEach((project) => {
  project.addEventListener("click", function () {
    projects.forEach((p) => {
      p.classList.remove("active");
    });

    this.classList.add("active");
  });
});