let introductionScript = {
  name: 'Procrastination Script',
  solution: 'Student Edge',
  subSolution: 'procrastination',
  version: 1.0,
  steps: [
    {
      step: '1.1',
      name: 'Verify Name',
      clearPage: true,
      questions: [
        {
          question: "<p>Thank you for calling DragonFly HPE, This is ${AGENT_FIRST_NAME}. <br>Before we get started, I just need to verify a few pieces of information. <br>Am I speaking with ${CUSTOMER_FIRST_NAME}?</p>",
          variables: [
            {
              AGENT_FIRST_NAME: {
                type: 'text',
                editable: false
              },
              CUSTOMER_FIRST_NAME: {
                type: 'text',
                editable: true
              }
            }
          ],
          action: {
            type: 'radio',
            options: [
              {
                option: 'YES',
                behavior: 'SHOW 1.1.1'
              },
              {
                option: 'NO',
                behavior: 'SHOW 1.1.2'
              }
            ]
          }
        }
      ]
    },
    {
      step: '1.1.1',
      name: 'Verify Name',
      questions: [
        {
          question: "And is that what you prefer to be called?",
          action: {
            type: 'button',
            buttonText: 'Next',
            behavior: 'NAVIGATE 1.2'
          }
        }
      ]
    },
    {
      step: '1.1.2',
      name: 'Verify Name',
      questions: [
        {
          question: "Oh, I'm sorry. Who am I speaking with today?",
          action: {
            type: 'button',
            buttonText: 'Next',
            behavior: 'NAVIGATE 1.2'
          }
        }
      ]
    },
    {
      step: '1.2',
      name: 'Verify Name',
      clearPage: true,
      questions: [
        {
          question: "<p>Hi {{CUSTOMER_FIRST_NAME}}. Like I said, my name is {{AGENT_FIRST_NAME}}. I'll be your performance specialist today. <br>I see you're calling about {{SUBSOLUTION}}. Is that right?</p>",
          variables: [
            {
              AGENT_FIRST_NAME: {
                type: 'text',
                editable: false
              },
              CUSTOMER_FIRST_NAME: {
                type: 'text',
                editable: false
              },
              SUBSOLUTION: {
                type: 'dropdown',
                options: [
                  'Study Skills', 'Procrastination Hack', 'Time Management', 'Academic Mindset', 'Crunch Time'
                ],
                editable: true
              }
            }
          ],
          action: {
            type: 'button',
            buttonText: 'Next',
            behavior: 'NAVIGATE 1.3'
          }
        }
      ]
    },
  ]
}

module.exports = introductionScript