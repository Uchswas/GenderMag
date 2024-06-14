gm_session5 = {
    "scenario": "Ecampus CS162 student wants to figure out what to do to complete the course to be able to plan their term.",
    "persona": "ABI",
    "Subgoals": [
        {
            "subgoal": "Find the Syllabus page",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
             "subgoal_page_image" : "HomePage.html",
            "answers": "No",
            "facets_used": ["Motivations", "Information Processing Style", "Attitude Towards Risk", "Learning Style"],
            "why": "They see a list of announcements and a welcome. Abi would want to scroll down to see the rest of the text to see what’s on the homepage. Abi would want to read through the information provided on the homepage. Abi would be looking for any pointers toward their main goal. Abi has never seen an online Canvas course at OSU before, so she wouldn’t be looking for the syllabus page since that’s OSU-specific. Besides, a syllabus is usually not a source of deadlines and lists of activities.",
            "Actions": [
                {
                    "action": "Click 'Syllabus' on the left pane",
                    "before_action": {
                        "question": "Will Abi know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "HomePage.html",
                        "answers": [
                            "answer1: No; facets: Motivations, Information Processing Style, Attitude Towards Risk, Learning Style; why: She doesn’t know what the syllabus page is yet---she’d instead want to go read the intro paragraphs on the course homepage. There are a lot of options. There are also multiple ways of doing the same thing."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "AfterclickingonSyllabus.html",
                        "answers": [
                            "answer1: Maybe; facets: Motivations, Information Processing Style, Attitude Towards Risk; why: She sees Schedule in the title of one of the widgets which might be a pointer to what she is looking for. It’s not clear that a schedule is going to have all the due dates for Week 1 — maybe it’ll just have an overview of what’s happening during the course, like sometimes appears in syllabi."
                        ],
                    }
                }
            ]
        },
        {
           
            "subgoal": "Find the summary of activities and deadlines",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
             "subgoal_page_image" :  "AfterclickingonSyllabus.png",
            "answers": "Yes",
            "facets_used": ["Motivations", "Information Processing Style", "Attitude Towards Risk", "Learning Style"],
            "why": "Since this is connected with her main goal she would want to look for deadlines on tab titled ‘Schedule’",
            "Actions": [
                {
                    "action": "Scroll down to 'Course Summary' and read through it",
                    "before_action": {
                        "question": "Will Abi know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "AfterclickingonSyllabus.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style, Attitude Towards Risk, Learning Style; why: She would want to see further information on this page - to reach her goal faster and avoid exploring further. Can see Assignment 1, Assignment 2, and seems like there will be more beneath on the same screen."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "AfterclickingonSyllabus.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: Abi sees the schedule with Date Details, Time Due and list of assignments informing that this page shows listed assignments and their deadlines making her reach the main goal."
                        ],
                    }
                }
            ]
        },
        {
            "subgoal": "Find list of tools to be installed/Setup for the course",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" :  "AfterclickingonSyllabus.png",
            "answers": "Maybe",
            "facets_used": ["Motivations", "Learning Style"],
            "why": "She might not know if these instructions will be part of modules or she should be looking for them at this point before actually starting the course. It’s not clear what “tools” are — are they required? Useful? Recommended? There’s another page in the course called “Tools you will need” — different location (Modules > Start Here), different title, but same info:",
            "Actions": [
                {
                    "action": "Click on 'Tools' Tab on top",
                    "before_action": {
                        "question": "Will Abi know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": "AfterclickingonSyllabus.png",
                        "answers": [
                            "answer1: Maybe; facets: Information Processing Style, Learning Style; why: Since she sees the option on the widget on top, she might want to collect more information in case there were any setup instructions."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": "Afterclickingontools.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style, Computer Self-Efficacy, Attitude Towards Risk, Learning: by Process vs. by Tinkering; why: She sees a list of tools/software and corresponding instructions that she can follow to set up her computer for the course."
                        ],
                    }
                }
            ]
        }
    ]
}
