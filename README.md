# Code-ADA-2024

This is our project for the Women in Computer Science's Code Ada Code to Cure 2024 Hackathon. We present a website aimed toward college students to easily match them with a therapist. Many college students struggle with finding a therapist who takes their insurance, is within their desired price range, and specializes in what they personally need. We use a scoring system to match registered therapists with registered patients on the website. We take into account factors such as gender preference, LGTBQ+ student preferences, price range, and more. Initially, the patient fills out a form detailing their mental health needs and all other necessary factors. The website uses a scoring system and ranks the therapists for the patient's needs. 

The most common mental health struggles in college students are depression, anxiety, ADHD, disordered eating, and PTSD. We use the sources below to estimate the student's needs based on symptoms they have experienced.

Depression section:

Installs virtual environment for python
```bash
sudo apt install python3.10-venv
```

Make virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Dependencies:
```bash
pip install numpy
pip install flask
```


How to run website

To run website to test locally run: 
```bash
python3 -m flask run
```

College Student Mental Health Sources:

Bowe, Kristen. “College Students and Depression.” Www.mayoclinichealthsystem.org, 22 Aug. 2023, www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/college-students-and-depression.

‌Mayo Clinic Staff. “Anxiety Disorders.” Mayo Clinic, Mayo Foundation for Medical Education and Research, 4 May 2018, www.mayoclinic.org/diseases-conditions/anxiety/symptoms-causes/syc-20350961.

‌“Open Path Collective.” Openpathcollective.org, 2024, openpathcollective.org/mental-health-topics/adhd/?msclkid=abfcf5ca4734188d216d92d9bceb1a7a&utm_source=bing&utm_medium=cpc&utm_campaign=OPC%20-%20Algorithm&utm_term=openpathcollective&utm_content=Group%202. Accessed 19 Oct. 2024.

‌ndic_support. “Is Your College Student Struggling with an Eating Disorder? The Warning Signs You Need to Know - National Eating Disorders Association.” National Eating Disorders Association, 24 Nov. 2020, www.nationaleatingdisorders.org/your-college-student-struggling-eating-disorder-warning-signs-you-need-know/. Accessed 19 Oct. 2024.

‌Mayo Clinic. “Eating Disorders .” Mayo Clinic, Mayo Foundation for Medical Education and Research, 2018, www.mayoclinic.org/diseases-conditions/eating-disorders/symptoms-causes/syc-20353603.

‌Mayo Clinic. “Post-Traumatic Stress Disorder (PTSD).” Mayo Clinic, Mayo Foundation for Medical Education and Research, 16 Aug. 2024, www.mayoclinic.org/diseases-conditions/post-traumatic-stress-disorder/symptoms-causes/syc-20355967.