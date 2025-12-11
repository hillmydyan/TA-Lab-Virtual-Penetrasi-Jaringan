function toggleStep(stepId) {
    const content = document.getElementById(stepId);

    // Tutup semua step lain
    document.querySelectorAll('.step-content').forEach(section => {
        if (section !== content) {
            section.classList.remove('open');
        }
    });

    // Toggle step yang diklik
    content.classList.toggle('open');
}
