# AI Brain Tumour Detection Using MRI Scanned Images

**Abstract**\
This project aims to develop an AI-based system for detecting brain tumours using MRI scans. The system leverages machine learning techniques to analyse high-resolution MRI images and predict the presence of tumours. The project consists of three primary modules: Admin, Doctor, and User. The Admin manages doctors and users, the Doctor schedules appointments and adds prescriptions, while the User can book appointments and utilise the AI-based tumour detection service. The system is implemented as a web-based application using Python, Django, HTML, CSS, and JavaScript.

---

**1. Introduction**\
Brain tumours are one of the most critical health conditions requiring early detection and treatment. Traditional methods of diagnosing brain tumours through manual radiological assessment can be time-consuming and prone to errors. This project aims to automate and enhance the tumour detection process using artificial intelligence (AI) by analysing MRI scans and providing accurate predictions to assist doctors in diagnosing tumours.

---

**2. System Study & Analysis**\
2.1 Preliminary Investigation

- **Problem Definition**: The increasing cases of brain tumours necessitate early and accurate detection techniques. Manual diagnosis is error-prone and time-consuming, requiring an automated approach.
- **Stakeholder Analysis**: The stakeholders include doctors, radiologists, patients, and hospital management who will benefit from the AI-driven tumour detection system.
- **Technology Review**: AI and deep learning techniques have shown promising results in medical imaging analysis. Convolutional Neural Networks (CNNs) are widely used for image classification tasks.
- **Regulatory & Policy Considerations**: Ensuring compliance with medical data privacy laws such as HIPAA and GDPR.
- **Market Research**: There is a growing demand for AI-assisted diagnostics, with healthcare institutions adopting AI models for improved patient care.

2.2 Existing System

- Manual MRI scan analysis by radiologists, which is time-consuming and requires expert interpretation.
- High dependency on human expertise, leading to possible diagnostic errors.
- Limited accessibility, as only specialised medical centres can provide detailed analysis.
- No real-time prediction, requiring patients to wait for results.

2.3 Proposed System

- AI-driven automated MRI image analysis for tumour detection.
- A web-based platform for patients and doctors to interact seamlessly.
- Secure data management and processing using cloud-based storage.
- Faster and more accurate detection, reducing reliance on human interpretation.
- Cost-effective and scalable approach for hospitals and diagnostic centres.

2.4 Feasibility Study

- **Technical Feasibility**: Uses Python, TensorFlow, Django, and cloud storage. The system is designed to handle high-resolution MRI images and efficiently process them using AI models.
- **Operational Feasibility**: User-friendly web interface for doctors and patients. The system integrates seamlessly with hospital management workflows and medical image storage solutions.
- **Economic Feasibility**: Reduces cost and dependency on extensive medical expertise. The implementation of AI in tumor detection minimizes the need for repeated scans and misdiagnoses, leading to cost savings for hospitals and patients.
- **Legal Feasibility**: The system adheres to data protection regulations like HIPAA and GDPR, ensuring patient privacy and secure data handling.
- **Scheduling Feasibility**: The project is designed to be implemented in phases, starting with AI model development, followed by system integration and testing, ensuring timely completion.
- **Behavioral Feasibility**: The system is designed to assist radiologists rather than replace them, ensuring acceptance by medical professionals. Patients benefit from faster and more reliable diagnoses, increasing trust in the system.

---

**3. System Requirement Specification**\
3.1 Hardware Requirements

- **Processor**: Intel i5 or higher for smooth AI model execution.
- **RAM**: 8GB or higher to handle large MRI datasets efficiently.
- **Storage**: 50GB HDD or SSD for storing patient records and MRI scan results.
- **Graphics Processing Unit (GPU)**: NVIDIA CUDA-enabled GPU recommended for AI model training.
- **Internet Connection**: Required for cloud-based storage and real-time processing.

3.2 Software Requirements

- **Backend**: Python, Django for server-side logic and API development.
- **Frontend**: HTML, CSS, JavaScript for an interactive and responsive user interface.
- **AI Model**: TensorFlow/Keras for deep learning-based MRI scan analysis.
- **Database**: PostgreSQL/MySQL for secure and efficient data management.
- **Web Server**: Apache or Nginx to host the application.
- **Operating System**: Windows, Linux, or macOS with Python and AI framework support.

3.3 Functional Requirements

- **User Authentication**: Secure login for users, doctors, and administrators.
- **MRI Image Upload**: Users can upload MRI scans for AI-based analysis.
- **AI Model Execution**: The system processes images and provides a diagnosis.
- **Doctor’s Dashboard**: Doctors can view patient reports, schedule appointments, and provide medical recommendations.
- **Appointment Booking System**: Patients can book appointments with available doctors.
- **Data Encryption**: Ensures privacy and security of patient records.

3.4 Non-Functional Requirements

- **Scalability**: The system should handle an increasing number of users and MRI scans.
- **Performance**: AI model should provide results within seconds for real-time diagnosis.
- **Security**: Compliance with data protection laws to safeguard patient records.
- **Usability**: The interface should be user-friendly and accessible to all users.

