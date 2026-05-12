#data.py 

SKILL_ALIASES = {
    # Languages
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "cpp": "cpp",
    "r": "r",
    "kotlin": "kotlin",

    # ML / Data
    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",
    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics",
    "stats": "statistics",
    "regression": "regression",
    "clustering": "clustering",
    "data-viz": "data_visualization",
    "data visualization": "data_visualization",
    "data viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "power bi": "data_visualization",
    "powerbi": "data_visualization",
    "pandas": "pandas",
    "numpy": "numpy",

    # Web — Frontend
    "react": "react",
    "reacts": "react",
    "reactjs": "react",
    "vue": "vue",
    "vue.js": "vue",
    "vuejs": "vue",
    "redux": "redux",
    "tailwind": "tailwind",
    "html/css": "html_css",
    "html css": "html_css",
    "html": "html_css",
    "css": "html_css",
    "jest": "jest",
    "graphql": "graphql",

    # Web — Backend
    "node.js": "nodejs",
    "nodejs": "nodejs",
    "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot",
    "springboot": "spring_boot",
    "rest api": "rest_api",
    "rest": "rest_api",
    "restapi": "rest_api",
    "microservices": "microservices",

    # Databases
    "sql": "sql",
    "mysql": "mysql",
    "mysq": "mysql",
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "mongodb": "mongodb",
    "redis": "redis",

    # DevOps / Cloud
    "docker": "docker",
    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "k8s": "kubernetes",
    "ci/cd": "ci_cd",
    "cicd": "ci_cd",
    "ci cd": "ci_cd",
    "aws": "aws",

    # Mobile
    "android": "android",
    "firebase": "firebase",

    # CS Fundamentals
    "algorithms": "algorithms",
    "algoritms": "algorithms",
    "data structure": "data_structures",
    "data structures": "data_structures",
    "competitive programming": "competitive_programming",
    
    # Design
    "ui/ux": "ui_ux",
    "ui ux": "ui_ux",
    "figma": "figma",
}

RESUMES = {
    "01": {
        "ID": "01",
        "Candidate": "Arjun Sharma",
        "Raw Skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning",
        "Background": "TCS Intern · BITS Pilani CSE 2024"
    },
    "02": {
        "ID": "02",
        "Candidate": "Priya Nair",
        "Raw Skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS",
        "Background": "Freelance Web Developer · VIT IT 2024"
    },
    "03": {
        "ID": "03",
        "Candidate": "Rahul Gupta",
        "Raw Skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates",
        "Background": "Infosys SDE Intern · IIT Delhi 2023"
    },
    "04": {
        "ID": "04",
        "Candidate": "Sneha Patel",
        "Raw Skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib",
        "Background": "IISc Research Assistant · IIIT Hyderabad AI 2024"
    },
    "05": {
        "ID": "05",
        "Candidate": "Vikram Singh",
        "Raw Skills": "C++, Algoritms, Data Structure, competitive programming, python",
        "Background": "Google SWE Intern · IIT Bombay 2024"
    },
    "06": {
        "ID": "06",
        "Candidate": "Ananya Krishnan",
        "Raw Skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD",
        "Background": "Full Stack Developer · NIT Trichy 2022"
    },
    "07": {
        "ID": "07",
        "Candidate": "Karan Mehta",
        "Raw Skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau",
        "Background": "Data Analyst · Delhi University 2023"
    },
    "08": {
        "ID": "08",
        "Candidate": "Deepika Rao",
        "Raw Skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma",
        "Background": "Samsung Android Intern · NSIT 2024"
    },
    "09": {
        "ID": "09",
        "Candidate": "Aditya Kumar",
        "Raw Skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest",
        "Background": "Frontend SDE · Flipkart / IIIT Bangalore"
    },
    "10": {
        "ID": "10",
        "Candidate": "Meera Iyer",
        "Raw Skills": "python, R, statistics, ML, regression, clustering, Power-BI",
        "Background": "Data Science Intern · Wipro 2024"
    }
}

JOB_DESCRIPTIONS = {
    "JD-1": {
        "ID": "JD-1",
        "Company": "Kakao",
        "Role": "ML Engineer",
        "Required Skills": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization",
        "Preferred Skills": "NLP, BERT, Feature Engineering, Statistics"
    },
    "JD-2": {
        "ID": "JD-2",
        "Company": "Naver",
        "Role": "Backend Engineer",
        "Required Skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes",
        "Preferred Skills": "REST API, CI/CD, Redis"
    },
    "JD-3": {
        "ID": "JD-3",
        "Company": "Line",
        "Role": "Frontend Engineer",
        "Required Skills": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS",
        "Preferred Skills": "Node.js, GraphQL, Redux, Jest, AWS"
    }
}