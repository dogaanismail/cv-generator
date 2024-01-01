var inputFieldData = {
    first_name: "",
    last_name: "",
    email: "",
    phone: "",
    aboutYourself: "",
    university: [],
    degree: [],
    gpa: [],
    jobTitle: [],
    companyName: [],
    startDate: [],
    endDate: [],
    otherInformation: [],
    skills: [],
    interest: []
};


function addEducation() {
    var universityElem = document.getElementById("university");
    var degreeElem = document.getElementById("degree");
    var gpaElem = document.getElementById("gpa");
    if (universityElem.value && degreeElem.value && gpaElem.value) {
        inputFieldData["university"].push(universityElem.value);
        inputFieldData["degree"].push(degreeElem.value);
        inputFieldData["gpa"].push(gpaElem.value);
        countElement = document.getElementById("count_edu");
        listContent = document.createElement("li");
        listContent.innerHTML = "<strong>University:</strong> " + universityElem.value + "<br><strong>Degree:</strong> " + degreeElem.value + "<br><strong>GPA:</strong> " + gpaElem.value;
        listContent.classList.add("list-group-item");
        document.getElementById("edu_list").appendChild(listContent);
        universityElem.value = ""
        degreeElem.value = ""
        gpaElem.value = ""
    } else {
        alert("University, degree, and GPA fields are required.");
    }
}

function addWorkExperience() {
    var jobTitleElem = document.getElementById("job_title");
    var companyNameElem = document.getElementById("company_name");
    var startDateElem = document.getElementById("start_date");
    var endDateElem = document.getElementById("end_date");
    var otherInformationElem = document.getElementById("other_information");
    if (jobTitleElem.value && companyNameElem.value && startDateElem.value && endDateElem.value) {
        inputFieldData["jobTitle"].push(jobTitleElem.value);
        inputFieldData["companyName"].push(companyNameElem.value);
        inputFieldData["startDate"].push(startDateElem.value);
        inputFieldData["endDate"].push(endDateElem.value);
        inputFieldData["otherInformation"].push(otherInformationElem.value);
        listContent = document.createElement("li");
        listContent.innerHTML = "<strong>Job Title:</strong> " + jobTitleElem.value + "<br><strong>Company:</strong> " + companyNameElem.value + "<br><strong>Start Date:</strong> " + startDateElem.value + "<br><strong>End Date:</strong> " + endDateElem.value;
        listContent.classList.add("list-group-item");
        document.getElementById("work_exp_list").appendChild(listContent);
        jobTitleElem.value = "";
        companyNameElem.value = "";
        startDateElem.value = "";
        endDateElem.value = "";
        otherInformationElem.value = "";
    } else {
        alert("Job Title, Company Name, Start Date, End Date are required");
    }
}


function addInterests() {
    const inputInterestElem = document.getElementById("input_interests");
    if (inputInterestElem.value) {
        const interestListElem = document.getElementById("interest_list");
        inputFieldData["interest"].push(inputInterestElem.value);
        const interestElem = document.createElement("span");
        interestElem.innerText = inputInterestElem.value;
        interestElem.classList.add("list-group-item", "mr-2");
        interestListElem.appendChild(interestElem);
        inputInterestElem.value = "";
    } else {
        alert("Interests is required");
    }
}

function addSkills() {
    const inputSkillsElem = document.getElementById("input_skills");
    if (inputSkillsElem.value) {
        const skillsListElem = document.getElementById("skills_list");
        inputFieldData["skills"].push(inputSkillsElem.value);
        const skillElem = document.createElement("span");
        skillElem.innerText = inputSkillsElem.value;
        skillElem.classList.add("list-group-item", "mr-2");
        skillsListElem.appendChild(skillElem);
        inputSkillsElem.value = "";
    } else {
        alert("Skills is required");
    }
}

function sendData() {
    firstNameElem = document.getElementById("first_name")
    lastNameElem = document.getElementById("last_name")
    emailElem = document.getElementById("email")
    phoneElem = document.getElementById("phone")
    aboytYourselfElem = document.getElementById("about_yourself")

    if (firstNameElem.value && lastNameElem.value && emailElem.value && phoneElem.value && aboytYourselfElem.value) {
        console.log("submit insisded")
        inputFieldData["first_name"] = firstNameElem.value
        inputFieldData["last_name"] = lastNameElem.value
        inputFieldData["email"] = emailElem.value
        inputFieldData["phone"] = phoneElem.value
        inputFieldData["aboutYourself"] = aboytYourselfElem.value

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'submit');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
            } else {
                console.log('Error:', xhr.statusText);
            }
        };
        xhr.onerror = function () {
            console.log('Error:', xhr.statusText);
        };
        xhr.send(JSON.stringify({'data': inputFieldData}));

        inputFieldData = {
            first_name: "",
            last_name: "",
            email: "",
            phone: "",
            aboutYourself: "",
            university: [],
            degree: [],
            gpa: [],
            jobTitle: [],
            companyName: [],
            startDate: [],
            endDate: [],
            otherInformation: [],
            skills: [],
            interest: []
        };
    } else {
        alert("First Name, Last Name, Phone, Email are required")
    }
}

var currentStep = 1;
var steps = document.getElementsByClassName('step');
var prevBtn = document.getElementById('prevBtn');
var nextBtn = document.getElementById('nextBtn');
var listItems = document.querySelectorAll('#side-list .list-group-item');

function showStep(step) {
    for (var i = 0; i < steps.length; i++) {
        steps[i].style.display = 'none';
    }
    steps[step - 1].style.display = 'block';

    for (var j = 0; j < listItems.length; j++) {
        listItems[j].classList.remove('active');
    }
    listItems[step - 1].classList.add('active');
}

function prevStep() {
    if (currentStep === 1) return;
    currentStep--;
    showStep(currentStep);
    updateButtons();
}

function nextStep() {
    if (currentStep === steps.length) return;
    currentStep++;
    showStep(currentStep);
    updateButtons();
}


function updateButtons() {
    if (currentStep === 1) {
        prevBtn.style.display = 'inline-block';
    } else {
        prevBtn.style.display = 'inline-block';
    }
}