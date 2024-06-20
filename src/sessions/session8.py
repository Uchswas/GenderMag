"""
Source: GM_Forms_Session#7.pdf

"""


from constant import BASE_IMAGE_PATH




gm_session8= {
    "scenario": "Abi is going to register for ICSE and MSR",
    "persona" : "ABI",
    "Subgoals": [
        {
            "subgoal": "From home page, wants to go to registration forms page",
            "question": "Will Abi have formed this sub-goal as a step to their overall goal?",
            "subgoal_page_image" : BASE_IMAGE_PATH+"ICSE2019Home.png",
            "answers": "Maybe/No",
            "facets_used": ["Maybe: None of the above, No: Information Processing STyle, Attitude Towards Risk"],
            "why": "Agrees with the No’s recorded, but on the plus side, has already decided to register, so wants to move ahead with it. She wants to read the info about how much it all costs.",
            "Actions": [
                {
                    "action": "Read the fees",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Reg.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Informarion Processing Style, Attitude Towards Risk, Learning Style; why: Also has a limited amount of startup $."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Fees.png",
                        "answers": [
                            "answer1: Yes; facets: None of the above; why: Yes, making progress, but wondering exactly when her paper is being presented, because that would be cheaper..."
                        ],
                    }
                },
                {
                    "action": "Click on online registration form registration",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Registration.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: It’s obviously the way to proceed. She sees the link on top."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Registration.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Abi will finally see the button if she scrolls all the way to the bottom.",
                            "answer2: No; facets: None of the above; why: Abi says -- I don’t feel like I’m making progress -- where’s the form? Not clear that there’s a button at the bottom, so she may not scroll all the way to the bottom. The register now button is greyed out, she’s not sure she can register using that. Seems there is only a summary info."
                        ],
                    }
                },
                {
                    "action": "Scroll and Click on Register now",
                    "before_action": {
                        "question": "Will ABI know what to do at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019RegisterNow.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations, Information Processing Style; why: Yes if she sees it or if she notices the scrollbar.",
                            "answer2: No; facets: None of the above; why: No if she doesn't see the button (register now is at the bottom of the page)."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019RegisterNow.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: My Abi sees the top of the screen, which isn’t about Registration at all. If her screen were shorter, she wouldn’t see the Registration info, and then would wonder why she’s here.",
                            "answer2: Maybe; facets: None of the above; why: If she sees the bottom part of the page with the registrant info, she might be more confident she did the right thing."
                        ],
                    }
                },
                {
                    "action": "Scroll down and start filling the registration form & scroll & click next",
                    "before_action": {
                        "question": "Will ABI do this at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019RegistrationForm.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: That's her task, she’s motivated to do it.",
                            "answer2: Maybe; facets: None of the above; why: Limited budget, might want to check out membership to see if she can save $."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019RegistrationForm.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Likes that her info is now shown -- it’s in! Having more fields to fill out she knows in the right place. The progress bar in top -- she knows she’s on the right track.",
                            "answer2: Maybe; facets: None of the above; why: The odd blue squares don’t make much sense, but ok..."
                        ],
                    }
                },
                {
                    "action": "Fill out the page",
                    "before_action": {
                        "question": "Will ABI do this at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019Form.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She’s motivated to fill it out.",
                            "answer2: Maybe; facets: None of the above; why: Limited budget, might want to check out membership to see if she can save $."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019Form.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: This is what she expected and looks like the right thing.",
                            "answer2: Maybe; facets: None of the above; why: The odd blue squares don’t make much sense, but ok..."
                        ],
                    }
                },
                {
                    "action": "Click save and next",
                    "before_action": {
                        "question": "Will ABI do this at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019SaveNext.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Familiarity with forms. Just wants to get on with it.",
                            "answer2: Maybe; facets: None of the above; why: A bit confused: this screen has two saves and the other screen did not have a ‘save’ at all. What are the implications between SAVE and SAVE-and-NEXT? She would click ‘save’ and then ‘save and next’ to be sure and safe."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019SaveNext.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: After redo (providing state info). My Abi is grumpy about the Privacy Policy, but it does look like she’s making progress.",
                            "answer2: Maybe; facets: None of the above; why: The progress bar is very confusing. And the scrolling down wasn’t obvious to read the Privacy policy."
                        ],
                    }
                },
                {
                    "action": "Click on all the check boxes and click SAVE and NEXT",
                    "before_action": {
                        "question": "Will ABI do this at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019CheckBoxes.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Task oriented focus, she will fill it out and move on.",
                            "answer2: Maybe; facets: None of the above; why: Some Abi’s would go read Policies too, but will eventually do this. Abi is not happy about the red messages. Might look at the privacy policy and code of conduct but then click on everything to move on."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019CheckBoxes.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: More forms to fill so she knows she’s making progress.",
                            "answer2: Maybe; facets: None of the above; why: Progress bar not moving though."
                        ],
                    }
                },
                {
                    "action": "Check off the check boxes and click on SAVE and NEXT",
                    "before_action": {
                        "question": "Will ABI do this at this step? Why?",
                        "page_on_which_abi_take_the_action": BASE_IMAGE_PATH+"ICSE2019CheckBoxes.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: Doing it, but quite irritated, seems like this demographic info is asking a lot. A lot of buzz words that she doesn't really know what these are. Only interested in mining but the form is making her check another one -- Abi is irritated (has to select at least 2 or 3 software engineering interests). Probably have an ACM membership."
                        ],
                    },
                    "after_action": {
                        "question": "If Abi does the right thing, will s/he know that s/he did the right thing and is making progress toward their goal? Why?",
                        "page_on_which_abi_is_after_the_action": BASE_IMAGE_PATH+"ICSE2019CheckBoxes.png",
                        "answers": [
                            "answer1: Yes; facets: Motivations; why: She’s making progress.",
                            "answer2: Maybe; facets: None of the above; why: Progress bar not moving though."
                        ],
                    }
                }
            ]
        }
    ]
}
