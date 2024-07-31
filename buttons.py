from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

DEPARTMENT_BUTTONS = [
    [
        InlineKeyboardButton("Electricity", callback_data="department_electricity"),
        InlineKeyboardButton("Computer", callback_data="department_computer"),
    ],
    [
        InlineKeyboardButton("Mechanical", callback_data="department_mechanical"),
        InlineKeyboardButton("Other", callback_data="department_other"),
    ],
]

DEPARTMENT_NAMES = {
    "electricity": "Electricity",
    "computer": "Computer",
    "mechanical": "Mechanical",
    "other": "Other",
}

SPECIALIZATION_NAMES = {
    "electrician_intern": "Electrician Intern",
    "electronic_parts_tester": "Electronic Parts Tester",
    "electronic_orders_employee": "Electronic Orders Employee",
    "documenter": "Documenter",
    "electrical_technician": "Electrical Technician",
    "power_electronics_specialist": "Power Electronics Specialist",
    "product_integration_engineer": "Product Integration Engineer",
    "pcb_designer": "PCB Designer",
    "assembly_technician": "Assembly Technician",
    "telecommunication_engineer": "Telecommunication Engineer",
    "electronics_technician": "Electronics Technician",
    "testing_and_troubleshooting_specialist": "Testing and Troubleshooting Specialist",
    "hardware_intern": "Hardware Intern",
    "software_intern": "Software Intern",
    "network_technician": "Network Technician",
    "data_scientist": "Data Scientist",
    "programmer": "Programmer",
    "c_plus_plus_programmer": "C++ Programmer",
    "hardware_specialist": "Hardware Specialist",
    "manufacturing": "Manufacturing",
    "vibration_analysis": "Vibration Analysis",
    "energy_conversion": "Energy Conversion",
    "heat_and_fluids": "Heat and Fluids",
    "draftsman": "Draftsman",
    "mechanical_quality_control_specialist": "Mechanical Quality Control Specialist",
    "turner": "Turner",
    "miller": "Miller",
    "human_resources_specialist": "Human Resources Specialist",
    "industrial_engineer": "Industrial Engineer",
    "business_administration_specialist": "Business Administration Specialist",
    "accountant": "Accountant",
}

SPECIALIZATION_BUTTONS = {
    "electricity": [
        [
            InlineKeyboardButton(
                "Electrician Intern", callback_data="specialization-electrician_intern"
            )
        ],
        [
            InlineKeyboardButton(
                "Electronic Parts Tester",
                callback_data="specialization-electronic_parts_tester",
            )
        ],
        [
            InlineKeyboardButton(
                "Electronic Orders Employee",
                callback_data="specialization-electronic_orders_employee",
            )
        ],
        [InlineKeyboardButton("Documenter", callback_data="specialization-documenter")],
        [
            InlineKeyboardButton(
                "Electrical Technician",
                callback_data="specialization-electrical_technician",
            )
        ],
        [
            InlineKeyboardButton(
                "Power Electronics Specialist",
                callback_data="specialization-power_electronics_specialist",
            )
        ],
        [
            InlineKeyboardButton(
                "Product Integration Engineer",
                callback_data="specialization-product_integration_engineer",
            )
        ],
        [
            InlineKeyboardButton(
                "Electrical Specialist",
                callback_data="specialization-electrical_specialist",
            )
        ],
        [
            InlineKeyboardButton(
                "PCB Designer", callback_data="specialization-pcb_designer"
            )
        ],
        [
            InlineKeyboardButton(
                "Assembly Technician",
                callback_data="specialization-assembly_technician",
            )
        ],
        [
            InlineKeyboardButton(
                "Telecommunication Engineer",
                callback_data="specialization-telecommunication_engineer",
            )
        ],
        [
            InlineKeyboardButton(
                "Electronics Technician",
                callback_data="specialization-electronics_technician",
            )
        ],
        [
            InlineKeyboardButton(
                "Testing and Troubleshooting Specialist",
                callback_data="specialization-testing_and_troubleshooting_specialist",
            )
        ],
    ],
    "computer": [
        [
            InlineKeyboardButton(
                "Hardware Intern", callback_data="specialization-hardware_intern"
            )
        ],
        [
            InlineKeyboardButton(
                "Software Intern", callback_data="specialization-software_intern"
            )
        ],
        [
            InlineKeyboardButton(
                "Network Technician",
                callback_data="specialization-network_technician",
            )
        ],
        [
            InlineKeyboardButton(
                "Data Scientist",
                callback_data="specialization-data_scientist",
            )
        ],
        [
            InlineKeyboardButton(
                "Programmer",
                callback_data="specialization-programmer",
            )
        ],
        [
            InlineKeyboardButton(
                "C++ Programmer", callback_data="specialization-c_plus_plus_programmer"
            )
        ],
        [
            InlineKeyboardButton(
                "Hardware Specialist",
                callback_data="specialization-hardware_specialist",
            )
        ],
    ],
    "mechanical": [
        [
            InlineKeyboardButton(
                "Manufacturing", callback_data="specialization-manufacturing"
            )
        ],
        [
            InlineKeyboardButton(
                "Vibration Analysis", callback_data="specialization-vibration_analysis"
            )
        ],
        [
            InlineKeyboardButton(
                "Energy Conversion", callback_data="specialization-energy_conversion"
            )
        ],
        [
            InlineKeyboardButton(
                "Heat and Fluids", callback_data="specialization-heat_and_fluids"
            )
        ],
        [InlineKeyboardButton("Draftsman", callback_data="specialization-draftsman")],
        [
            InlineKeyboardButton(
                "Mechanical Quality Control Specialist",
                callback_data="specialization-mechanical_quality_control_specialist",
            )
        ],
        [InlineKeyboardButton("Turner", callback_data="specialization-turner")],
        [InlineKeyboardButton("Miller", callback_data="specialization-miller")],
    ],
    "other": [
        [
            InlineKeyboardButton(
                "Human Resources Specialist",
                callback_data="specialization-human_resources_specialist",
            )
        ],
        [
            InlineKeyboardButton(
                "Industrial Engineer",
                callback_data="specialization-industrial_engineer",
            )
        ],
        [
            InlineKeyboardButton(
                "Business Administration Specialist",
                callback_data="specialization-business_administration_specialist",
            )
        ],
        [InlineKeyboardButton("Accountant", callback_data="specialization-accountant")],
    ],
}