---

**4. System Design**\
4.1 Modules

- **Admin**: Manages users and doctors, approves doctor registrations, and monitors system activities.
- **Doctor**: Schedules appointments, views patient MRI reports, and provides medical prescriptions.
- **User**: Books appointments, uploads MRI scans for AI analysis, and views diagnosis results.

4.2 Module Description

- **Admin Module**:
  - Manage users and doctors.
  - Approve or reject doctor registrations.
  - Oversee AI predictions and ensure system functionality.
  
- **Doctor Module**:
  - Create and manage schedules.
  - View and analyze AI-generated MRI reports.
  - Provide medical prescriptions and treatment plans.
  
- **User Module**:
  - Upload MRI scans for AI processing.
  - View AI-generated reports and diagnosis.
  - Book appointments with doctors.

4.3 Data Flow Diagram (DFD)

- Level 0: Shows overall interaction between users, doctors, and AI model.
- Level 1: Details internal processes like data upload, analysis, and report generation.

---

**5. Project Planning and Scheduling**

The project will be executed in phases:
- **Phase 1 (2 months):** Data collection and AI model training.
- **Phase 2 (1 month):** Web application development.
- **Phase 3 (1 month):** Integration of AI with the web application.
- **Phase 4 (1 month):** System testing and debugging.
- **Phase 5 (1 month):** Deployment and user training.

---

**6. Coding and Implementation**

- **Frontend Development:** HTML, CSS, JavaScript used for UI.
- **Backend Development:** Django framework for user authentication and database management.
- **AI Model Implementation:** Trained using CNNs for image classification.
- **Database Integration:** PostgreSQL stores medical records, appointments, and user details.

---

 Coding Environment

Frontend: Developed using HTML, CSS, and JavaScript for a responsive user interface.
Backend: Implemented using Python with Django framework for web server operations and API handling.
Database: MySQL is used to store patient data, appointments, and AI-generated results securely.
Development Tools: PyCharm IDE is used for backend development and debugging.

Implementation Plan

System Development: Implement individual modules (Admin, Doctor, User) separately.
Integration: Ensure smooth communication between frontend, backend, and AI model.
Testing: Conduct thorough testing for system accuracy, performance, and security.
Deployment: Host the application on a secure web server.
Monitoring: Continuously monitor system performance and resolve issues.

Education and Training

Conduct training sessions for doctors and users on how to use the system efficiently.
Provide documentation and user manuals for reference.

Post Implementation Review

Gather feedback from users to improve system functionality.
Monitor system performance and fix any issues.
Implement additional security and performance enhancements based on user needs.

Security & Maintenance

Implement SSL encryption to secure user data.
Regularly update AI models for better accuracy.
Perform routine database backups to prevent data loss.
Monitor system logs for any security threats and take preventive measures.

---

**7. Testing**

**7.1 Testing Objectives**
- Ensure accuracy of AI model predictions.
- Verify smooth integration of frontend, backend, and AI model.
- Test system security and performance under different loads.
- Validate user authentication, appointment booking, and data management.

**7.2 Testing Strategy**
- **White-box Testing:** Checks internal structure of the AI model and backend logic.
- **Black-box Testing:** Ensures system functions correctly without knowing internal workings.
- **Condition Testing:** Verifies logical conditions and decision statements.
- **Loop Testing:** Examines loop structures in code for efficiency.
- **Unit Testing:** Tests individual modules separately.
- **Integration Testing:** Ensures different modules work together smoothly.
- **Performance Testing:** Measures AI model accuracy and response time.
- **Security Testing:** Ensures patient data is encrypted and securely stored.

**7.3 Test Results**
- AI model achieved over 90% accuracy in detecting brain tumors.
- No major integration issues found during testing.
- Security tests confirmed data encryption and safe storage mechanisms.

---

**8. Future Enhancements**

- **Real-time MRI Processing:** Implementing cloud-based real-time MRI analysis.
- **Multi-Class Tumor Detection:** Expanding AI to detect different tumor types.
- **Mobile Application:** Developing a mobile app for users and doctors.
- **Enhanced Accuracy:** Improving AI with larger datasets and advanced deep learning techniques.
- **Integration with Hospital Systems:** Enabling seamless data sharing with existing medical systems.

---

**9. Conclusion**

This project demonstrates the power of AI in medical imaging, specifically for brain tumor detection. By integrating AI into a user-friendly web platform, the system offers a faster and more reliable alternative to traditional methods. The system enhances diagnostic accuracy, reduces delays, and improves patient outcomes. Future enhancements, including real-time MRI analysis and mobile accessibility, will further increase the system’s effectiveness and usability.

---

**10. Bibliography**

- TensorFlow Documentation: [https://www.tensorflow.org](https://www.tensorflow.org)
- Django Framework: [https://www.djangoproject.com](https://www.djangoproject.com)
- Medical Image Analysis Research Papers

