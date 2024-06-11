"""
Source: GMsession1.docx.pdf
"""

gm_session_1 = {
    "scenario": "Ecampus CS162 student wants to figure out what to do during Week 1 and what the Week 1 deadlines are.",
    "Subgoals": [
        {
            "subgoal": "Find the Syllabus page",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "facets_used": ["Motivations", "Information Processing Style"],
            "why": "They see a list of announcements and a welcome. Abi would want to scroll down to see the rest of the text to see what’s on the homepage. Abi would want to read through the information provided on the homepage. Abi would be looking for any pointers toward their main goal. Abi has never seen an online Canvas course at OSU before, so she wouldn’t be looking for the syllabus page, since that’s OSU-specific (and usually a syllabus is not a source of deadlines and lists of activities).",
            "Actions": [
                {
                    "action": "Click 'Syllabus' on the left pane",
                    "before_action": {
                        "question": "Will Abi know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "HomePage.html",
                        "answers": [
                            "answer1: No; facets: None of the above; why: She doesn’t know what the syllabus page is yet---she’d instead want to go read the intro paragraphs on the course homepage"
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "AfterclickingonSyllabus.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She sees ‘Schedule’ in the title of one of the widgets which might be a pointer to what she is looking for"
                        ],
                    }
                }
            ]
        },
        {
            "subgoal": "Find the summary of activities and deadlines",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "answers": "Yes",
            "facets_used": ["Motivations", "Information Processing Style"],
            "why": "Since this is connected with her main goal she would want to look for deadlines on tab titled ‘Schedule’",
            "Actions": [
                {
                    "action": "Scroll down to 'Course Summary' and read through it",
                    "before_action": {
                        "question": "Will Abi know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "AfterclickingonSyllabus.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She would want to see further information on this page - to reach her goal faster and avoid exploring further."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "AfterclickingonSyllabus.html",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: Abi sees the schedule with Date Details, Time Due and list of assignments informing that this page shows listed assignments and their deadlines making her reach the main goal."
                        ],
                    }
                }
            ]
        }
    ]
}
