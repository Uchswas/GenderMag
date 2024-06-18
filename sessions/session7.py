"""
Source: GM_Forms_Session#6.pdf

"""
from constant import BASE_IMAGE_PATH

gm_session6 = {
    "scenario": "Abi (is Chinese citizen, lives in US (NOT a permanent resident)) has decided to go to ICSE and is looking into Travel Visa stuff now",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "Look for visa information in the conference website",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Home.png",
            "answers": "Yes/Maybe",
            "facets_used": ["Motivations", "Information Processing Style","Attitude Towards Risk"],
            "why": "She wants to go to ICSE, so she will want to find information. She is risk averse so she wants to be sure she has info about the visa. She wants to get the whole picture and have the idea of what kind of visa to get to go to ICSE.",
            "Actions": [
                {
                    "action": "Click attending",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: None of the Above; why: Only match.",
                            "answer2: Maybe; facets: Information Processing Style; why: She would like to investigate the page first before clicking."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Styke; why: She is going to read the whole list. (mot) She is looking for Visa...and she sees visa."
                        ],
                    }
                },
                {
                    "action": "Click on Visa",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Same as facets: Motivation."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She is seeing all the breadcrumbs to know that she is making progress."
                        ],
                    }
                }
                {
                    "action": "Click on Visa",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Home.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Same as facets: Motivation."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: She is seeing all the breadcrumbs to know that she is making progress."
                        ],
                    }
                }
                {
                    "action": "Read the visa lnvitation letter",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets: Information Processing Style, Attitude Towards Risk; why: She wants to make sure that she is going to get the visa before spending the money.",
                            "answer2: Maybe; facets: Information Processing Style, Attitude Towards Risk; why: She will click on Entry requirements to see if there is anything else that she should know. She wants to know anything more specific to her situation"

                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Visa.png",
                        "answers": [
                            "answer1: Yes; facets:  Attitude Towards Risk, Learnign Style; why: Catch 22... she has to spend the registration $$ before she knows she will get the visa. Is she eligible for a refund if the visa is denied? She wants to know a bit more information. There is also a process outlined."
                        ],
                    }
                }
            ]
        }
    ]
}