POSITION_DESCRIPTIONS = {
    "electrician_intern": "Job Description:\nCollaboration in large national projects\nConditions:\nProficiency in specialized subjects\nInterest in learning and progress",
    "electronic_parts_tester": "Job Description:\nTesting and inspecting electronic parts\nRequired skills and conditions:\n\nFamiliarity with designing inspection tests for electronic parts\nFamiliarity with working with measuring devices and report writing principles\nFamiliarity with inspection and quality assurance principles\nStudent or graduate with a bachelor's degree in electronics\nAbility to understand technical texts in English",
    "electronic_orders_employee": "Job Description:\nWorking with files and Excel programs to review statistics and provide necessary parts\nReceiving electronic parts and separating parts and forming desired assemblies for assembly",
    "documenter": "Preparing reports and documentation for electronic and telecommunications projects",
    "electrical_technician": "Performing technical tasks in the field of electricity and electronics",
    "power_electronics_specialist": "Job Description:\nParticipation in the design and testing of power electronics circuits and modules\nRequired skills and conditions:\nStudent or graduate with a bachelor's or master's degree in power\nFamiliarity with Altium and Cadence software\nFamiliarity with power electronics converters\nFamiliarity with working with test equipment",
    "product_integration_engineer": "Job Description:\nRepair and maintenance of telecommunications and electronic devices, repair of various boards",
    "pcb_designer": "Job Description:\nPCB design\nHandling PCB order-related tasks\nRequired skills:\nFamiliarity with English to understand technical texts and component datasheets",
    "assembly_technician": "Job Description:\nAssembly of electronic parts, modules, cabling, SMD\n\nRequired skills:\nFamiliarity with assembly tools",
    "telecommunication_engineer": "Job Description:\nDesigning antennas and microwave and millimeter waveguides, designing and implementing antenna test and measurement systems\nDesigning active and passive microwave circuits, testing and tuning microwave modules\nRequired skills and conditions:\nStudent or graduate with a master's degree\nFamiliarity with specialized telecommunications software",
    "electronics_technician": "Job Description:\nRepair and maintenance of telecommunications and electronic devices, repair of various boards",
    "testing_and_troubleshooting_specialist": "Job Description:\nTesting telecommunications subsystems and integrated assemblies\nRequired skills and conditions:\nStudent or graduate with a bachelor's or master's degree in electronics or telecommunications\nBasic familiarity with test equipment",
    "hardware_intern": "Job Description:\nCollaboration in large national projects\nConditions:\nProficiency in specialized subjects\nInterest in learning and progress",
    "software_intern": "Job Description:\nCollaboration in large national projects\nConditions:\nProficiency in specialized subjects\nInterest in learning and progress",
    "network_technician": "Job Description and Tasks\nPerforming Help Desk tasks, Passive\nRequired skills and conditions:\nFamiliarity with network fundamentals (+Network)\nFamiliarity with Microsoft and Cisco services\nFamiliarity with hardware and software maintenance and troubleshooting",
    "data_scientist": "Job Description:\nIdentifying problems and extracting solutions based on data using coding, math, and problem-solving skills\nData preparation\nSelection of appropriate models and algorithms\nUsing specialized libraries\nCommunication and collaboration with the project team\nQualifications:\nGraduate with a bachelor's or master's degree in engineering, computer science, or related fields\nInterest in working in the field of data science",
    "programmer": "Job Description:\nWriting new code and modifying existing programs and applications\nDiagnosing errors and troubleshooting issues\nDeveloping and implementing solutions\nRequired skills and conditions:\nBachelor's degree in computer science or related fields\nProficiency in coding languages such as Python, Java, or C++",
    "c_plus_plus_programmer": "Job Description:\nProgramming in C++\nRequired skills and conditions:\nBachelor's degree in computer science or related fields\nProficiency in C++ programming",
    "hardware_specialist": "Job Description:\nDesigning, developing, and testing computer hardware\nCollaborating with software developers to ensure hardware and software compatibility\nRequired skills and conditions:\nBachelor's degree in computer science or related fields\nProficiency in hardware design and development",
    "manufacturing": "Job Description:\nInvolvement in the production and manufacturing processes\nRequired skills and conditions:\nUnderstanding of manufacturing principles\nAbility to operate machinery and tools",
    "vibration_analysis": "Job Description:\nAnalyzing vibration data to identify potential issues in machinery and equipment\nRequired skills and conditions:\nUnderstanding of vibration analysis techniques\nAbility to interpret and analyze data",
    "energy_conversion": "Job Description:\nWorking on projects related to energy conversion and management\nRequired skills and conditions:\nKnowledge of energy conversion principles\nAbility to design and implement energy systems",
    "heat_and_fluids": "Job Description:\nWorking on projects related to heat transfer and fluid dynamics\nRequired skills and conditions:\nUnderstanding of heat transfer and fluid dynamics principles\nAbility to conduct experiments and analyze data",
    "draftsman": "Job Description:\nCreating technical drawings and plans for mechanical projects\nRequired skills and conditions:\nProficiency in CAD software\nAbility to interpret and create technical drawings",
    "mechanical_quality_control_specialist": "Job Description:\nEnsuring the quality of mechanical products and processes\nRequired skills and conditions:\nKnowledge of quality control principles\nAbility to conduct inspections and tests",
    "turner": "Job Description:\nOperating lathes to produce precision parts\nRequired skills and conditions:\nProficiency in operating lathes\nAbility to read and interpret technical drawings",
    "miller": "Job Description:\nOperating milling machines to produce precision parts\nRequired skills and conditions:\nProficiency in operating milling machines\nAbility to read and interpret technical drawings",
    "human_resources_specialist": "Job Description:\nManaging HR tasks such as recruitment, employee relations, and performance management\nRequired skills and conditions:\nKnowledge of HR principles and practices\nStrong communication and interpersonal skills",
    "industrial_engineer": "Job Description:\nOptimizing production processes and systems\nRequired skills and conditions:\nKnowledge of industrial engineering principles\nAbility to analyze and improve processes",
    "business_administration_specialist": "Job Description:\nManaging administrative tasks and supporting business operations\nRequired skills and conditions:\nKnowledge of business administration principles\nStrong organizational and multitasking skills",
    "accountant": "Job Description:\nManaging financial transactions and records\nRequired skills and conditions:\nKnowledge of accounting principles\nProficiency in accounting software",
}

inline_back_button = [InlineKeyboardButton("Back", callback_data="back")]


def get_department_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(DEPARTMENT_BUTTONS)
    return markup


def get_back_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("back", callback_data="back")]])


def get_specialization_markup(department_name: str) -> InlineKeyboardMarkup:
    inline_buttons = SPECIALIZATION_BUTTONS[department_name] + [inline_back_button]
    return InlineKeyboardMarkup(inline_buttons)


def get_position_description(position_name: str) -> str:
    return POSITION_DESCRIPTIONS[position_name]
