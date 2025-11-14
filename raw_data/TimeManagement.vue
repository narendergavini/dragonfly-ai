<template>
  <div class="mb-3">
    <p class="text-xl font-semibold mb-3">Call Application, Goals and Time Constraints</p>
    <p>Why don't you start off by telling me a little bit about why you are calling today.</p>
    <p>Optional: Feel free to share any details you think might be relevant to our conversation. For instance:</p>
    <ul class="ml-5">
      <li>Is there a particular assignment or exam you're procrastinating on that you need to complete?</li>
      <li>Or, are you calling for more general tips on combating procrastination?</li>
    </ul>
    <br>
    <p class="font-semibold">Caller Application (Caller Response)</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="caller-application" value="sa" v-model="callerApplication" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Specific Application</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="gtm" v-model="callerApplication" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">General Time Management</label>
        </div>
      </div>
    </fieldset>
    <br>
    <p>Are you working with any time constraints, like upcoming deadlines?</p>
    <ul class="ml-5">
      <li>Less than 24 hours [Divers to SMS solutions]</li>
      <li>Time Constraint</li>
      <li>None</li>
    </ul>
    <br>
    <p>What would you like to accomplish immediately after this call. That is, what do you hope our session will prepare you to do?</p>
    <p>If specific application: How will <span class="font-bold">[SPECIFIC APPLICATION]</span> benefit your future?</p>
    <br>
    <p class="font-bold">Caller Goals for this Session</p>
    <textarea rows="3" placeholder="Agent Notes: Caller Goals" class="w-3/4 my-3"></textarea>
    <p>How do you think better time management skills specifically will help you achieve your goals?</p><br>
    <p class="italic">Confirm and clarify above selections and call goals before continuing.</p>
  </div>
  <hr>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Individual Variables 1</p>
    <p>Now just a few more quick questions to help us put together an action plan that can work for you. There are no wrong answers here.</p><br>
    <p>My first question is about your comfort zone when it comes to setting and following through on your goals generally.</p><br>
    <p>Would you say you are more <span class="italic">flexible</span> or more <span>inflexible</span> when it comes to setting goals and sticking to them? You might think here of "flexible" as tending to align more with a "creative" or "spontaneous" personality, and "inflexible" as aligning more with "logical" or "rule-oriented" personalities.</p><br>
    <fieldset class="mt-3">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="subscript-type" value="emotional" v-model="loadSubscript" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Flexible/Creative/Spontaneous [Loads Emotional Scripting]</label>
        </div>
        <div class="flex items-center">
          <input name="subscript-type" value="cognitive" v-model="loadSubscript" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Inflexible/Logical/Rule Oriented [Loads Cognitive Scripting]</label>
        </div>
      </div>
    </fieldset>
  </div>
  <hr>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Individual Variables 2</p>
    <p>The scientific literature distinguishes between two kinds of challenges we can face when it comes to time management. </p><br>
    <p>We can struggle with the <span class="font-bold">organizational</span> challenges of time management – how do we implement clear processes for managing our time, how do we accurately plan ahead for specific tasks, etc.</p><br>
    <p>Or can struggle with the <span class="font-bold">motivational</span> challenges of time management – how do I motivate myself to do the work I need to do right now; how do I better concentrate on the tasks I need to accomplish right now.</p><br>
    <p>If you were to take a moment and think about it, would you say your time management issues are related more to organizational challenges or challenges with motivation or concentration?</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
        <div class="flex items-center">
          <input name="challenge-type" value="organizational" v-model="challengeType" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Organization</label>
        </div>
        <div class="flex items-center">
          <input name="challenge-type" value="motivational" v-model="challengeType" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Motivation/Concentration</label>
        </div>
      </div>
    </fieldset>
  </div>
  <hr>
  <div class="my-3" v-if="challengeType === 'motivational'">
    <p class="text-xl font-semibold mb-3">Motivation Track</p>
    <p>Hey, I get it. Sometimes even if we know a task is important, it can be hard to find the motivation to start it or see it through to the finish.</p>
    <p>Let me ask you this: How do you define motivation?</p><br>
    <p class="font-bold">Motivation</p>
    <textarea rows="3" placeholder="Agent Notes: Motivation" class="w-3/4 my-3"></textarea>
    <p>And why is it you feel you need to improve motivation?</p><br>
    <p class="font-bold">Improvement Goals</p>
    <textarea rows="3" placeholder="Agent Notes: Improvement Goals" class="w-3/4 my-3"></textarea>
    <p>Research tells us that there are three major aspects of motivation we can work on:</p>
    <ol class="ml-5">
      <li>Practicing Control</li>
      <li>Increasing Curiosity, and</li>
      <li>Managing Challenge</li>
    </ol><br>
    <p>We’re going to walk through these one by one.</p>
    <p>But first, how are you feeling so far? Any questions?</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'organizational'">
    <p class="text-xl font-semibold mb-3">Organization Track</p>
    <p>Great. So this is always where we want to start: by recognizing the importance of any given task to your future goals or to your overall values.</p><br>
    <p>Time Management is as much about finding time to complete everything you need to complete as it is about recognizing which tasks are the most important. It won’t always be possible to complete everything you have to do, or to give everything in your life the amount of attention and time you would like to.</p><br>
    <p>Since we’re focusing more on the organizational side of time management, we’re going to focus on building some tools to help you:</p>
    <ol class="ml-5">
      <li>Priority Tasks</li>
      <li>Subdivide Tasks into smaller sub-tasks</li>
      <li>More successfully estimate how much time and effort a given task requires, and</li>
      <li>Using those estimates to help create a schedule.</li>
    </ol><br>
    <p>How are you feeling? Any questions so far?</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'organizational'">
    <p class="text-xl font-semibold mb-3">Define Application</p>
    <p>To help make our discussion a bit more concrete, can you think of an assignment or a course that you are perhaps struggling to find time to work on? Preferably, this would be something that isn’t due immediately. For instance, maybe there’s a midterm or final coming up in the next few weeks that you need to find time to work on, or maybe there’s a class that you’re taking or a responsibility you’ve been putting off that you need to start dedicating more time toward.</p><br>
    <p class="text-gray-700 italic">Caller Response: APPLICATION</p><br>
    <p>Great. So, throughout the call we’ll use <span class="font-bold">Application</span> as an example to apply some of the different time management strategies we will be talking about to.</p>
    <p>Make sense?</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="loadSubscript === 'cognitive'">
    <p class="text-xl font-semibold mb-3">Cognitive Script</p>
    <p v-if="callerApplication === 'sa'">Let’s start by setting some intentions around your goals. By setting intentions, you’re clarifying for yourself why working on <span class="font-bold">[SPECIFIC APPLICATION]</span> matters to you, and for people like you who are very logical, that can help you stay focused.</p>
    <p v-else>Let’s start by setting some intentions around your goals. By setting intentions, you’re clarifying for yourself why having stronger time management skills matters to you, and for people like you who are very logical, that can help you stay focused.</p>
    <br>
    <p v-if="callerApplication === 'sa'">To do this, I want you to think about how working on <span class="font-bold">[SPECIFIC APPLICATION]</span> will benefit you.</p>
    <p v-else>To do this, I want you to think about your goal for time management in terms of how <span class="font-bold">better time management</span> will <span class="font-bold">benefit</span> you.</p>
    <br>
    <p>But:</p>
    <ul class="ml-5" v-if="callerApplication === 'sa'">
      <li> I want you to think beyond the short term. Instead, try to identify a long-term benefit success might provide you.
        <ul class="ml-5">
          <li>Something like, “The skills or knowledge I will gain from this will make me more attractive to potential employers.”</li>
          <li>OR, “If I do well on this, I will know a little bit more about how the world works, which is important to me.”</li>
        </ul>
      </li>
      <li>What matters is that it provides meaning to you and your long-term goals.</li>
      <li>But be specific: what skill or what knowledge specifically will you take away from this experience (class or assignment)?</li>
    </ul>
    <ul class="ml-5" v-else>
      <li>I want you to think beyond the short term. Instead, try to identify a long-term benefit that better time management skills will provide for you. It can help to think of these benefits in relation to your long term goals.</li>
      <li>What matters is that it provides meaning to you and your long-term goals.</li>
    </ul>
    <br>
    <p v-if="callerApplication === 'sa'">Okay, your turn. How will doing your best on <span class="font-bold">[SPECIFIC APPLICATION]</span> benefit you or provide long-term value to your life?</p>
    <p v-else>Okay, your turn. What are some long-term values or benefits you think better time management skills will provide your life?</p>
    <br>
    <p class="font-bold">Caller Identified Benefits/Values</p>
    <textarea rows="3" placeholder="Agent Notes: Caller Identified Benefits/Values" class="w-3/4 my-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="loadSubscript === 'emotional'">
    <p class="text-xl font-semibold mb-3">Emotional Script 1</p>
    <p><span class="font-bold">[CALLER FIRST NAME]</span>, a lot of times, when we struggle with time management, it has a lot to do with how we feel about a looming task. Perhaps we don’t feel it’s important. Or perhaps we’re assigning too much importance to it.</p>
    <p>In either case, these are negative feelings. And these feelings make us more likely to either put off the task, avoid it altogether, or allot too little (or too much) time to it.</p><br>
    <p>Now, the relationship we have with our emotions can be complicated, and this can be especially true for people like you who are a bit more creative and spontaneous. But it can be helpful to address and reframe these negative emotions.</p><br>
    <p>I’m going to walk you through two really simple mental exercises you can do to start reframing these negative emotions so you can gain some emotional perspective when it comes to the tasks you’re working on.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="loadSubscript === 'emotional'">
    <p class="text-xl font-semibold mb-3">Emotional Script 2</p>
    <p v-if="callerApplication === 'sa'">The first exercise is all about finding value in what you’re doing. We’ll use <span class="font-bold">[SPECIFIC APPLICATION]</span> as an example to work with.</p>
    <p v-else>For our first exercise, I want you to focus on finding value in what you are doing.</p>
    <p>On a scale from 1 to 10, with ten being extremely important and 1 being not important at all, how important do you feel <span class="font-bold">[APPLICATION]</span> is to you and your future?</p><br>
    <input type="number" v-model="scale" class="block w-24 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Scale" />
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="loadSubscript === 'emotional' && scale > 0 && scale < 7">
    <p class="text-xl font-semibold mb-3">Emotional Script 3.A</p>
    <p>We tend to distance ourselves emotionally and cognitively from things we don’t find interesting or rewarding, and this distancing can make us lose motivation. One thing you can do, then, to help with some motivation is try to find some personal value in the task. </p>
    <p v-if="callerApplication === 'sa'">Can you think of some ways you could view <span class="font-bold">[SPECIFIC APPLICATION]</span> that might help you revalue it?</p>
    <p v-else>Can you think of some ways you could view certain tasks or assignments that might help you revalue it?</p>
    <br>
    <p class="text-gray-700 italic">Follow-up question to press Caller, if needed</p>
    <p>Is there maybe some value to you in the assignment that you’re not considering?</p><br>
    <p class="text-gray-700 italic">If Caller still struggles to identify value</p>
    <p>Sometimes this exercise can be fairly straightforward, and sometimes it requires a little bit of creativity to do. Let’s try a short exercise. [Load “Identifying Transferable Skills”]</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="load-exercise" value="true" v-model="loadExercise" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Yes [Load Exercise]</label>
        </div>
        <div class="flex items-center">
          <input name="load-exercise" value="false" v-model="loadExercise" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">No [Move On]</label>
        </div>
      </div>
    </fieldset>
    <div v-if="loadExercise === 'false'">
      <br>
      <p class="font-bold">Caller Identified Benefits/Values</p>
      <textarea rows="3" placeholder="Agent Notes: Caller Identified Benefits/Values" class="w-3/4 my-3"></textarea>
      <p v-if="callerApplication === 'sa'">Does seeing some value in the <span class="font-bold">[SPECIFIC APPLICATION]</span> increase how important you feel the assignment is on that scale from one to ten, with ten being extremely important and one being not important at all?</p>
      <p v-else>Does seeing some value in certain tasks or assignments increase how important you feel the assignment is on that scale from one to ten, with ten being extremely important and one being not important at all?</p>
    </div>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="loadExercise === 'true'">
    <p class="text-xl font-semibold mb-3">Identifying Transferable Skills</p>
    <p v-if="callerApplication === 'sa'">Ok. “Value” is a pretty vague concept. Let’s think about this in a more concrete way. Can you think of some useful transferable skills you are developing when you work on <span class="font-bold">[SPECIFIC APPLICATION]</span>? Skills that can benefit you later, when you’re working on tasks that are valuable to you?</p>
    <p>Ok. “Value” is a pretty vague concept. Let’s think about this in a more concrete way. Can you think of some useful transferable skills you are developing while you work on these seemingly unrelated tasks? Skills that can benefit you later, when you’re working on tasks that are valuable to you? </p>
    <br>
    <p>For instance, a biology major may not immediately see the value of an essay that they have to complete for an English class. But if you think about the assignment as a chance to practice specific skills, like clear communication or critical or creative thinking which a biologist would need to communicate with the public or design new research programs, then it’s much easier to see how those skills would be valuable for our biology major.</p><br>
    <p v-if="callerApplication === 'sa'">So, what are some transferable skills you’re developing or practicing by working on <span class="font-bold">[SPECIFIC APPLICATION]</span>?</p>
    <p>So, what are some transferable skills you’re developing or practicing by working on some of your current assignments?</p>
    <p class="text-gray-700 italic">Encourage a response by caller, make suggestions, and review skill examples as needed</p><br>
    <p class="font-bold">Possible Skills</p>
    <ul class="ml-5">
      <li>Decision-Making</li>
      <li>Collaboration</li>
      <li>Integrity</li>
      <li>Leadership</li>
      <li>Multi-tasking</li>
      <li>Communication</li>
      <li>Management</li>
      <li>Teamwork</li>
      <li>Problem-Solving</li>
      <li>Professionalism</li>
      <li>Initiative</li>
      <li>Empathy</li>
    </ul>
    <br>
    <p class="font-bold">Caller Identified Values</p>
    <textarea rows="3" placeholder="Agent Notes: Identified Values" class="w-3/4 mt-3"></textarea>
    <p v-if="callerApplication === 'sa'">Does seeing some value in the <span class="font-bold">[SPECIFIC APPLICATION]</span> increase how important you feel the assignment is on that scale from one to ten? </p>
    <p v-else>Does seeing some value in the things you’re working on increase how important you feel they are on that scale from one to ten?</p>
    <p>Initially you'd put it at {{ scale }}.</p><br>
    <p>Excellent. Use that awareness of value to help motivate you.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="loadSubscript === 'emotional'">
    <p class="text-xl font-semibold mb-3">Emotional Script 4</p>
    <p class="font-bold">Best Possible Future</p><br>
    <p>Now, <span class="font-bold">[CALLER FIRST NAME]</span>, I want you to imagine your Best Possible Future, okay? </p>
    <p>This is where you want to be in, say, three or five or ten years.</p><br>
    <p>You can think about your Best Possible Future in terms of academics, career, hobbies, health, or any other aspect of your life that feels most important to you right now.</p><br>
    <p>But whatever it is, be specific…If you’re imagining a particular job, then I want you to:</p>
    <ul class="ml-5">
      <li>Imagine exactly what you would do</li>
      <li>Who you would work with</li>
      <li>and where it would be</li>
    </ul>
    <br>
    <p>Alight, what is your Best Possible Future?</p>
    <p class="text-gray-700 italic">Listen to caller response</p><br>
    <p v-if="callerApplication === 'sa'">Now I want you to consider how you never mentioned “<span class="font-bold">[SPECIFIC APPLICATION]</span>” as part of your best life.</p>
    <p v-else>Now I want you to consider how you never mentioned any of the specific assignments that you’re working on now as part of your best life.</p>
    <p>I think this is important to remember: Sometimes, when we frame a task as valuable or important to us, we can make the mistake of inadvertently making it seem more significant than it really is. Most of the things we end up doing are stepping stones. Each stepping stone can give you an important foothold, but don’t lose sight of the more significant thing you’re using those stepping stones to get to: your goal. </p><br>
    <p>Alright, let’s move on.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'motivational'">
    <p class="text-xl font-semibold mb-3">Motivation Track - Practicing Control</p>
    <p>Are you ready?</p>
    <p>Good! We can Start with control.</p>
    <p>Taking control of your goals and the path you take to get to your goals is an important first step to success. This means you have to embody the idea that the goals you set and the steps you take to get there matter.</p>
    <p>How does time management fit into this? Well, proper time management can help save you time and effort by using your available time and effort efficiently.</p><br>
    <p>Let me ask you this: What are some things you would do if you had more time?</p>
    <textarea rows="3" placeholder="Agent Notes" class="w-3/4 mt-3"></textarea>
    <p>That’s great! There’s some motivation right there. I want you to be able to do all of those things too.</p><br>
    <p>So let’s focus on some things you can do to practice control over your time.</p>
    <p><span class="font-bold">First</span>, you can create and maintain a schedule or calendar.</p>
    <ul class="ml-5">
      <li>This sounds simple, and it is. But it can also be incredibly important for developing a sense of control.</li>
      <li>When you create a schedule or calendar, you are literally organizing your time. Of course, there are things you will have to do - class times, work shifts, other responsibilities - but there will also be chunks of time that you will be fully in charge of. That doesn’t mean you can do anything you want in those times (you still have responsibilities), but you do control them, and by consciously scheduling those times you are asserting that control.</li>
    </ul><br>
    <p><span class="font-bold">Second</span>, you can write your own earlier deadlines for course assignments.</p>
    <ul class="ml-5">
      <li>I know it sounds bonkers to do work early, but this isn’t about trying to be a great student; it’s about taking control of your time. If you create your own deadlines, you’re asserting that much more control over your time.</li>
      <li>Your deadlines don’t have to be that much earlier, either. If you have an assignment due at noon, you could set yourself a deadline to do it by eleven.</li>
    </ul><br>
    <p><span class="font-bold">Third</span>, you can share your plans with others.</p>
    <ul class="ml-5">
      <li>This lets others know (and yourself know) that you are in charge of your own time.</li>
    </ul>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'organizational'">
    <p class="text-xl font-semibold mb-3">Organization Track - Prioritization Booster 1</p>
    <p>As you know, we have too many things to do each day. It’s not always possible to do everything on our to-do list.</p>
    <p>Finding the value in the tasks we need to accomplish is one way to help us prioritize that task.</p>
    <p>But even though every task that we need to accomplish has some value to us, those values are relative.</p>
    <p>What I mean is, some tasks are just more important, urgent, or necessary than others.</p>
    <p>Taking a moment to prioritize tasks can help you make decisions about which tasks to focus on first or longest. It can also help identify tasks that you can eliminate or put off for a later date.</p><br>
    <p>To help with this, you’re going to use a simple 2x2 grid.</p>
    <p>Draw a rectangle and divide that rectangle into 4 sections.</p>
    <p>Each box will be labeled</p>
    <ul class="ml-5">
      <li>Above the top-left box write “urgent” and above the top-right box “not urgent”.</li>
      <li>Along the side of the top-left box write the word “important” and along the side of the bottom-left box write “less important”.</li>
    </ul>
    <p>Now you have a 2x2 grid to prioritize your tasks at any given time.</p>
    <img src="/images/section-graph.png" alt="section graph">
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'motivational'">
    <p class="text-xl font-semibold mb-3">Motivation Track - Increase Curiosity</p>
    <p>The second thing we can work on is increasing our curiosity.</p>
    <p>You might wonder what curiosity has to do with motivation.</p>
    <ol class="ml-5">
      <li>Attempt to streamline your weekly plan
        <ul class="ml-5">
          <li>Can you adjust your planning to be more consistent with your overall goals?</li>
          <li>Can you eliminate overlapping tasks?</li>
          <li>Can you make your travel time more efficient?</li>
        </ul>
      </li>
      <li>Sense of Competence
        <ul class="ml-5">
          <li>Can you realize the value in the work that you do?</li>
        </ul>
      </li>
      <li>Sense of Meaning
        <ul class="ml-5">
          <li>Does material you learn in one class apply to other classes, improve your understanding of other class subject matter, or inspire new questions?</li>
        </ul>
      </li>
    </ol>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'organizational'">
    <p class="text-xl font-semibold mb-3">Organization Track - Prioritization Booster 2</p>
    <p v-if="callerApplication === 'sa'">So, let's put this simple grid into practice by filling it in with everything you need to do [between now and <span class="font-bold">[TIME CONSTRAINT]</span>]</p>
    <p v-else>So, let’s put this simple grid into practice. To help focus things, I want you to think about where tasks related to <span class="font-bold">[APPLICATION]</span> fit into the grid as you do this.</p>
    <p>Note: As an exercise, walk Caller through filling out the grid. Talking points for each quadrant are listed below</p><br>
    <p class="font-bold">Talking points for each quadrant</p>
    <p class="font-semibold">Urgent & Important</p>
    <ol class="ml-5">
      <li>Pressing Problems</li>
      <li>Deadline Close</li>
    </ol>
    <br>
    <p class="font-semibold">Not Urgent but Important</p>
    <ol class="ml-5">
      <li>Long term planning</li>
      <li>Personal growth</li>
      <li>Health and Wellness activities (exercise, etc.)</li>
    </ol>
    <br>
    <p class="font-semibold">Urgent but Not Important</p>
    <ol class="ml-5">
      <li>Emails</li>
      <li>Calls</li>
      <li>Last minute or spur-of-the-moment activities</li>
    </ol>
    <br>
    <p class="font-semibold">Not Urgent & Not Important</p>
    <ol class="ml-5">
      <li>Things that take you away from your goals</li>
    </ol>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'motivational'">
    <p class="text-xl font-semibold mb-3">Motivation Track - Modulating Challenge</p>
    <p>Stretch the boundaries of your comfort zone. Testing your limits will increase the meaningfulness of your accomplishments.</p><br>
    <p>Set challenges that are attainable yet present some difficulty.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'organizational'">
    <p class="text-xl font-semibold mb-3">Organization Track - Prioritization Booster 3</p>
    <p>So what do you do with this information?</p><br>
    <p class="font-bold">Tasks that are urgent and important should be prioritized.</p>
    <p>If you find yourself working on tasks that either aren’t important or aren’t urgent while you still have some of those urgent and important tasks to do, you should ask yourself if you are really using your time to your best advantage.</p><br>
    <p class="font-bold">Your daily or weekly plan should make note of tasks that are not urgent but are important and begin planning for them.</p><br>
    <p class="font-bold">Tasks that are urgent but not important can be incorporated into your daily plan as they fit.</p>
    <p>Often, these tasks are small and not very time consuming - like answering emails - or don’t require much sustained effort or focus and can be scheduled in-between more important tasks or during times of the day when your attention is waning or is divided.</p><br>
    <p class="font-bold">Any tasks that you’ve listed in the not urgent and not important quadrant should be reevaluated.</p>
    <p>Why should you continue to give your limited time and energy to this task or responsibility that is neither urgent nor important to you?
      If you find that the task does matter to you, that’s fine. Move it into one of the other quadrants. Otherwise: ditch it. Life is too short and our time and energy is too limited to waste on things that aren’t important.
    </p><br>
    <p>Next, we’ll talk about splitting larger tasks up into smaller tasks.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="challengeType === 'motivational'">
    <p class="text-xl font-semibold mb-3">Motivation Track - Rewarding</p>
    <p>Discover ways to reward yourself!</p>
    <ol class="ml-5">
      <li>Identify people, places, things, or ideas that you enjoy. Things that make you smile, make you happy, or make you thankful.</li>
      <li>Schedule time for those as a reward for attaining your goals.</li>
      <li>Hold yourself accountable.</li>
    </ol>
    <p>Find a reliable accountability partner</p><br>
    <p>Next, we’ll talk through a really simple exercise that can help reimagine more challenging tasks as smaller, less complex mini-tasks.</p>
    <p>Thinking about the things we have to do in this way can help motivate us to do them. After all, it’s easier to “Write a thesis statement” than it is to “Write a six-page essay,” although by writing a thesis statement you are already starting to work on that six-page essay.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Subdivision Booster 1</p>
    <p>Many tasks are more complex than they seem at first, composed of multiple, interrelated actions.</p>
    <p>Research shows that by breaking these complex tasks into smaller, more closely defined tasks we enable ourselves to concentrate more deeply and focus more effectively than we would otherwise.</p>
    <p>We call this task subdivision</p>
    <p>For example:</p>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flow-root">
        <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <table class="min-w-full divide-y divide-gray-300">
              <thead>
              <tr class="divide-x divide-gray-200">
                <th scope="col" class="py-3.5 pl-4 pr-4 text-left text-sm font-semibold text-gray-900 sm:pl-0">Original Task</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Subdivided Tasks</th>
              </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">1. Write an essay</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">
                  <ol class="ml-5">
                    <li>Read the essay prompt</li>
                    <li>Complete assigned reading</li>
                    <li>Reread essay prompt</li>
                    <li>Brainstorm topic</li>
                    <li>Conduct Research</li>
                    <li>Write thesis</li>
                    <li>Write body paragraphs</li>
                    <li>Write introduction</li>
                    <li>Write conclusion</li>
                    <li>Edit and Format essay</li>
                    <li>Submit</li>
                  </ol>
                </td>
              </tr>
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">2. Get the car fixed</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">
                  <ol class="ml-5">
                    <li>Locate a mechanic</li>
                    <li>Call mechanic to schedule maintenance</li>
                    <li>Check bank funds</li>
                    <li>Arrange alternative transportation, if necessary</li>
                    <li>Drop car off at mechanic</li>
                  </ol>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <p>This process will make it easier for you to prioritize and schedule the various subtasks. Make sense?</p>
    <p v-if="callerApplication === 'sa'">Let's walk through this process for your <span class="font-bold">[SPECIFIC APPLICATION]</span></p>
    <p v-else>Let's walk through this process using <span class="font-bold">[APPLICATION]</span> as an example.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Subdivision Booster 2</p>
    <p>Okay. How might you subdivide <span class="font-bold">[APPLICATION]</span> into smaller, more defined tasks that you can tackle one by one.</p>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flow-root">
        <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <table class="min-w-full divide-y divide-gray-300">
              <thead>
              <tr class="divide-x divide-gray-200">
                <th scope="col" class="py-3.5 pl-4 pr-4 text-left text-sm font-semibold text-gray-900 sm:pl-0">Original Task</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Subdivided Tasks</th>
              </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">1. APPLICATION</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">
                  <textarea rows="5" v-model="subdividedTasks" placeholder="Agent Notes..." class="w-3/4 my-3"></textarea>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <p>Because subdividing tasks breaks complex tasks into a series of smaller, discrete tasks, it can also be a helpful way of deciding how to begin a task that you don’t quite know how to start. </p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Time and Effort Booster 1</p>
    <p>Everyone has some subjects or activities that they are better at, or that come more naturally to them, and other subjects or activities that they struggle a little more with.</p>
    <p>There’s no shame in this because it’s true for all of us.</p>
    <p>The question is, how do we acknowledge and respond to this reality in a way that helps us do our best?</p><br>
    <p>One way to approach this challenge is to simply be mindful of those subjects or tasks that don’t come as easily as you would like, and to then budget more time and effort to completing them. In other words, be pragmatic and remember:</p>
    <p class="font-bold">More difficult tasks require two things:</p>
    <ol class="ml-5">
      <li class="font-bold">More Time</li>
      <li class="font-bold">More Effort</li>
    </ol>
    <br>
    <p>Let's talk about how to use this idea to help guide your actions.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Time and Effort Booster 2</p>
    <p>Since more challenging tasks require <span class="font-bold">more time</span>, you should</p>
    <ol class="ml-5">
      <li>Plan to dedicate more time to more challenging tasks.</li>
      <li>Plan more challenging tasks for when you have more time available.</li>
    </ol>
    <p>Are there certain times of day or certain days of the week when you have more time available?</p>
    <table class="min-w-full divide-y divide-gray-300 border-2 mt-3">
      <thead>
      <tr>
        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Mornings</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Afternoons</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Evenings</th>
      </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-0">
          <fieldset>
            <div class="space-y-2">
              <div v-for="morning in mornings" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="morning.id" :value="morning.id" type="checkbox" v-model="morningAvailableTimes" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="morning.id" class="font-medium text-gray-900">{{ morning.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <fieldset>
            <div class="space-y-2">
              <div v-for="afternoon in afternoons" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="afternoon.id" :value="afternoon.id" type="checkbox" v-model="afternoonAvailableTimes" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="afternoon.id" class="font-medium text-gray-900">{{ afternoon.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <fieldset>
            <div class="space-y-2">
              <div v-for="evening in evenings" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="evening.id" :value="evening.id" type="checkbox" v-model="eveningAvailableTimes" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="evening.id" class="font-medium text-gray-900">{{ evening.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
      </tr>
      </tbody>
    </table>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Time and Effort Booster 3</p>
    <p>Since more challenging tasks require <span class="font-bold">more time</span>, you should</p>
    <ol class="ml-5">
      <li>Plan to dedicate more time to more challenging tasks.</li>
      <li>Plan more challenging tasks for when you have more time available.</li>
    </ol>
    <p>Are there certain times of day or certain days of the week when you generally feel more energized or focused?</p>
    <table class="min-w-full divide-y divide-gray-300 border-2 mt-3">
      <thead>
      <tr>
        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Mornings</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Afternoons</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Evenings</th>
      </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-0">
          <fieldset>
            <div class="space-y-2">
              <div v-for="morning in mornings" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="morning.id" :value="morning.id" type="checkbox" v-model="morningFocusedTimes" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="morning.id" class="font-medium text-gray-900">{{ morning.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <fieldset>
            <div class="space-y-2">
              <div v-for="afternoon in afternoons" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="afternoon.id" :value="afternoon.id" type="checkbox" v-model="afternoonFocusedTimes" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="afternoon.id" class="font-medium text-gray-900">{{ afternoon.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <fieldset>
            <div class="space-y-2">
              <div v-for="evening in evenings" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="evening.id" :value="evening.id" type="checkbox" v-model="eveningFocusedTimes" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="evening.id" class="font-medium text-gray-900">{{ evening.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
      </tr>
      </tbody>
    </table>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Time and Effort Booster 4</p>
    <p>Imagine your answers plotted on a Venn diagram (this is the diagram with the two circles that overlap in the middle).</p>
    <img src="/images/time-management-2.png" alt="Time Management 2">
    <p>One circle contains those times during the day/week when you have more time available.</p>
    <p>The other circle contains those times when you feel most energized and focused.</p>
    <p>Where those answers overlap, that’s when you want to schedule those activities or tasks you find most challenging, difficult, or demanding.</p><br>
    <p class="font-bold">Time and Focus overlap:</p>
    <textarea rows="3" v-model="overlap" placeholder="Agent Notes..." class="w-3/4 my-3"></textarea>
    <p><span class="font-bold">PS NOTE:</span> If there is no overlap: “Currently you haven’t identified a time when you both have time and feel energized. Something you might consider doing is taking a look at your current schedule and seeing what you can move around so that, at least once a week, you have some flex time to schedule those really demanding, difficult tasks that require time and energy. And remember that feeling “energized” is relative - even if you’re exhausted most of the time (and aren’t we all!), there are still times of the day when you are less exhausted and more able to focus.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Time and Effort Booster Application</p>
    <p>Like you know - and like the exercise we just completed hopefully made clear as well - your time and effort is valuable.</p>
    <p>It’s valuable because it’s limited: you only have so much time, and so much energy to put toward all of the things you have to do.</p>
    <p>In general, you want your best efforts to be directed at your most challenging tasks.</p><br>
    <p>If we define challenging tasks by either…</p>
    <ol class="ml-5">
      <li>Their level of difficulty</li>
      <li>The amount of time needed to complete them, or</li>
      <li>Their urgency</li>
    </ol>
    <br>
    <p>...I wonder if you might be able to identify one or two of the subdivided tasks that you mentioned earlier in the call that you would describe as “challenging” or at least “more challenging than the others”?</p>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="flow-root">
        <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
            <table class="min-w-full divide-y divide-gray-300">
              <thead>
              <tr class="divide-x divide-gray-200">
                <th scope="col" class="py-3.5 pl-4 pr-4 text-left text-sm font-semibold text-gray-900 sm:pl-0">Original Task</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Subdivided Tasks</th>
              </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white">
              <tr class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-0">1. APPLICATION</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">
                  <textarea rows="5" v-model="subdividedTasks" placeholder="Agent Notes..." class="w-3/4 my-3"></textarea>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <p>Excellent.</p>
    <p>So if you were putting together a time management schedule or plan, you would probably want to consider working on those tasks:</p>
    <p class="font-bold">Time and Focus overlap:</p>
    <textarea rows="3" v-model="overlap" placeholder="Agent Notes..." class="w-3/4 my-3"></textarea>
    <p>So then you would build your schedule backwards from there.</p><br>
    <p>For instance, if I knew I was going to struggle figuring out a thesis for a history paper, then I might plan to dedicate my Thursday afternoon (which is when I have both free time and the most energy) to working on that thesis.</p><br>
    <p>Of course, before I can write a thesis, I need to complete all of the readings and reread the paper assignment prompt. So, going back to my schedule, I would figure out times when I could schedule in those tasks before Thursday afternoon.</p>
    <hr class="mt-3">
  </div>
</template>

<script setup>
import { ref } from "vue";

const callerApplication = ref(null)
const loadSubscript = ref(null)
const challengeType = ref(null)
const scale = ref(null)
const loadExercise = ref(null)
const subdividedTasks = ref(null)
const morningAvailableTimes = ref([])
const afternoonAvailableTimes = ref([])
const eveningAvailableTimes = ref([])
const overlap = ref(null)

const morningFocusedTimes = ref([])
const afternoonFocusedTimes = ref([])
const eveningFocusedTimes = ref([])

const mornings = [
  {
    id: 'morning-1',
    label: 'Weekday mornings'
  },
  {
    id: 'morning-2',
    label: 'Weekend mornings'
  },
  {
    id: 'morning-3',
    label: 'Monday mornings'
  },
  {
    id: 'morning-4',
    label: 'Tuesday mornings'
  },
  {
    id: 'morning-5',
    label: 'Wednesday mornings'
  },
  {
    id: 'morning-6',
    label: 'Thursday mornings'
  },
  {
    id: 'morning-7',
    label: 'Friday mornings'
  },
  {
    id: 'distraction-8',
    label: 'Saturday mornings'
  },
  {
    id: 'distraction-9',
    label: 'Sunday mornings'
  },
]
const afternoons = [
  {
    id: 'afternoon-1',
    label: 'Weekday afternoons'
  },
  {
    id: 'afternoon-2',
    label: 'Weekend afternoons'
  },
  {
    id: 'afternoon-3',
    label: 'Monday afternoons'
  },
  {
    id: 'afternoon-4',
    label: 'Tuesday afternoons'
  },
  {
    id: 'afternoon-5',
    label: 'Wednesday afternoons'
  },
  {
    id: 'afternoon-6',
    label: 'Thursday afternoons'
  },
  {
    id: 'afternoon-7',
    label: 'Friday afternoons'
  },
  {
    id: 'afternoon-8',
    label: 'Saturday afternoons'
  },
  {
    id: 'afternoon-9',
    label: 'Sunday afternoons'
  },
]
const evenings = [
  {
    id: 'evening-1',
    label: 'Weekday evenings'
  },
  {
    id: 'evening-2',
    label: 'Weekend evenings'
  },
  {
    id: 'evening-3',
    label: 'Monday evenings'
  },
  {
    id: 'evening-4',
    label: 'Tuesday evenings'
  },
  {
    id: 'evening-5',
    label: 'Wednesday evenings'
  },
  {
    id: 'evening-6',
    label: 'Thursday evenings'
  },
  {
    id: 'evening-7',
    label: 'Friday evenings'
  },
  {
    id: 'evening-8',
    label: 'Saturday evenings'
  },
  {
    id: 'evening-9',
    label: 'Sunday evenings'
  },
]
</script>