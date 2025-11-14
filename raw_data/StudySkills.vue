<template>
  <div class="mb-3">
    <p class="text-xl font-semibold mb-3">Call Application, Goals and Time Constraints</p>
    <p>Why don't you start off by telling me a little bit about why you are calling today.</p>
    <p>Feel free to share any details you think might be relevant to your call today. For instance:</p>
    <ul class="ml-5">
      <li>Is there a particular assignment or exam you're studying for,</li>
      <li>Or, are you calling for more general study tips?</li>
    </ul>
    <br>
    <p class="font-semibold">Caller Application (Caller Response)</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="caller-application" value="exam-prep" v-model="callerApplication" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Specific Application / Exam Preparation</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="general-study" v-model="callerApplication" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">General Study Skills</label>
        </div>
      </div>
    </fieldset>
    <br>
    <p>Are you working with any time constraints, like upcoming deadlines?</p>
    <ul class="ml-5">
      <li>Less than 24 hours</li>
      <li>Specific Time Constraint</li>
      <li>None</li>
    </ul>
    <br>
    <p>What would you like to accomplish immediately after this call. That is, what do you hope our session will prepare you to do?</p><br>
    <p>Or, do you have future goals that you are pursuing that require better study skills?</p><br>
    <p>IF SPECIFIC APPLICATION: How will doing your best on <span class="font-semibold">[APPLICATION]</span> benefit your future?</p><br>
    <p class="font-semibold">Caller Goals for this Session</p>
    <textarea rows="3" placeholder="Agent Notes: Caller Goals" class="w-3/4 my-3"></textarea>
    <p>How do you think better study skills will help you achieve your goals?</p><br>
    <p class="italic">Confirm and clarify above selections and call goals before continuing.</p>
  </div>
  <hr>
  <div class="my-3">
    <p>Could you tell me a bit about your current study practices? I just want to get a sense of what you're already doing to establish a baseline we can work from.</p><br>
    <p class="font-semibold">Current Practices</p>
    <fieldset class="my-3">
      <div class="space-y-3">
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="note-taking" v-model="currentPractices" value="note-taking" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="note-taking" class="text-gray-900">Note Taking (In Class)</label>
            <p v-if="currentPractices.indexOf('note-taking') !== -1">When you take notes, do you primarily take notes by hand or digitally?</p>
            <fieldset v-if="currentPractices.indexOf('note-taking') !== -1" class="mt-3">
              <div class="space-y-2">
                <div class="relative flex items-start">
                  <div class="flex h-6 items-center">
                    <input id="note-taking-by-hand" v-model="noteTakingTypes" value="by-hand" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="ml-3 text-sm leading-6">
                    <label for="note-taking-by-hand" class="text-gray-900">By Hand</label>
                  </div>
                </div>
                <div class="relative flex items-start">
                  <div class="flex h-6 items-center">
                    <input id="note-taking-digital" v-model="noteTakingTypes" value="digital" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="ml-3 text-sm leading-6">
                    <label for="note-taking-digital" class="text-gray-900">Digital</label>
                  </div>
                </div>
              </div>
            </fieldset>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="review" v-model="currentPractices" value="review" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="review" class="text-gray-900">Reviewing / Re-watching course lectures or slide decks</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="reading" v-model="currentPractices" value="reading" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="reading" class="text-gray-900">Reading / Highlighting</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="review-notes" v-model="currentPractices" value="review-notes" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="review-notes" class="text-gray-900">Reviewing Notes</label>
            <fieldset v-if="currentPractices.indexOf('review-notes') !== -1" class="mt-3">
              <div class="space-y-2">
                <div class="relative flex items-start">
                  <div class="flex h-6 items-center">
                    <input id="soon-after" v-model="reviewTime" value="soon-after" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="ml-3 text-sm leading-6">
                    <label for="soon-after" class="text-gray-900">Soon after class</label>
                  </div>
                </div>
                <div class="relative flex items-start">
                  <div class="flex h-6 items-center">
                    <input id="end-of-week" v-model="reviewTime" value="end-of-week" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  </div>
                  <div class="ml-3 text-sm leading-6">
                    <label for="end-of-week" class="text-gray-900">End of week or prior to test / exam</label>
                  </div>
                </div>
              </div>
            </fieldset>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="self-testing" v-model="currentPractices" value="self-testing" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="self-testing" class="text-gray-900">Self-testing or pre-testing</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="mnemonics" v-model="currentPractices" value="mnemonics" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="mnemonics" class="text-gray-900">Creating mnemonics to help remember information</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="connections" v-model="currentPractices" value="connections" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="connections" class="text-gray-900">Making connections between different concepts or classes</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="flashcards" v-model="currentPractices" value="flashcards" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="flashcards" class="text-gray-900">Using flashcards</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="other-practice" v-model="currentPractices" value="other" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="other-practice" class="text-gray-900">Other</label>
            <input type="text" v-model="otherPractice" id="other-practice" class="w-96 block rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Agent Notes" />
          </div>
        </div>
      </div>
    </fieldset>
    <p class="font-semibold">Study Session Frequency (per class or total?)</p>
    <fieldset class="my-3">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="caller-application" value="none" v-model="studyFrequency" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm leading-6 text-gray-900">None</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="1-2" v-model="studyFrequency" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm leading-6 text-gray-900">1-2 times per week</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="3-4" v-model="studyFrequency" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm leading-6 text-gray-900">3-4 times per week</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="5-6" v-model="studyFrequency" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm leading-6 text-gray-900">5-6 times per week</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="6+" v-model="studyFrequency" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm leading-6 text-gray-900">More than 6 times per week</label>
        </div>
      </div>
    </fieldset>
    <p class="font-semibold">Average Study Session Duration:</p>
    <div class="flex my-3 items-center">
      <input type="number" class="text-sm mr-2 w-16" v-model="averageHour">
      <span class="mr-6">hours </span>
      <input type="number" class="text-sm mr-2 w-16" v-model="averageMinute">
      <span>minutes </span>
    </div>
  </div>
  <hr>
  <div v-if="currentPractices.indexOf('note-taking') !== -1" class="my-3">
    <p>While preparation is important, </p>
    <p>Note-taking is an essential skill.</p>
    <p>Studies show that handwritten notes are more effective than taking notes on the computer.</p>
    <p>If you are able, we recommend taking notes by hand instead of on the computer.</p><br>
    <p>I recommend using the StudySkills because it helps prioritize specific actions that really work with effective learning practices.</p>
    <p>Here’s how it works.</p>
    <p>Whenever you turn to a new page of your notebook, you’ll divide the paper into 4 sections:</p>
    <ul class="ml-6">
      <li>a header at the top</li>
      <li>a footer at the bottom, and</li>
      <li>2 columns dividing the space in the middle
        <ul class="ml-6">
          <li>a narrower, marginal column on the Left that is still wide enough to add questions and additional comments after the lecture or class, and</li>
          <li>a wider one to the right where the main body of your notes will go.</li>
          <li>If you’re using standard lined paper, you can use the red line going down the left side of the sheet as a guide for separating the two columns.</li>
        </ul>
      </li>
    </ul>
    <br>
    <p>The header section is for your class title and the date. You could add other identifying information to help you quickly access the information later, like the lecture title or the main topics covered.</p>
    <p>The larger, right-hand column is for your own notes during the lecture. If your instructor is delivering the lecture using PowerPoint slides or another presentation software, don’t copy down the information on the slides word for work. Put information in your own words using concise sentences and keywords that can jog your memory later.</p>
    <p>We’ll talk about what you do with the other two columns next, when we talk about how to best structure individual study sessions.</p>
  </div>
  <hr>
  <div class="my-3">
    <p>Before we dive too deep into some skills and practices you can use to supercharge your learning, let’s talk briefly about some mental and physical preparation you can do to help you perform at your best.</p><br>
    <p class="font-semibold">Physical Preparation</p>
    <ul class="ml-6">
      <li><span class="italic">Drink.</span> Plenty of water throughout the day;</li>
      <li><span class="italic">Eat.</span> Try to eat brain foods like plenty of fruits and vegetables, and oily fish for their omega-3 fatty acids;
        <ul class="ml-6">
          <li>Smaller meals with snacks in between are recommended, because larger meals can lead to drowsiness and lower concentration;</li>
        </ul>
      </li>
      <li><span class="italic">Exercise.</span> Even just ten minutes here or there can help you stay focused and keep your mind working more efficiently.
        <ul class="ml-6">
          <li>Incorporate exercise into your day by exercising before or after study sessions, or during short breaks.</li>
          <li>Types of exercise: short walks, seat calisthenics, push-ups, etc.</li>
        </ul>
      </li>
      <li><span class="italic">Sleep.</span> 7-9 hours per night;</li>
    </ul>
    <p>These things can seem trivial, but research shows that they’re really important. Do you think changing some of your habits around these types of physical preparation could be helpful for you?</p><br>
    <p><span class="font-semibold">[First Name]</span>. Can I tell you something wild?</p>
    <p>Research shows that when you nurture a positive outlook about your learning you actually begin to learn and retain more than you would if you have a negative outlook. So just by being positive, you actually learn better!</p>
    <p>Let’s talk about some easy ways you can cultivate positivity.</p><br>
    <p class="font-semibold">Mental Preparation</p>
    <ul class="ml-6">
      <li>Use self-affirming language to set yourself up for success:
        <ul class="ml-6">
          <li>Speak in the present tense: “I am studying 3 hrs today” NOT “I will study three hours today.”</li>
          <li>Use words of encouragement: “I am proud of myself.”</li>
        </ul>
      </li>
      <li>Nurture positivity by spreading positivity.
        <ul class="ml-6">
          <li>Encourage others and cultivate relationships with people who encourage you.</li>
        </ul>
      </li>
      <li>Find an accountability partner
        <ul class="ml-6">
          <li>Someone who is reliable and consistent who you can study alongside.</li>
        </ul>
      </li>
    </ul>
    <p>Would you like to try a short exercise that you can do to help cultivate your positivity? (This can be useful for people who tend to feel negatively about their abilities.)</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="caller-application" value="yes" v-model="loadShortExercise" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Yes</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="no" v-model="loadShortExercise" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">No</label>
        </div>
      </div>
    </fieldset>
  </div>
  <hr>
  <div v-if="loadShortExercise === 'yes'" class="my-3">
    <p>I want you to think of a time where you surprised yourself by how much knowledge you had on a certain topic or subject. (This does not have to be an academic subject, but it could be.)</p>
    <p class="text-red-500">[Caller Response]</p><br>
    <p>How about a time when you used information from one class to do work in another class?</p>
    <p class="text-red-500">[Caller Response]</p><br>
    <p>Excellent. Let’s try a few more:</p>
    <p>Can you think of times when you:</p>
    <ul class="ml-6">
      <li>Persisted when you encountered setbacks</li>
      <li>Successfully completed a task or class through hard work, even if you felt you didn’t have a natural talent at it</li>
      <li>Learned from critiques</li>
      <li>Found someone who inspired you, and imitated their efforts.</li>
    </ul>
    <p>Great Job.</p><br>
    <p>Before you sit down to study, it can be helpful to run through a brief mental exercise like this just as a way to remind yourself of ways you’ve been awesome in the past. If you can bring that positive mindset into the study session, the research says you are more likely to benefit from the session.</p>
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p>To help make our discussion a bit more concrete, can you think of an assignment or a course that you are currently working on that you could be studying for? Preferably, this would be something that isn’t due immediately but that you know is on the horizon. For instance, maybe a midterm or final coming up in the next few weeks that you need to study for.</p><br>
    <p class="text-red-500">[Application]</p><br>
    <p>Great. So, as we discuss different study skills throughout the call we’ll use <span class="font-semibold">[APPLICATION]</span> as an example to apply these different strategies to. </p>
    <p>Make Sense?</p>
  </div>
  <hr>
  <div class="my-3">
    <p v-if="callerApplication === 'exam-prep'">First thing’s first, let’s remind ourselves of your study assets.</p>
    <p v-else>Before you even start studying, you should take note of your study assets. </p>
    <p>Study assets refer to the different resources available to you either directly through the course, or through the Department or University.</p>
    <p>I’ll read through a list of resources most courses and universities make available, and you can tell me if you have or if you can obtain access to each of them. I also encourage you to make your own notes about these course assets as we talk, particularly about those you don’t currently utilize so that you can check on them.</p><br>
    <p>Okay, some typical course assets would include:</p>
    <p class="pl-6 text-red-500">[Talk through each course asset and help caller brainstorm how they might better utilize each asset]</p>
    <p class="pl-6 text-red-500">[Check the course assets the Caller uses or thinks they can access]</p>
    <fieldset class="my-3">
      <div class="space-y-3">
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="note-taking" v-model="courseAssets" value="course-syllabus" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="note-taking" class="text-gray-900">Course Syllabus</label>
            <p><span class="font-semibold">What it is:</span> A document shared by your professor that usually includes information like course goals, meeting times, instructor office hours, course policies, and assignment overviews.</p>
            <p><span class="font-semibold">What to look for:</span></p>
            <ul class="ml-6">
              <li>Course calendar and assignment overviews
                <ul class="ml-6">
                  <li>Can inform you of important dates to take note of</li>
                </ul>
              </li>
              <li>Course goals and course overview sections
                <ul class="ml-6">
                  <li>Can help inform you about how your instructor is approaching their subject.</li>
                </ul>
              </li>
            </ul>
            <p><span class="font-semibold">Why this can help:</span></p>
            <ul class="ml-6">
              <li>Knowing the specific focus your professor is bringing to their course can help you anticipate the kinds of questions or discussions you might expect to have in that course and therefore help direct your attention during readings and study sessions.
                <ul class="ml-6">
                  <li>For instance, a course labeled “Western Philosophical Traditions” could encompass many potential topics. However, your professor’s overview might list the specific questions that the course will focus on, for instance: free will, the nature of reality, etc.</li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="review" v-model="courseAssets" value="instructor" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="review" class="text-gray-900">Instructor or TA office hours</label>
            <p>How they can help:</p>
            <ul class="ml-6">
              <li>can sometimes turn into informal help sessions</li>
              <li>can inform you on instructor’s though processes</li>
              <li>can inform you on added tips</li>
            </ul>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="reading" v-model="courseAssets" value="lecture-downloads" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="reading" class="text-gray-900">Lecture Downloads</label>
            <p>How they can help:</p>
            <ul class="ml-6">
              <li>Can be used to review content you missed or found difficult to comprehend the first time</li>
              <li>Can be used to jog your memory about new concepts</li>
            </ul>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="review-notes" v-model="courseAssets" value="friends" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="review-notes" class="text-gray-900">Friends who have taken the same class</label>
            <p>How they can help:</p>
            <ul class="ml-6">
              <li>Can inform you of Exam formats</li>
              <li>Can inform you of difficult topics</li>
            </ul>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="self-testing" v-model="courseAssets" value="study-sessions" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="self-testing" class="text-gray-900">Study Sessions</label>
            <ul class="ml-6">
              <li>TA Organized</li>
              <li>Peer Organized</li>
              <li>Organized by you
                <ul class="ml-6">
                  <li>How they can help:
                    <ul class="ml-6">
                      <li>Provides structure</li>
                      <li>Draws on the collective strengths and memories of the group</li>
                    </ul>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="mnemonics" v-model="courseAssets" value="help-center" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="mnemonics" class="text-gray-900">Help Centers</label>
            <ul class="ml-6">
              <li>Department (preferable)</li>
              <li>Other general University Tutoring or Support Centers:
                <ul class="ml-6">
                  <li>Writing Centers for help writing papers,</li>
                  <li>Speaking Centers for help delivering oral presentations</li>
                  <li>University Libraries for help accessing academic research
                    <ul class="ml-6">
                      <li>How they can help:
                        <ul class="ml-6">
                          <li>Provide targeted support from subject-area experts</li>
                          <li>Often familiar with university and departmental exam or test formats</li>
                        </ul>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="connections" v-model="courseAssets" value="course-readings" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="connections" class="text-gray-900">Course Readings</label>
            <ul class="ml-6">
              <li>Textbooks</li>
              <li>Articles/essays
                <ul class="ml-6">
                  <li>Expand on and enhance information covered in class</li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
        <p v-if="callerApplication === 'exam-prep'">Excellent. At the most basic level, any of these course assets that are available to you and you think might help, you should utilize. But that’s not why you called, so let’s talk more specifically on how you can prepare for your <span class="font-semibold">[APPLICATION]</span>.</p>
      </div>
    </fieldset>
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p>So, we’ve talked about some study assets that you can incorporate into your studying routine, now let’s talk more specifically about how you can get the most out of course lectures and class time.</p>
    <p>To begin with, Preparation is key here. </p>
    <p>There are <span class="font-semibold">two</span> things you can do to help make lectures and class time more productive for you.</p>
    <p><span class="font-semibold">First</span>, whenever possible, read assigned material beforehand.</p>
    <ul class="ml-6">
      <li>In humanities courses (like history, philosophy, and English), the readings will likely form the basis of course discussion and lectures. Which means without doing the reading, you will not be able to participate.</li>
      <li>In the sciences, social sciences, and other disciplines completing the readings will help prime your brain for the content your professor will review and help you focus on what is important during the lecture.In the sciences, social sciences, and other disciplines completing the readings will help prime your brain for the content your professor will review and help you focus on what is important during the lecture.</li>
    </ul>
    <p>And <span class="font-semibold">Second</span>, come up with at least three (3) questions about the concepts discussed in the readings that you can bring with you to class to get answered.</p>
    <p>That’s it: just do the reading, and brainstorm at least three questions you might ask about the material being covered.</p>
  </div>
  <hr>
  <div v-if="callerApplication === 'exam-prep'" class="my-3">
    <p>In which general subject category is the Caller’s <span class="font-semibold">[APPLICATION]</span>?</p>
    <fieldset class="my-3">
      <div class="space-y-5">
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="humanities-or-social" v-model="subjectCategory" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="humanities-or-social" class="font-medium text-gray-900">Humanities or Social Sciences</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="sciences-or-math" v-model="subjectCategory" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="sciences-or-math" class="font-medium text-gray-900">Sciences or Math</label>
          </div>
        </div>
        <div class="relative flex items-start">
          <div class="flex h-6 items-center">
            <input id="general" v-model="subjectCategory" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
          <div class="ml-3 text-sm leading-6">
            <label for="general" class="font-medium text-gray-900">General</label>
          </div>
        </div>
      </div>
    </fieldset>
  </div>
  <hr>
  <div class="my-3">
    <p v-if="callerApplication === 'exam-prep'">Real quick, let's review some of the science and best practices around studying, so you know why we’re doing what we’re about to do.</p>
    <p>First, Good study sessions let you exercise three main learning practices. </p>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="mt-6 flow-root">
        <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <table class="min-w-full divide-y divide-gray-300">
              <thead>
              <tr class="divide-x divide-gray-200">
                <th scope="col" class="py-3.5 pl-4 pr-4 text-left text-sm font-semibold text-gray-900 sm:pl-0">Learning Practice</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Definition</th>
              </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">Encoding</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">Which is any practice you use to try and get new information or new ideas to stick in your memory. </td>
              </tr>
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">Rehearsal</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">Or when you repeat information back to yourself. For instance, if you needed to memorize a list of words you might <br> repeat the list to yourself over and over. </td>
              </tr>
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">Retrieval</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">Or any practice that challenges you to bring information to mind from memory; that is, without the help of notes. </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <p>Based on what you’ve told me, you are practicing:</p>
    <p>[<span class="font-semibold">PS NOTE</span>] Review table below with Caller. Discuss what they are currently doing and what they could be doing better!</p>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="mt-6">
        <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle">
            <table class="min-w-full divide-y divide-gray-300">
              <thead>
              <tr class="divide-x divide-gray-200">
                <th scope="col" class="py-3.5 pl-4 pr-4 text-left text-sm font-semibold text-gray-900 sm:pl-0">Encoding</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Rehearsal</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Retrieval</th>
              </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 text-sm font-medium text-gray-900 sm:pl-0">
                  <fieldset class="my-3">
                    <div class="space-y-3">
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="encoding-note-taking" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="encoding-note-taking" class="font-medium text-gray-900">Note Taking (In Class)</label>
                        </div>
                      </div>
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="encoding-reading" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="encoding-reading" class="font-medium text-gray-900">Reading/Highlighting</label>
                        </div>
                      </div>
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="encoding-mnemonics" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="encoding-mnemonics" class="font-medium text-gray-900">Creating mnemonics</label>
                        </div>
                      </div>
                    </div>
                  </fieldset>
                </td>
                <td class="whitespace-nowrap pl-4 text-sm text-gray-500">
                  <fieldset class="my-3">
                    <div class="space-y-3">
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="rehearsal-review-lectures" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="rehearsal-review-lectures" class="font-medium text-gray-900">Reviewing/re-watching course <br> lectures or slide decks</label>
                        </div>
                      </div>
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="rehearsal-review-notes" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="rehearsal-review-notes" class="font-medium text-gray-900">Reviewing notes</label>
                        </div>
                      </div>
                    </div>
                  </fieldset>
                </td>
                <td class="whitespace-nowrap pl-4 text-sm text-gray-500">
                  <fieldset class="my-3">
                    <div class="space-y-3">
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="retrieval-testing" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="retrieval-testing" class="font-medium text-gray-900">Self-testing or pre-testing</label>
                        </div>
                      </div>
                      <div class="relative flex items-start">
                        <div class="flex h-6 items-center">
                          <input id="retrieval-connections" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                        </div>
                        <div class="ml-3 text-sm leading-6">
                          <label for="retrieval-connections" class="font-medium text-gray-900">Making connections between <br> different concepts or classes</label>
                        </div>
                      </div>
                    </div>
                  </fieldset>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <p class="text-red-500">[This table should load the selections from the Present Snapshot-Current Practices screen, indicating those practices the caller is currently doing (indicated by check marks) as well as those practices they could be doing (indicated by having no check).]</p><br>
    <div v-if="callerApplication === 'exam-prep'">
      <p>Second, study sessions should be <span class="font-semibold">short</span> but <span class="font-semibold">frequent</span>.</p>
      <p class="font-semibold">Duration - short</p>
      <p>Your ability to focus on and retain new information is strongest between X-XX minutes and starts to decline after about XX minutes. </p>
      <p>Of course, you can study for longer, but you’ll be less efficient at retaining additional information beyond XX minutes.</p><br>
      <p class="font-semibold">Frequency - high</p>
      <p>Frequency helps strengthen what cognitive psychologists call the “recency effect.” Think of the recency effect as: the less time between study sessions, the more successful you’re likely to be at storing the information in your memory.</p>
    </div>
    <div v-if="callerApplication === 'general-study'">
      <p>Besides these learning practices, you should also think about your study sessions in terms of their duration and frequency.</p>
      <p>That’s what we’ll talk briefly about next.</p>
    </div>
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p>Ideally, your study sessions will be short but frequent.</p><br>
    <p class="font-semibold">Duration - short</p>
    <p>Your ability to focus on and retain new information is strongest between X-XX minutes and starts to decline after about XX minutes.</p>
    <p>Of course, you can study for longer, but you’ll be less efficient at retaining additional information beyond XX minutes.</p><br>
    <p class="font-semibold">Frequency - high</p>
    <p>Frequency helps strengthen what cognitive psychologists call the “recency effect.” Think of the recency effect as: the less time between study sessions, the more successful you’re likely to be at storing the information in your memory.</p>
  </div>
  <hr>
  <div v-if="callerApplication === 'exam-prep'" class="my-3">
    <p>For the rest of the call, we’re just going to put together a smart study schedule so that you can better prepare for your upcoming <span class="font-semibold">[APPLICATION]</span>.</p>
    <p>The basic formula for determining how much time you should be putting in studying for a class is to multiply the number of course credit hours by 2-4.</p><br>
    <p>So, an instructor would assume that for a 3 credit class, their students are spending anywhere from 6 to 12 hours on coursework per week. Realistically, that’s probably on the high end of what people actually do, but it does at least give you a number to aim at.</p><br>
    <p>You said your <span class="font-semibold">[APPLICATION]</span> is in <span class="font-semibold">[TIME CONSTRAINT]</span>, is that right?</p>
    <p>Great. Between now and then, how many total hours can you commit to studying for <span class="font-semibold">[APPLICATION]</span>?</p>
    <input type="number" v-model="hours" placeholder="Enter Hours" class="w-36 text-sm"/>
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p>Of course, it’s possible to be practicing all of these different techniques like exercising encoding processes, planning short but frequent study sessions and still not be getting the most out of your study regimen.</p>
    <p>Something that can help is to establish a repeatable “study flow” where you cycle through three basic kinds of brief study sessions:</p>
    <ol class="ml-6">
      <li>Studying your notes or the textbook in order to make information memorable (which aids encoding)</li>
      <li>Re-writing your notes as flashcards (which aids rehearsal)</li>
      <li>And verbally expressing what you know (which aids retrieval)</li>
    </ol>
    <br>
    <p>Next, we’ll talk about some different ways to incorporate this flow into your own study habits.</p>
  </div>
  <hr>
  <div v-if="callerApplication === 'exam-prep'" class="my-3">
    <p>What material do you need to study for the <span class="font-semibold">[APPLICATION]</span>? Did your instructor give any hints about what might be on the <span>[APPLICATION]</span>?</p>
    <textarea rows="3" placeholder="Agent Notes: Tasks/Activities" class="w-3/4 my-3"></textarea>
    <p>Excellent</p><br>
    <p>Let’s start there. You said you have <span>{{ hours }}</span> hours available to study, right?</p>
    <p>We’ll treat each hour as an individual study session. </p>
    <p>I want you to get something to write with.</p>
    <p>{{ 'Draw a table with six columns and ' + Number(hours + 1) + ' rows.' }}</p>
    <p>Label the first row of the first <span class="font-semibold">three</span> columns the following: <span class="font-semibold">Hour Study	Source</span></p>
    <p>In the <span class="font-semibold">Hour</span> column, number the rows 1 through <span class="font-semibold">{{ hours }}</span>.</p>
    <p>Next, in the <span class="font-semibold">Study</span> column, I want you to write down which topics you’ll focus on for each hour-long session.</p>
    <p>[<span class="font-semibold">PS NOTE</span> Walk Caller through filling out the following table. The “Source” column indicates where the Caller can locate information relevant to the topic, for instance in a course textbook, their notes, a recorded course lecture, etc.]</p>
    <img src="/images/study-skill-table-1.png" class="w-1/2" alt="table-1">
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p>Remembering that the ideal study sessions are short but frequent, we’ll talk through some different ways you can structure study sessions so that they work for you.</p>
    <p>But all of the different kinds of study sessions we’ll talk about will use that repeatable flow we just talked about:</p>
    <ol class="ml-6">
      <li>encoding, or absorbing information. </li>
      <li>Rehearsing that information somehow, for instance by using flashcards. </li>
      <li>And retrieving the information you’ve learned from your memory through some form of verbal or written expression.</li>
    </ol>
    <br>
    <p>As I talk about the different study sessions, I’m also going to order them in terms of most basic to most complex. </p>
    <p>More basic study sessions are really about memorizing the <span class="font-semibold">definitions</span> of key terms. This helps when you’re just learning a new subject or you’re encountering an idea that you’re completely unfamiliar with. </p>
    <p>As you become familiar with a subject, you’ll move on from worrying about definitions to wanting to focus more on understanding the <span class="font-semibold">concepts</span> behind those definitions.</p>
    <p>Then, you start focusing on how to <span class="font-semibold">apply</span> those concepts to real world situations.</p>
    <p>Once you have a handle on concepts and applications, then studying is really about finding <span class="font-semibold">patterns</span> between different concepts in the subject area, or even on recognizing patterns across subject areas so you can see how different domains of knowledge connect.</p><br>
    <p>Does that make sense?</p>
    <p>We’ll talk about how to set up study sessions for each of these kinds of learning.</p><br>
    <p>[<span class="font-semibold">Note to PS</span> Talk through with the caller how to incorporate different study methods into their study routine. It may not be necessary to cover the entire table, depending on how well the Caller knows their subject area. Focus on providing help depending on where the caller is at.]</p>
    <table class="border overflow-x-auto mt-3">
      <thead>
        <tr class="border">
          <th class="p-2 border">Study Session <br> Category</th>
          <th class="p-2 border">Significance</th>
          <th class="p-2 border">How To Incorporate (General)</th>
          <th class="p-2 border">How To Incorporate (Math Specific)</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border">
          <td class="p-2 border">Definitions</td>
          <td class="p-2 border">
            <p>Allows for communication.</p><br>
            <p>Allow you to explain <br> concepts to other people.</p><br>
            <p>Allow you to be more specific.</p><br>
            <p>Provide rules (Math/Science).</p><br>
            <p>Provide context.</p>
          </td>
          <td class="p-2 border">
            <p><span class="font-semibold">Flashcards</span> (encoding and rehearsal) <br>Focus on the relationship between the word & definition.</p><br>
            <p>Focus on groups of words that “go together”.</p><br>
            <p><span class="font-semibold">Communicate Verbally</span> (rehearsal and retrieval) <br>Create a sentence with the word that will provide clarity of the definition.</p><br>
            <p>Use word association- say (or have someone else say) a vocabulary word out loud and name other words or phrases that come to mind when you say them.</p>
          </td>
          <td class="p-2 border">
            <p><span class="font-semibold">Flashcards</span> (encoding and rehearsal) <br>Know important theorems/formulas.</p><br>
            <p>Focus on the relationship between theorems/formulas.</p><br>
            <p>Focus on groups of words that “go together”.</p><br>
            <p><span class="font-semibold">Communicate Verbally</span> (rehearsal and retrieval) <br>Create a sentence with the word that will provide clarity of the definition.</p><br>
            <p>Use word association- say (or have someone else) a vocabulary word out loud and name other words or phrases that come to mind when you say them.</p>
          </td>
        </tr>
        <tr class="border">
          <td class="p-2 border">Concepts</td>
          <td class="p-2 border">
            <p>Allow you to test or verify ideas.</p><br>
            <p>Allow compare and contrast concepts.</p><br>
            <p>Allow for refinement.</p>
          </td>
          <td class="p-2 border">
            <p><span class="font-semibold">Flashcards</span> (encoding and rehearsal) <br>Focus on the relationship between the word & definition.</p><br>
            <p>Focus on validity or strength of the concept.</p><br>
            <p>Focus on validity or weaknesses of the concept.</p><br>
            <p>Focus on the contribution of the person or concept.</p><br>
            <p><span class="font-semibold">Communicate Verbally</span> (rehearsal and retrieval) <br>What question or problem is this concept trying to address? Connect the problem with the concept (proposed solution).</p><br>
            <p>Compare & contrast concepts.</p>
          </td>
          <td class="p-2 border">
            <p><span class="font-semibold">Flashcards</span> (encoding and rehearsal) <br>Identify Objectives (course/textbook)</p><br>
            <p>Focus on the relationship between the questions & appropriate solutions.</p><br>
            <p>Focus on the contribution of the theorem/formula/method.</p><br>
            <p>Are there other ways to solve this problem?</p><br>
            <p><span class="font-semibold">Communicate Verbally</span> (rehearsal and retrieval) <br>What question or problem is this concept trying to address? Connect the problem with the concept (proposed solution).</p><br>
            <p>Compare & contrast similar concepts.</p>
          </td>
        </tr>
        <tr class="border">
          <td class="p-2 border">Application of Concepts</td>
          <td class="p-2 border">
            <p>Provide context for the concepts.</p><br>
            <p>Allow for repetition under varying conditions.</p><br>
            <p>Allow for modifications or exceptions to present themselves.</p>
          </td>
          <td class="p-2 border">
            <p><span class="font-semibold">Flashcards</span> (encoding and rehearsal) <br>Create scenarios or problems to be addressed.</p><br>
            <p>Under what conditions should a particular theorem/formula be applied?</p><br>
            <p>Under what conditions should a particular concept NOT be applied? And why?</p><br>
            <p>Which concept would be a better fit in this situation?</p><br>
            <p><span class="font-semibold">Communicate Verbally</span> (rehearsal and retrieval) <br>Share what you know with an imaginary audience.</p><br>
            <p>Share what you know with a friend or study partner & ask for feedback.</p>
          </td>
          <td class="p-2 border">
            <p><span class="font-semibold">Flashcards</span> (encoding and rehearsal) <br>Practice-practice-practice-practice (Repetition is Key!)</p><br>
            <p>Under what conditions should a particular theorem/formula/method be applied? And why?</p><br>
            <p>Under what conditions should a particular theorem/formula/method NOT be applied? And why?</p><br>
            <p>Are there other ways to solve this problem?</p><br>
            <p><span class="font-semibold">Communicate Verbally</span> (rehearsal and retrieval) <br>Share what you know with an imaginary audience.</p><br>
            <p>Share what you know with a friend or study partner & ask for feedback.</p>
          </td>
        </tr>
        <tr class="border">
          <td class="p-2 border">Patterns</td>
          <td class="p-2 border">
            <p>Allow the transfer of knowledge across subjects.</p><br>
            <p>Encourages new ideas.</p><br>
            <p>Encourages a global perspective and broader appreciation.</p>
          </td>
          <td class="p-2 border"></td>
          <td class="p-2 border"></td>
        </tr>
      </tbody>
    </table>
  </div>
  <hr>
  <div v-if="callerApplication === 'exam-prep'" class="my-3">
    <p>Because study sessions should be short but frequent - but it is sometimes necessary to stack multiple study sessions one after the other - we’re going to make a rule for these study sessions. </p>
    <p>That rule is: you can only study for 45 minutes every hour. </p>
    <p>The other fifteen minutes you’ll use as a mini break or reward session.</p>
    <p>Label the fourth column of your table <span class="font-semibold">Break</span>. Now, let’s identify a reward or an activity that you can do as a reward and to help stay motivated.</p>
    <p>[<span class="font-semibold">PS NOTE</span> Add Caller-identified reward to the note field in the Break column.]</p>
    <img src="/images/study-skill-table-2.png" class="w-1/2" alt="table-2">
    <p>Now,  if you want to block off a two or three hour chunk of your afternoon for studying, you can. These little micro-breaks help you recharge and reset your focus.</p>
  </div>
  <hr>
  <div v-if="callerApplication === 'exam-prep'" class="my-3">
    <p>Finally, we want to make sure we’re incorporating those three learning practices we discussed earlier - encoding (or making information memorable), rehearsing (or repeating that information with cues), and retrieving (or using your memory to access that information without external cues).</p>
    <p>[<span class="font-semibold">PS NOTE</span> Fill in the Category and Practice columns using the drop down menus. Not all Callers will need all Category types.]</p><br>
    <p>[<span class="font-semibold">EXPLANATORY NOTE</span> The Category selection determines the learning goal, on an ascending scale from simplest (learning definitions) to most complex (applying concepts and making connections between concepts). The Practice column outlines three specific study sessions, one for each encoding, rehearsing, and retrieving practice. Ideally, a study schedule will include all three practice types within each applicable Category type.] </p>
    <img src="/images/study-skill-table-3.png" class="w-4/5" alt="table-3">
    <p>[<span class="font-semibold">PS NOTE</span> Review the full smart study schedule with the Caller.] </p>
    <p>Do you have any questions?</p><br>
    <p class="text-red-500">The “Category” drop down is dependent on one factor: whether the PS has selected “Humanities” (or “General”) or “Science and Math” on the earlier Screen Pop Up. Below I outline the menu options beginning with the Humanities/General option and next moving on to the Sciences and Math option.</p>
    <img src="/images/study-skill-table-4.png" class="w-1/5" alt="table-4">
    <p class="text-red-500">The “Practice” drop down options are then dependent on the “Category” choice. Note that Practice options are different for Humanities/General and Sciences and Math. Below I outline the menu options in the Practices menu, beginning with the Humanities/General options and next moving on to the Sciences and Math options.</p><br>
    <p class="text-red-500">Humanities/General</p>
    <table class="border">
      <thead>
        <tr class="border">
          <th class="p-2">Practice (Definition)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="border p-2">(Encode) Create key term flashcards with term and definition. Next, organize flashcards into groups of words that "go together."</td>
        </tr>
        <tr>
          <td class="border p-2">(Rehearse) Create a sentence with the key term in it that will provide clarity of the definition.</td>
        </tr>
        <tr>
          <td class="border p-2">(Retrieve) Practice word association. Say (or have someone else say) a vocabulary word out loud and name other words that come to mind. Explain how they are relevant or related.</td>
        </tr>
      </tbody>
    </table>
    <table class="border mt-6">
      <thead>
      <tr class="border">
        <th class="p-2">Practice (Concepts)</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="border p-2">(Encode) Using key term flashcards: Review persons or events from the class who are associated with each term. Next, review the validity (strengths and weaknesses) of the concepts underlying each term. Finally, review the overall contribution of the person or concept to the subject area as a whole.</td>
      </tr>
      <tr>
        <td class="border p-2">(Rehearse) Using key term flashcards, for each concept or term ask: What question or problem is this concept trying to address? How does it attempt to address this problem?</td>
      </tr>
      <tr>
        <td class="border p-2">(Retrieve) Out loud, or in your notebook, compare and contrast concepts.</td>
      </tr>
      </tbody>
    </table>
    <table class="border mt-6">
      <thead>
      <tr class="border">
        <th class="p-2">Practice (Applying Concepts)</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="border p-2">(Encode) For each key term flashcard, ask, “Under what conditions might this concept, formula, or theorem be applied? Under what conditions should it NOT be applied?”</td>
      </tr>
      <tr>
        <td class="border p-2">(Rehearse) Create various scenarios or problems to be addressed and then ask yourself, “Which concept would be a better fit for this situation?”</td>
      </tr>
      <tr>
        <td class="border p-2">(Retrieve) Share what you know with a friend, study partner, or imaginary audience.</td>
      </tr>
      </tbody>
    </table>
    <table class="border mt-6">
      <thead>
      <tr class="border">
        <th class="p-2">Practice (Making Connections)</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="border p-2">Consider: How does what you are learning connect with other subjects or concepts you are familiar with or are studying in other courses? How does the term or concept help explain human social behavior? Can you think of other things you have learned about that support or challenge this concept?</td>
      </tr>
      </tbody>
    </table>
    <p class="text-red-500 mt-6">Sciences and Math</p>
    <table class="border">
      <thead>
      <tr class="border">
        <th class="p-2">Practice (Definitions)</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="border p-2">(Encode) Create a set of flashcards for important theorems, terms, and formulas, with the formula or term on one side and the explanation on the other side. Practice.</td>
      </tr>
      <tr>
        <td class="border p-2">(Rehearse) Try organizing flashcards in various ways that help you see terms/theorems that “go together” or help you focus on relationships between theorems and formulas.</td>
      </tr>
      <tr>
        <td class="border p-2">(Retrieve) Practice word association. Say (or have someone else say) a term or formula out loud. Provide a definition or formula associated with that term and name other words that come to mind. Explain how they are relevant or related.</td>
      </tr>
      </tbody>
    </table>
    <table class="border mt-6">
      <thead>
      <tr class="border">
        <th class="p-2">Practice (Concepts)</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="border p-2">(Encode) Using key term flashcards, identify the kinds of problems you might use the term, theorem, or formula to address.</td>
      </tr>
      <tr>
        <td class="border p-2">(Rehearse) Work on practice problems from the course textbook or from online.</td>
      </tr>
      <tr>
        <td class="border p-2">(Retrieve) Out loud, or in a notebook, discuss each formula, theorem, or term you are studying by answering the question: “What question or problem is this formula/theorem/term trying to address?”</td>
      </tr>
      </tbody>
    </table>
    <table class="border mt-6">
      <thead>
      <tr class="border">
        <th class="p-2">Practice (Applying Concepts)</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="border p-2">(Encode) For each key term flashcard, ask, “Under what conditions might this concept, formula, or theorem be applied? Under what conditions should it NOT be applied?”</td>
      </tr>
      <tr>
        <td class="border p-2">(Rehearse) Create various scenarios or problems to be addressed and then ask yourself, “Which concept would be a better fit for this situation?” Work on practice problems from the course textbook or from online.</td>
      </tr>
      <tr>
        <td class="border p-2">(Retrieve) Share what you know about each term or concept with a friend, study partner, or imaginary audience.</td>
      </tr>
      </tbody>
    </table>
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p>If you’ve been diligent about implementing the study sessions described earlier, when it comes to exam prep sessions you’ll primarily be focused on practicing the speed and accuracy of that retrieval mechanism you’ve been working on.</p>
    <p>To do this, beginning a couple days before your exam, you should implement brief study sessions where you:</p>
    <ul class="ml-6">
      <li>Review your class notes and flashcards</li>
      <li>Review Reading Materials</li>
    </ul>
    <br>
    <p>In addition, you should be more conscious of taking advantage of attending:</p>
    <ul class="ml-6">
      <li>Help sessions</li>
      <li>Instructor office hours</li>
      <li>Group sessions</li>
    </ul>
    <br>
    <p>And once again, remember that brief, frequent study sessions are better than one long cram session.</p><br>
    <p class="font-semibold">Pro Tip: Be the Expert!</p>
    <ol class="ml-6">
      <li>Ask yourself, “If I were to teach this topic/class how would I present it to my class?”</li>
      <li>Stand in front of a mirror and teach what you know as if you were the instructor</li>
    </ol>
  </div>
  <hr>
  <div v-if="callerApplication === 'exam-prep'" class="my-3">
    <p>Above all, remember your goals and keep those in the forefront of your mind!</p><br>
    <p class="italic">[Review Caller Goals from the top of the call, saved in Caller Notes]</p><br>
    <textarea rows="3" placeholder="Agent Notes: Caller Notes" class="w-3/4 my-3"></textarea>
    <p>To end, I’ll leave you with two extra, quick study tips.</p><br>
    <p>Pro Tip 1: Make memorable connections</p>
    <ul class="ml-6">
      <li>If you are a highly visual person you might read from a textbook and remember a picture of a cell that goes with the description of a skin cell. In this case, making a connection with the material you read, and the picture can help you remember the material. The more relevance it has to you, the easier the material will be to remember.</li>
    </ul>
    <p>Pro Tip 2: Be the Expert!</p>
    <ul class="ml-6">
      <li>Ask yourself, “If I were to teach this topic/class how would I present it to my class?”</li>
      <li>Stand in front of a mirror and teach what you know as if you were the instructor</li>
    </ul>
    <br>
    <p>Thanks for calling Dragonfly. Again, my name is <span class="font-semibold">[PS Name]</span>. Please take a moment or two to fill out the survey at the end of the call to let me know how I did today.</p><br>
    <p>Have a wonderful day!</p>
  </div>
  <hr>
  <div v-if="callerApplication === 'general-study'" class="my-3">
    <p><span class="font-semibold">[FIRST NAME]</span>, when you think about studying, remember all of the resources you have at your disposal.</p><br>
    <p class="italic">Study Resources</p><br>
    <textarea rows="3" placeholder="Agent Notes: Study Resources" class="w-3/4 my-3"></textarea>
    <p>And remember that successful study sessions are made possible by how well you listen and take notes in class. Using a standard method of note taking - like the Cornell Method - can keep your notes organized and clear.</p><br>
    <p>Also remember that how you study is important. Ideally, you want to incorporate practices that work with how your brain learns.</p><br>
    <p>Above all, remember your goals and keep those in the forefront of your mind!</p><br>
    <p class="italic">[Review Caller Goals from the top of the call, saved in Caller Notes]</p><br>
    <textarea rows="3" placeholder="Agent Notes: Caller Notes" class="w-3/4 my-3"></textarea>
    <br>
    <p>Thanks for calling Dragonfly. Again, my name is <span class="font-semibold">[PS Name]</span>. Please take a moment or two to fill out the survey at the end of the call to let me know how I did today.</p><br>
    <p>Have a wonderful day!</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const callerApplication = ref(null)
const currentPractices = ref([])
const noteTakingTypes = ref([])
const reviewTime = ref([])
const otherPractice = ref(null)
const studyFrequency = ref(null)
const averageHour = ref(0)
const averageMinute = ref(0)
const loadShortExercise = ref(null)
const courseAssets = ref([])
const subjectCategory = ref([])
const hours = ref(0)

</script>