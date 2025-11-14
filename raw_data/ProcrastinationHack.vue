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
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Specific Application / ATE</label>
        </div>
        <div class="flex items-center">
          <input name="caller-application" value="gp" v-model="callerApplication" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">General Procrastination</label>
        </div>
      </div>
    </fieldset>
    <br>
    <p>What would you like to accomplish immediately after this call. That is, what do you hope our session will prepare you to do?</p><br>
    <p>Caller Goals for this Session</p>
    <textarea rows="3" placeholder="Agent Notes: Caller Goals" class="w-3/4 my-3"></textarea>
    <p>Are you working with any time constraints, like upcoming deadlines?</p>
    <ul class="ml-5">
      <li>Less than 24 hours [Diverts to Crunch Time solutions]</li>
      <li>Specific Time Constraint</li>
      <li>None</li>
    </ul>
    <br>
    <p class="italic">Confirm and clarify above selections and call goals before continuing.</p>
  </div>
  <hr>
  <div class="my-3">
    <p>Now just a few more quick questions to help us put together an action plan that can work for you. There are no wrong answers here.</p><br>
    <p>My first question is about your comfort zone when it comes to setting and following through on your goals generally.</p><br>
    <p>Would you say you are more <span class="italic">flexible</span> or more <span>inflexible</span> when it comes to setting goals and sticking to them? You might think here of "flexible" as tending to align more with a "creative" or "spontaneous" personality, and "inflexible" as aligning more with "logical" or "rule-oriented" personalities.</p><br>
    <ul class="ml-5">
      <li>Flexible/Creative/Spontaneous</li>
      <li>Inflexible/Logical/Rule Oriented</li>
    </ul>
    <br>
    <p>My next question has to do with your perception of procrastination. Under normal circumstances do you find completing your work in the last minute to be:</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="procrastination-type" value="active" v-model="procrastinationType" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Exciting, or energizing (Active Procrastination)</label>
        </div>
        <div class="flex items-center">
          <input name="procrastination-type" value="passive" v-model="procrastinationType" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Stressful, or draining (Passive Procrastination)</label>
        </div>
      </div>
    </fieldset>
  </div>
  <hr>
  <div class="my-3" id="active-procrastination" v-if="procrastinationType === 'active'">
    <p class="text-xl font-semibold mb-3">Active Procrastinator Script</p>
    <p>Let's begin by addressing the facts... sometimes procrastination pays off. And contrary to what some people say, procrastination has its benefits. You might be able to name some benefits of procrastination. Go ahead! What might be some benefits in procrastination?</p><br>
    <p>Ok, but we should continue to be honest... Sometimes procrastination is an epic failure, right? Can you name some times procrastination doesn't work?</p><br>
    <p>So, you have thought about when it works for you and when it doesn't?</p>
    <table class="min-w-full divide-y divide-gray-300 border-2 mt-3">
      <thead>
      <tr>
        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Procrastination Works</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Procrastination Doesn't Work</th>
      </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-0">
          <ul class="ml-5">
            <li>I have expertise in the subject matter</li>
            <li>I am the only one working on this</li>
            <li>My schedule is open</li>
            <li>I am planning things out as I wait</li>
            <li>I have plenty of time</li>
          </ul>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <ul class="ml-5">
            <li>I am not an expert in the subject matter</li>
            <li>I have to rely on others</li>
            <li>My schedule is packed</li>
            <li>I am not thinking about assignment until later</li>
            <li>I have limited time</li>
          </ul>
        </td>
      </tr>
      </tbody>
    </table>
    <br>
    <p>What do you think we might learn from our list of when procrastination works and when it doesn't work?</p><br>
    <p>Ideally you would only want to procrastinate when the procrastination conditions are favorable to your success (Table 2, left column), otherwise it is best to space out your studies.</p>
  </div>
  <hr>
  <div class="my-3" id="passive-procrastination" v-if="procrastinationType === 'passive'">
    <p class="text-xl font-semibold mb-3">Passive Procrastinator Script</p>
    <p>I want us to try a short visualization exercise.</p>
    <ul class="ml-5">
      <li>Imagine you are a city bus. Not just on it. You <span class="italic underline">are</span> the bus.</li>
      <li>Where you would normally move about using your legs, you now have wheels.</li>
      <li>The interior of the bus is your mind.</li>
      <li>In your mind are passengers, each a unique version of yourself.</li>
      <li>Each version of yourself has different strengths and can perform certain tasks better than all the other passengers when that task requires their particular set of strengths.</li>
      <li>Each bus stop represents one of the tasks you need to get done during the day.</li>
      <li>Some stops are daily and others are 3x per week, or 4x per week, etc. For example, a class lecture may be three days a week and study time could be 2 days a week.</li>
      <li>The key success is to drop off the best version of you at the right stop for each task at hand.</li>
    </ul>
    <p>Can you imagine this in mind?</p><br>
    <p>Now who is going to drive the bus?</p>
    <p>What characteristics do you want in a bus driver?</p>
    <ul class="ml-5">
      <li>Reliable</li>
      <li>Knows the Route</li>
      <li>Consistent</li>
    </ul>
  </div>
  <hr>
  <div class="my-3" v-if="procrastinationType && callerApplication">
    <p>Finally, if you were to take a moment to think about it, would you say you're procrastination on your <span class="underline font-bold">[Specific Application / General Procrastination]</span> is due to managing distractions, having low motivation, or feeling uncertainty or anxiety about the outcome?</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
        <div class="flex items-center">
          <input name="procrastination-reasoning" value="distractions" v-model="reasoning" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Distractions</label>
        </div>
        <div class="flex items-center">
          <input name="procrastination-reasoning" value="motivation" v-model="reasoning" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Motivation</label>
        </div>
        <div class="flex items-center">
          <input name="procrastination-reasoning" value="uncertainty" v-model="reasoning" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Uncertainty</label>
        </div>
      </div>
    </fieldset>
    <br>
    <p class="italic">Clarify with keywords in columns below before proceeding!</p>
    <table v-if="reasoning" class="min-w-full divide-y divide-gray-300 border-2 mt-3">
      <thead>
      <tr>
        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0">Distractions</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Motivation</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Uncertainty</th>
      </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm text-gray-900 sm:pl-0">
          <fieldset>
            <div class="space-y-2">
              <div v-for="factor in distractionFactors" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="factor.id" :value="factor.id" type="checkbox" v-model="reasoningFactors" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="factor.id" class="font-medium text-gray-900">{{ factor.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <fieldset>
            <div class="space-y-2">
              <div v-for="factor in motivationFactors" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="factor.id" :value="factor.id" type="checkbox" v-model="reasoningFactors" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="factor.id" class="font-medium text-gray-900">{{ factor.label }}</label>
                </div>
              </div>
            </div>
          </fieldset>
        </td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
          <fieldset>
            <div class="space-y-2">
              <div v-for="factor in uncertaintyFactors" class="relative flex items-start">
                <div class="flex h-6 items-center">
                  <input :id="factor.id" :value="factor.id" type="checkbox" v-model="reasoningFactors" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
                <div class="ml-3 text-sm leading-6">
                  <label :for="factor.id" class="font-medium text-gray-900">{{ factor.label }}</label>
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
  <div class="my-3" v-if="reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distraction Script</p>
    <p>I want you to know that</p>
    <ul class="ml-5">
      <li>Research shows that it's difficult to avoid distractions that interfere with our performance. This is something everybody struggles with.</li>
    </ul>
    <br>
    <p>However,</p>
    <ul class="ml-5">
      <li>Research also shows that it is easier to form new healthy habits than to change old habits.</li>
    </ul>
    <br>
    <p>That said,</p>
    <ul class="ml-5">
      <li>Today we'll focus on forming new healthy habits rather than feeling shame about our current habits or tendency to be distracted.</li>
    </ul>
    <br>
    <p>To do this, we're going to implement a 3-step plan of attack to help minimize distraction and ward off some of those procrastinating tendencies.</p>
    <p>We call this the 3-P Process and it has 3 steps:</p>
    <ol class="ml-5">
      <li>Planning</li>
      <li>Practice</li>
      <li>Practicing Under Adversity</li>
    </ol>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty Script</p>
    <p>We’re going to focus today's call on reframing some of these feelings of uncertainty or anxiety you’ve mentioned, because those feelings are really at the heart of why you’re procrastinating.</p>
    <p>{{ 'You mentioned keywords: ' + convertSelectionsToText() }}</p><br>
    <p>We’ll practice some cognitive reframing techniques to help you take ownership of your situation as a way to minimize these feelings of uncertainty.</p>
    <p>Then, we’re going to put together a brief plan to help you kickstart your productivity and pursue success.</p><br>
    <p>Sounds good?</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Motivation Script</p>
    <p>We’re going to focus today's call on reframing how you approach and think about what you’re working on.</p>
    <p>{{ 'You mentioned keywords: ' + convertSelectionsToText() }}</p><br>
    <p>We’ll practice some cognitive reframing techniques to help you take ownership of your situation and find some purpose to guide you toward action.</p>
    <p>Then, we’re going to put together a brief plan to help you kickstart your productivity and pursue success.</p><br>
    <p>Sounds good?</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="procrastinationType === 'active'">
    <p v-if="reasoning === 'distractions'" class="text-xl font-semibold mb-3">Distraction - Cognitive (Specific Application, Active Procrastination)</p>
    <p v-if="reasoning === 'uncertainty'" class="text-xl font-semibold mb-3">Uncertainty - Cognitive (Specific Application, Active Procrastination)</p>
    <p v-if="reasoning === 'motivation'" class="text-xl font-semibold mb-3">Motivation - Cognitive (Specific Application, Active Procrastination)</p>
    <p v-if="callerApplication === 'sa'">Let's start by setting some intentions around your goals. By setting intentions, you're clarifying for yourself why working on <span class="font-bold">[SPECIFIC APPLICATION]</span> matters to you, and for people like you who are very logical, that can help you stay focused.</p>
    <p v-else>Let’s start by setting some intentions around your goals. By setting intentions, you’re clarifying for yourself why overcoming procrastination matters to you, and for people like you who are very logical, that can help you stay focused.</p>
    <br>
    <p>To do this, I want you to think about your goal in terms of how <span class="font-semibold">this experience</span> will <span class="font-semibold">benefit</span> you.</p><br>
    <p>But:</p>
    <ul class="ml-5">
      <li>I want you to think beyond the short term. Instead, try to identify <span class="font-semibold">a long-term benefit</span> success might provide you.
        <ul class="ml-5">
          <li>Something like, “The skills or knowledge I will gain from this will make me more attractive to potential employers.”</li>
          <li>OR, “If I do well on this, I will know a little bit more about how the world works, which is important to me.”</li>
        </ul>
      </li>
      <li>What matters is that it provides meaning to you and your long-term goals.</li>
      <li>But be specific: what skill or what knowledge specifically will you take away from this experience (class or assignment)?</li>
    </ul>
    <br>
    <p v-if="callerApplication === 'sa'">Ok, your turn, What are some benefits or values you think might get by performing well on your <span class="font-bold">[SPECIFIC APPLICATION]</span>?</p>
    <p v-else>Okay, your turn. What are some benefits or values you think you might get by combating procrastination?</p><br>
    <p class="font-bold">Caller Identified Benefits/Values</p>
    <textarea rows="3" placeholder="Agent Notes" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="procrastinationType === 'passive'">
    <p class="text-xl font-semibold mb-3">Emotional Connectivity 1 (Passive Procrastination)</p>
    <p>The relationship we have with our emotions can be complicated, and this can be especially true for people like you who are a bit more creative and spontaneous.</p><br>
    <p><span class="font-bold">[CALLER FIRST NAME]</span>, a lot of times, procrastination has a lot to do with how we feel about a looming task. If we have negative feelings around the task—maybe we’re worrying about failure, for instance—then we’re more likely to avoid it. And that avoidance? That’s procrastination.</p><br>
    <p>So, let’s just take a moment to run through some quick mental exercises that can help you connect with your positive emotions and gain some emotional perspective when it comes to procrastination.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="procrastinationType === 'passive'">
    <p class="text-xl font-semibold mb-3">Emotional Connectivity 2 (Passive Procrastination)</p>
    <p class="font-bold">Context Chair Exercise</p><br>
    <p>For this first exercise, you’ll need 2 chairs. If you don’t have two chairs nearby, that’s fine. You can just imagine them.</p>
    <p>Have you got your two chairs (or are you imagining your two chairs)?</p><br>
    <p>Ok, I want you to think of one chair as the optimism chair and the other as the pessimism chair.</p>
    <ol v-if="callerApplication === 'sa'" class="ml-5">
      <li>First, I want you to sit in the optimism chair. I want you to speak (aloud) some benefits you would receive for completing <span class="font-bold">[SPECIFIC APPLICATION]</span> on time</li>
      <li>Next, I want you to look over at the pessimism chair, but don’t sit down in it! We both know you don’t need to sit down in that chair to hear those negative thoughts about what if you don’t do well on the <span class="font-bold">[SPECIFIC APPLICATION]</span>. Instead, I want you to listen to those negative thoughts but counter them by speaking aloud a positive, optimistic thought.</li>
    </ol>
    <ol v-else class="ml-5">
      <li>First, I want you to sit in the optimism chair. I want you to speak (aloud) some benefits you’ll receive when you procrastinate less</li>
      <li>Next, I want you to look over at the pessimism chair, but don’t sit down in it! We both know you don’t need to sit down in that chair to hear those negative thoughts about what if you keep procrastinating. Instead, I want you to listen to those negative thoughts but counter them by speaking aloud a positive, optimistic thought.</li>
    </ol>
    <br>
    <p>The benefit of this exercise is that it helps you create a tool that you can use to create a positive expectation for the future that can help you to perform at your best.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="procrastinationType === 'passive'">
    <p class="text-xl font-semibold mb-3">Emotional Connectivity 3 (Specific Application, Passive Procrastination)</p>
    <p class="font-bold">Best Possible Future</p><br>
    <p>Now, <span class="font-bold">[CALLER FIRST NAME]</span>, let’s leave the present for a moment and I want you to imagine your Best Possible Future, okay? This is where you want to be in, say, three or five or ten years.</p>
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
    <p>I think this is important to remember: Sometimes the significance of a thing seems so heavy at the moment, when in reality, it’s pretty insignificant in terms of the bigger picture of our life, right? Maybe it’s a steppingstone, but in the end that’s all it is. You’ll do more important things later.</p><br>
    <p>Alright, let’s move on.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty - Take Ownership (Active Procrastination)</p>
    <p>I also want you to practice “taking ownership” of your situation by controlling how your mind “sees” in <span class="italic">time</span> and <span class="italic">space</span>.</p>
    <p>What do I mean by this?</p><br>
    <p>Well, let's use an example: Daydreaming.</p>
    <p>A daydream is an example of one way your mind can “see” in <span class="italic">time</span>.</p>
    <p>Typically, when we talk about daydreaming, we think about positive outcomes or things we would really enjoy doing. You might daydream about an experience you hope to have, or a place you look forward to going, and you get excited.</p>
    <p>In other words, daydreaming is a way of looking into the future and imagining what it will be like.</p><br>
    <p>But it’s also a way of visualizing <span class="italic">space</span>.</p>
    <p>For instance, again imagine you’re daydreaming about good things and good outcomes. How are you feeling during or even right after that daydream?</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>You feel good, right? Imagining good outcomes in the pretend time and space of your daydream actually affects how you feel in the actual time and space of the present!</p>
    <p>On the flip side, if you’re daydreaming about bad things or bad outcomes, you’re probably going to find yourself in a pretty negative head space, right?</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>Of course, in both of these situations you know that it’s just a daydream. That it’s not real. But it can still affect how you feel about your present and future.</p><br>
    <p><span class="font-bold">[CALLER FIRST NAME]</span>. I want you to think of your moments of uncertainty as a form of daydreaming.</p>
    <p>When you start feeling unsure or uncertain about something, remind yourself that this is because you are making a negative prediction about what will or could potentially occur in the future. It’s just a prediction. Try to counter these negative thoughts with positive predictions for the future.</p><br>
    <p>Would you like to try one exercise that can help you do this?</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="load-exercise" value="true" v-model="loadExercise" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Yes [Load Context Chair]</label>
        </div>
        <div class="flex items-center">
          <input name="load-exercise" value="false" v-model="loadExercise" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">No [Move On]</label>
        </div>
      </div>
    </fieldset>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty' && loadExercise === 'true' && procrastinationType === 'active'">
    <p class="text-xl font-semibold mb-3">Context Chair Exercise</p>
    <p>For this first exercise, you’ll need 2 chairs. If you don’t have two chairs nearby, that’s fine. You can just imagine them.</p>
    <p>Have you got your two chairs (or are you imagining your two chairs)?</p><br>
    <p>Ok, I want you to think of one chair as the optimism chair and the other as the pessimism chair.</p>
    <ol v-if="callerApplication === 'sa'" class="ml-5">
      <li>First, I want you to sit in the optimism chair. I want you to speak (aloud) some benefits you would receive for completing <span class="font-bold">[SPECIFIC APPLICATION]</span> on time</li>
      <li>Next, I want you to look over at the pessimism chair, but don’t sit down in it! We both know you don’t need to sit down in that chair to hear those negative thoughts about what if you don’t do well on the <span class="font-bold">[SPECIFIC APPLICATION]</span>. Instead, I want you to listen to those negative thoughts but counter them by speaking aloud a positive, optimistic thought.</li>
    </ol>
    <ol v-else class="ml-5">
      <li>First, I want you to sit in the optimism chair. I want you to speak (aloud) some benefits you’ll receive when you procrastinate less</li>
      <li>Next, I want you to look over at the pessimism chair, but don’t sit down in it! We both know you don’t need to sit down in that chair to hear those negative thoughts about what if you keep procrastinating. Instead, I want you to listen to those negative thoughts but counter them by speaking aloud a positive, optimistic thought.</li>
    </ol>
    <br>
    <p>The benefit of this exercise is that it helps you create a tool that you can use to create a positive expectation for the future that can help you to perform at your best.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty' && loadExercise === 'true' && procrastinationType === 'passive'">
    <p class="text-xl font-semibold mb-3">Imaging Success Exercise</p>
    <p v-if="callerApplication === 'sa'">This exercise is about imagining what achieving your desired goals looks like to you.</p>
    <p v-if="callerApplication === 'sa'">This about your <span class="font-bold">[SPECIFIC APPLICATION]</span>, I want you to imagine you've already achieved your goals regarding <span class="font-bold">[SPECIFIC APPLICATION]</span>.</p>
    <p v-if="callerApplication === 'gp'">For this exercise, I want you to think about what your life looks like after you’ve accomplished some of your current goals. </p>
    <br>
    <p>How did you get there?</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>What are the skills you used to get there?</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>What you’ve just done is you’ve replaced negative predictions about the future with a positive prediction, and you’ve identified a list of skills that you already possess and that you can use to achieve that positive prediction.</p><br>
    <p>Now that you can picture what it’s like to achieve your goal, we should address what that road to your destination looks like. </p>
    <p>Keep in mind, research shows we perform our best when we are challenged, not when things are easy or when they are extremely difficult. This may make things slightly uncomfortable at times, but I’ll show you how much easier it is to span the gap between where you are and where you want to be when you have a well built bridge in place.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Present: Do</p>
    <p>Imagining the future in positive terms can help you clarify your goals.</p>
    <p>It can also help motivate you in the present.</p>
    <p>Now, I want you to think about the present.</p><br>
    <p>What does “being in the present” mean to you?</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>Good! Being in the present means not feeling encumbered by the past or worried about the future. It means you are able to focus on what you are doing <span class="italic">now</span>.</p>
    <p>Any time you think about the present, I want you to think, “doing”. The present is for <span class="italic">doing</span>.</p><br>
    <p>In order to do this you need to be confident in two things: </p>
    <ol class="ml-5">
      <li>Your goal (that positive future vision we just discussed) and</li>
      <li>Your plan to get there (bridge building).</li>
    </ol>
    <br>
    <p>A lot easier said than done, I know. But I want you to repeat after me: “Being in the present means focusing on <span>doing</span>.”</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>Well done!</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Revaluing the Assignment 1</p>
    <p>On a scale from 1 to 10, how important do you feel this <span class="font-bold">[SPECIFIC APPLICATION]</span> is to you? </p><br>
    <input type="number" v-model="scale" class="block w-24 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Scale" />
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation' && scale > 0 && scale < 7">
    <p class="text-xl font-semibold mb-3">Revaluing the Assignment 2</p>
    <p>We tend to distance ourselves emotionally and cognitively from things we don’t find interesting or rewarding, and this distancing can present as procrastination. One thing you can do, then, to help with some motivation is try to find some personal value in the task.</p><br>
    <p v-if="callerApplication === 'sa'">Can you think of some ways you could view the <span class="font-bold">[SPECIFIC APPLICATION]</span> that might help you revalue it?</p>
    <p v-else>Can you think of some way the tasks or assignments you are putting off working on right now might hold value for you, particularly in the future?</p>
    <br>
    <p class="text-gray-700 italic">Follow-up question to press Caller, if needed</p>
    <p>Is there maybe some value to you in the assignment that you’re not considering?</p><br>
    <p class="text-gray-700 italic">If Caller still struggles to identify value</p>
    <p>Sometimes this exercise can be fairly straightforward, and sometimes it requires a little bit of creativity to do. Let’s try a short exercise.</p>
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
      <p class="font-bold">Caller Identified Values</p>
      <textarea rows="3" placeholder="Agent Notes: Identified Values" class="w-3/4 mt-3"></textarea>
      <p v-if="callerApplication === 'sa'">Does seeing some value in the <span class="font-bold">[SPECIFIC APPLICATION]</span> increase how important you feel the assignment is on that scale from one to ten? </p>
      <p v-else>Does seeing some value in the things you’re working on increase how important you feel they are on that scale from one to ten?</p>
    </div>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation' && scale >= 7">
    <p class="text-xl font-semibold mb-3">Revaluing the Assignment 3</p>
    <p>That’s great! The assignment is already pretty important to you, which means you’re already finding personal value in it. </p><br>
    <p v-if="callerApplication === 'sa'">What do you find is valuable to your future success about <span class="font-bold">[SPECIFIC APPLICATION]</span>?</p>
    <p v-else>What are some of the skills or attributes of these tasks that you find valuable?</p>
    <br>
    <p class="font-bold">Caller Identified Values</p>
    <textarea rows="3" placeholder="Agent Notes: Identified Values" class="w-3/4 mt-3"></textarea>
    <p>Excellent. Use that awareness of value to help motivate you to take ownership of <span class="font-bold">[SPECIFIC APPLICATION]</span>.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation' && loadExercise === 'true'">
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
    <p>Excellent. Use that awareness of value to help motivate you to take ownership of <span class="font-bold">[SPECIFIC APPLICATION]</span>.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Motivation - Deep Dive</p>
    <p>Another strategy to take ownership of what you’re working on is to make improvements on how, or in what order, the information is presented.</p><br>
    <p>Imagine you are the instructor teaching your own class. How would you reach students like yourself and persuade them to be more motivated or engaged with the material?</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Motivation - Finish Early</p>
    <p>Setting a self-imposed deadline earlier than the class deadline is a good way of motivating yourself to finish work you’d otherwise put off doing.</p><br>
    <p>Finishing early is a test of your ability to turn your intentions into actions. Self-imposed deadlines allow you to take action within your environment instead of reacting to it. Here is how this would work:</p>
    <ol class="ml-5">
      <li>Make your due date 1 class period sooner than the current deadline. (if class is once a week make your deadline a week sooner…if class is MWF and current due date is F change it to W).</li>
      <li>Set a reward  (Food/entertainment/trip/workout) for when you finish.</li>
      <li>Set a countdown to how many days you have until your new deadline.</li>
      <li>Specify daily goals (aligned with countdown) you want to accomplish for that assignment </li>
    </ol>
    <br>
    <p>Can you think of situations where this would be helpful?</p>
    <p class="text-gray-700 italic">Allow caller to answer, if yes, encourage elaboration</p><br>
    <p>What are some benefits of starting or finishing your work early?</p>
    <p class="font-bold">Possible Benefits</p>
    <ul class="ml-5">
      <li>Less stress or anxiety</li>
      <li>Less likely to NOT finish</li>
      <li>More Time to get help</li>
      <li>One less thing to do</li>
      <li>More flexibility</li>
      <li>Feeling of accomplishment</li>
      <li>More editing time</li>
    </ul>
    <br>
    <p class="font-bold">Reasons/Benefits to finish early</p>
    <textarea rows="3" placeholder="Agent Notes: Reasons/Benefits" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Motivation - Expressing Appreciation</p>
    <p>I would like us to just take a moment to express appreciation for where you are right now. Not your physical location, but where you are in terms relative to yourself.</p>
    <p>Think of how many years you have been alive?</p>
    <p class="italic text-gray-700">Caller Response Age</p><br>
    <p>Now reflect on how this whole year is only 1 of <span class="font-bold">[CALLER AGE]</span> years of your life.</p>
    <p>In terms of days, this day only accounts for 1 of <span class="font-bold">[CALLER AGE * 365]</span> days of your life so far.</p><br>
    <p>In other words, you have come far! And each day is just a small piece of your total life.</p>
    <p>If you see yourself in this light, you’ll realize your trajectory is moving upward and it will continue moving upward as your experiences increase and become richer over time. </p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="callerApplication === 'gp'">
    <p class="text-xl font-semibold mb-3">Determine Target</p>
    <p>We can begin the first step by using something you typically would put off doing.</p><br>
    <p>Do you have something that fits the bill? Maybe an upcoming assignment? Or an assignment you really procrastinated on in the past? It'll just serve as a concrete example for our conversation.</p>
    <p class="text-gray-700 italic">Allow caller to answer</p><br>
    <p>Great. Let's jump right in with your <span class="font-bold">[Caller Response Application]</span> as an example.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="callerApplication === 'sa' && reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distractions Task Planner - Specific Application</p>
    <p>Let’s start by determining what needs to go in the plan.</p>
    <p v-if="procrastinationType === 'passive'">If you think back to our bus stop analogy, what we're doing now is equivalent to planning the stops for our bus route so that when the driver gets on the bus, they already have a plan for where they are going.</p>
    <p>You said you had until <span class="font-bold">[Time-Constraint]</span>, is that right?</p><br>
    <p>Great. So, what are some things you need to accomplish for your <span class="font-bold">[Specific Application]</span> between now and then?</p>
    <textarea rows="3" placeholder="Agent Notes: Task List" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="callerApplication === 'gp' && reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distractions Task Planner - General Procrastination</p>
    <p>To help us plan, let’s come up with a fake due date for an assignment. You might think about what the usual lead time you have between when you learn about an assignment and when it becomes due. Maybe that’s a week, or two weeks, or three days. Can you come up with a reasonable due date?</p><br>
    <p>Excellent. So, given that our due date is in/on _______, let’s brainstorm some things you would need to do for your assignment between now and then?</p>
    <p v-if="procrastinationType === 'passive'">If you think back to our bus stop analogy, what we’re doing now is equivalent to planning the stops for our bus route so that when the driver gets on the bus, they already have a plan for where they are going.</p>
    <textarea rows="3" placeholder="Agent Notes: Task List" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty Task Planner</p>
    <p>So far, we’ve focused on controlling feelings of uncertainty by defining your goals and cultivating a positive outlook for the future that, in turn, helps create a positive attitude in the present.</p><br>
    <p>Here is where the really important work of the present comes into play.</p>
    <p>Somehow, you need to channel your positive present emotions into efforts that can help bring about that positive future vision.</p><br>
    <p>The best way to do that is to create a daily schedule to direct your efforts, and then to place your trust in that daily schedule.</p>
    <div v-if="callerApplication === 'sa'">
      <p v-if="procrastinationType === 'passive'">If you think back to our bus stop analogy, what we’re doing now is equivalent to planning the stops for our bus route so that when the driver gets on the bus, they already have a plan for where they are going.</p><br>
      <p>You said you had until <span class="font-bold">[Time-Constraint]</span>, is that right?</p><br>
      <p>Great. So, what are some things you need to accomplish for your <span class="font-bold">[Specific Application]</span> between now and then?</p>
    </div>
    <div v-if="callerApplication === 'gp'">
      <p>To help us plan, let’s come up with a fake due date for <span class="font-bold">[Application]</span>. You might think about what the usual lead time you have between when you learn about an assignment and when it becomes due. Maybe that’s a week, or two weeks, or three days. Can you come up with a reasonable <span class="font-bold">[Time-Constraint]</span>?</p><br>
      <p>Excellent. So, given that our due date is in/on <span class="font-bold">[Time-Constraint]</span>, let’s brainstorm some things you would need to do for your <span class="font-bold">[Application]</span> between now and then?</p>
      <p v-if="procrastinationType === 'passive'">If you think back to our bus stop analogy, what we’re doing now is equivalent to planning the stops for our bus route so that when the driver gets on the bus, they already have a plan for where they are going.</p>
    </div>
    <textarea rows="3" placeholder="Agent Notes: Task List" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Motivation Task Planner</p>
    <p v-if="callerApplication === 'sa'">So far, we’ve talked about finding value and interest in your <span class="font-bold">[SPECIFIC APPLICATION]</span> as a way to see your efforts as worthwhile, both in the present and in the future.</p>
    <p v-else>So far, we’ve talked about finding value and interest in what you’re working on as a way to see your efforts as worthwhile, both in the present and in the future.</p>
    <p>But real motivation only comes after we take action, not before.</p>
    <p>I know that sounds counter-intuitive. If you lack motivation, then how are you supposed to take action to begin with?</p><br>
    <p>But this is where a little bit of grit and trust comes in handy.</p>
    <p>Because what the research shows is that the more action we take, the more motivated we become. So we can use action to help increase motivation.</p>
    <p>So let’s wrap up this call by putting together a simple schedule to get your efforts started.</p><br>
    <p v-if="procrastinationType === 'passive'">The first thing we need to do is to map out what needs to go in the schedule. If you think back to our bus stop analogy, what we’re doing now is equivalent to planning the stops for our bus route so that when the driver gets on the bus, they already have a plan for where they are going.</p><br>
    <div v-if="callerApplication === 'sa'">
      <p>You said you had until <span class="font-bold">[Time-Constraint]</span>, is that right?</p><br>
      <p>Great. So, what are some things you need to accomplish for your <span class="font-bold">[Specific Application]</span> between now and then?</p>
    </div>
    <div v-if="callerApplication === 'gp'">
      <p>To help us plan, let’s come up with a fake due date for <span class="font-bold">[Application]</span>. You might think about what the usual lead time you have between when you learn about an assignment and when it becomes due. Maybe that’s a week, or two weeks, or three days. Can you come up with a reasonable <span class="font-bold">[Time-Constraint]</span>?</p><br>
      <p>Excellent. So, given that our due date is in/on <span class="font-bold">[Time-Constraint]</span>, let’s brainstorm some things you would need to do for your <span class="font-bold">[Application]</span> between now and then?</p>
    </div>
    <textarea rows="3" placeholder="Agent Notes: Task List" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distractions Time Planner - Active Procrastination</p>
    <p>Ideally, when you’re creating a schedule, you want to set regular times for working on certain tasks. Planning the same task at about the same time creates consistency that, in the long term, can help turn that task into a habit.</p><br>
    <p>For instance, if you plan to set aside two hours every evening to study your biology notes, you might find that at first it’s really hard to get yourself to do it. But, after a few weeks, it starts to become easier until, eventually, it feels automatic to do it.</p><br>
    <p>Research shows that it can take anywhere from 18 to 66 days to form a new habit.</p><br>
    <p>Ideally, your schedule will help encourage the creation of productive habits like this.</p><br>
    <p v-if="procrastinationType === 'passive'">Again, if you think back to the bus stop analogy. These time slots function like the bus schedule. By putting them on your schedule, you’re committing to consistently be there.</p>
    <br>
    <p>Let’s think back to those tasks or activities you just brainstormed.</p><br>
    <p>Are there any of those tasks that you think might benefit from being assigned to regular, recurring times in your schedule in order to make them into longer-term habits?</p>
    <p class="text-gray-700 italic">Note: Performance Specialist (PS) adds notes to the Task/Activities to indicate caller's responses. For instance, if the Tasks/Activities from the previous screen included “Study biology notes… [enter], Write introduction paragraph… [enter], etc.” The Caller might identify “study biology notes” as a task that would benefit from repeatability. The PS would then add a note on the with “study biology notes” indicating “Habit”]</p><br>
    <p>Excellent. Now, let’s put our planning into practice by mapping out a schedule you can use to get started. </p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Performance Calendar Screen 1</p>
    <p class="text-gray-700 italic">Pull up a calendar before this script</p>
    <p>We're going to put together a schedule to help you move forward.</p>
    <p v-if="callerApplication === 'sa'">Using <span class="font-bold">[SPECIFIC APPLICATION]</span> as an example just to illustrate some best practices.</p><br>
    <p>I strongly encourage you to find something you can use to take down some notes as we do this, either pen and paper or pull up a calendar app on your phone or computer.</p>
    <p>We'll put together a schedule for: <span class="font-bold">Calendar Duration (Based on Time Constraint) - if no Time Constraint, use Two Weeks as the default.</span></p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
        <div class="flex items-center">
          <input name="calendar-duration" value="one-week" v-model="calendarDuration" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">One Week</label>
        </div>
        <div class="flex items-center">
          <input name="calendar-duration" value="two-weeks" v-model="calendarDuration" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Two Weeks</label>
        </div>
        <div class="flex items-center">
          <input name="calendar-duration" value="three-weeks" v-model="calendarDuration" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Three Weeks</label>
        </div>
        <div class="flex items-center">
          <input name="calendar-duration" value="one-month" v-model="calendarDuration" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">One Month</label>
        </div>
        <div class="flex items-center">
          <input name="calendar-duration" value="multi-month" v-model="calendarDuration" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Multi-month</label>
        </div>
      </div>
    </fieldset>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="calendarDuration">
    <p class="text-xl font-semibold mb-3">Performance Calendar Screen 2</p>
    <p>First thing we want to do is to take note of those elements of your schedule that you can’t change and need to plan around. Things like:</p>
    <ul class="ml-5">
      <li>Class times</li>
      <li>Appointments</li>
      <li>Sports practice, extra-curricular</li>
      <li>Etc.</li>
    </ul>
    <textarea rows="3" placeholder="Agent Notes: Caller necessary time commitments" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Performance Calendar Screen 3</p>
    <p>Great. Now that we know what you can’t change, let’s start thinking about when during your schedule you might add some of those tasks you identified earlier. <span class="text-gray-700 italic">Reference task list made previously.</span></p><br>
    <p>One great way to do this is to think about those tasks that you find harder or that require more concentration, and plan to do them during times of the day when you feel most awake or productive.</p>
    <p>Is there a time of day when you generally feel most energized or productive?</p>
    <p class="text-gray-700 italic">Caller answer time of day</p><br>
    <p>Okay, thinking about your schedule and remembering that, if possible, you want to schedule more difficult tasks during <span class="font-bold">[TIME OF DAY]</span>, when during the week do you think you can do each of your tasks? And whenever possible, try to block off time in hour-long increments.</p><br>
    <p class="text-gray-700 italic">Note: Performance Specialist should use Task/Activity notes to help Caller fill in their schedule. Additional tasks/activities can be scheduled as they come up. This is all done verbally, with the PS asking questions or offering suggestions as the Caller speaks. To help the PS, they should be able to see a Calendar of the appropriate duration and should have access to a Notes box to take down notes for themselves if desired.</p>
    <textarea rows="3" placeholder="Agent Notes" class="w-3/4 mt-3"></textarea>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Performance Calendar Screen 4</p>
    <p>There’s really only one more thing to do. I want you to look at all of those hour-long blocks of study and work time you’ve created and I want you to think of them as really two different buckets of time:</p>
    <ul class="ml-5">
      <li>A 45-minute time block where you are working on the task you've planned</li>
      <li>And a 15-minute block that you set aside for a break of some kind</li>
    </ul>
    <br>
    <p>This break can be anything you want it to be. Maybe it’s a snack break, or a short walk, or just some time to check your social and relax.</p>
    <p>So as you look at your schedule, remember that 15 minutes of every hour is a small reward and break time. Got it?</p><br>
    <p>Actually, one more thing. I want you to come up with a larger reward for yourself for when you’ve completed everything. It doesn’t need to be big and elaborate, but it should be something that gives you pleasure and that you don’t get to indulge in all of the time.</p><br>
    <p class="text-gray-700 italic">Listen to Caller and congratulate them</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distractions - Practicing Under Adversity - 1</p>
    <p>Setting a schedule is only really useful if you follow that schedule.</p>
    <p>{{ "We’ve already talked about the importance of Trusting the Process, which means making a plan and sticking to it even when those distracting factors you mentioned earlier: " + convertSelectionsToText() + " are still around. Because they will be right?" }}</p><br>
    <p>So, there’s one more thing I want to talk about, which is how to keep trusting in the process and letting your goals - and not your distractions - guide your actions.</p><br>
    <p>You might think of this as how to practice the behaviors and skills we’ve talked about even while facing adversity.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distractions - Practicing Under Adversity - 2</p>
    <p>There are three ways we deal with distractions:</p>
    <ol class="ml-5">
      <li>We can react to them, which we don't want to do, or</li>
      <li>We can prepare for them, or</li>
      <li>We can limit their control over our goals.</li>
    </ol>
    <p>So, let’s talk about a few techniques you can use to prepare for your distractions in order to limit their control over your goals.</p><br>
    <p>First, and possibly most importantly, is that you can <span class="font-bold">Set aside time specifically for your distractions</span>.</p>
    <p>Realistically, the things that distract us aren’t going away, right?</p>
    <ul class="ml-5">
      <li>You’ll always have family or friendship obligations that will require your time.</li>
      <li>Social media isn’t going away.</li>
      <li>The internet, video games, movies, TV shows… all of these things are going to try to capture our attention.</li>
    </ul>
    <p>Instead of approaching the things that distract you as if you could cut them out of your life, try scheduling specific times for your distractions.</p><br>
    <p>This might mean setting aside time every day for a social media break, or to call your family, or making sure to reserve one evening a week for playing video games or for just doing something for yourself.</p>
    <p>Let’s try scheduling some time during your week for your most common distractions.</p><br>
    <p class="text-gray-700 italic">Performance Specialist should review the schedule the Caller has made and suggest times to schedule some of the Caller’s distractions.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'distractions'">
    <p class="text-xl font-semibold mb-3">Distractions - Practicing Under Adversity - 3</p>
    <p>Equally important to setting aside time for your distractions is to</p>
    <p class="font-bold">Practice saying “No” to distractions EXCEPT for during the scheduled time.</p><br>
    <p>This requires practicing some discipline, which is essential. Just remember: when you give in to your distractions, you’re allowing them to define your actions. What you want to do is to</p>
    <p class="font-bold">Lead with your goals, which means: Let your actions be defined by your goals.</p><br>
    <p>Finally, <span class="font-bold">Good behavior should be rewarded.</span></p><br>
    <p>So, when you’ve been successful at saying no to your distractions during those times when you’re supposed to be working toward your goal: reward yourself!</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty - Practicing Conscientious</p>
    <p>Now that you’ve created a schedule, you want to stick to it. Trust in it.</p>
    <p>But remember: just because you’ve made a schedule, that doesn’t mean you can’t change it.</p><br>
    <p>And so the last thing you want to schedule each week is a time to reflect on what you have completed throughout the week, celebrate your accomplishments, and make any tweaks you think might help.</p>
    <p>During this once-a-week-at-most planning session is the <span class="font-bold">ONLY</span> time you evaluate what is working and what is not working in your plan and make adjustments accordingly.</p><br>
    <p>But remember…ONLY make changes once per week! </p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty Coda</p>
    <p>I want you to think about the plan you’ve created as a bridge between the Present and the Future. </p>
    <p>In the future are all those goals you’ve articulated. The present, meanwhile, is that space of optimism you’ve cultivated: a place full of possibility.</p>
    <p>It’s important as you work toward your future that you spend the bulk of your time and efforts firmly in the present, doing the tasks you’ve planned in order to get to the future you want.</p><br>
    <p>Ideally, you’d spend 75% of your time in the present, just doing the work you’ve set out for yourself and trusting in the process.</p>
    <p>Imagining the future can be really fun, but it should only account for about 10% of our time.</p>
    <p>The other 15% of your time can be usefully put toward reviewing, revising, and optimizing your planning (schedule).</p><br>
    <p>Some people do all three of these things, but end up spending too much or too little time on one or two of these processes. If you take a moment to think about it, about what percentage of time would you say you currently spend:</p>
    <ul class="ml-5">
      <li>Imagining the future (ideally around 10%)</li>
      <li>Planning (ideally around 15%)</li>
      <li>In the present, doing (ideally around 75%)</li>
    </ul>
    <br>
    <p class="text-gray-700 italic">Performance Specialist should bring Caller’s attention to where they are spending too much or too little time. If the Caller is in line with recommendation, PS should congratulate them</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty - Expressing Appreciation</p>
    <p>I would like us to just take a moment to express appreciation for where you are right now. Not your physical location, but where you are in terms relative to yourself.</p>
    <p>Think of how many years you have been alive?</p>
    <p class="italic text-gray-700">Caller Response Age</p><br>
    <p>Now reflect on how this whole year is only 1 of <span class="font-bold">[CALLER AGE]</span> years of your life.</p>
    <p>In terms of days, this day only accounts for 1 of <span class="font-bold">[CALLER AGE * 365]</span> days of your life so far.</p><br>
    <p>In other words, you have come far! And each day is just a small piece of your total life.</p>
    <p>If you see yourself in this light, you’ll realize your trajectory is moving upward and it will continue moving upward as your experiences increase and become richer over time. </p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'uncertainty'">
    <p class="text-xl font-semibold mb-3">Uncertainty - Practicing Under Adversity</p>
    <p>Remember, when you're feeling uncertainty around {{ convertSelectionsToText() }}</p><br>
    <p>Try to practice the responses we’ve talked about:</p>
    <p>First, practice Taking Ownership of your task by realizing that how you feel about the future matters. If you spend time imagining a positive future, you will be more likely to approach your present efforts positively.</p>
    <p>Second, remember to use your positive vision of the future to create a plan that can direct your present efforts toward realizing that positive future.</p>
    <p>Third, remember that the majority of your efforts should be spent in the present, trusting in and following the plan you’ve made and resisting the urge to worry about whether or not your efforts will pan out.</p><br>
    <p>Next, once a week, revisit your plan and make any tweaks to things that aren’t working.</p>
    <p>Finally, take the time to celebrate and reward your efforts.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="reasoning === 'motivation'">
    <p class="text-xl font-semibold mb-3">Motivation - Practicing Under Adversity</p>
    <p>It’s important to identify when and why you feel unmotivated to complete certain tasks; for instance when you find them: {{ convertSelectionsToText() }}</p><br>
    <p>When you encounter these feelings, that’s your adversity. In order to overcome that adversity, you need to practice the responses we’ve talked about:</p>
    <ul class="ml-5">
      <li>Practice re-valuing the assignment</li>
      <li>Do a Deep-Dive in the assignment or subject to discover something meaningful or interesting to you about the subject</li>
      <li>Plan to finish early by setting your own deadlines</li>
      <li>Remembering to express appreciation of where you’re at and where you can go</li>
    </ul>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Process Summary</p>
    <p v-if="reasoning === 'distractions'"><span class="font-bold">[FIRST NAME]</span>, remember that everybody struggles with distractions and with procrastination.</p>
    <p v-if="reasoning === 'uncertainty'"><span class="font-bold">[FIRST NAME]</span>, remember that everybody struggles with feelings of uncertainty and with procrastination.</p>
    <p v-if="reasoning === 'motivation'"><span class="font-bold">[FIRST NAME]</span>, remember that everybody struggles with a lack of motivation from time to time.</p>
    <p>But by allowing your actions to be guided by your goals, and by setting aside specific time for your distractions, you can create a plan that’s both realistic and oriented toward success.</p>
    <p>Above all, remember your goals and keep those in the forefront of your mind!</p><br>
    <p class="text-gray-700 italic">Review Caller Goals from the beginning of the call (Scroll up to top)</p><br>
    <p>Thanks for calling Dragonfly. Again, my name is <span class="font-bold">[Performance Specialist Name]</span>. Please take a moment or two to fill out the survey at the end of the call to let me know how I did today.</p><br>
    <p>Have a wonderful day!</p>
    <hr class="mt-3">
  </div>
</template>

<script setup>
import {ref, onMounted, watch} from "vue";

const callerApplication = ref(null)
const procrastinationType = ref(null)
const reasoning = ref(null)
const reasoningFactors = ref([])
const loadExercise = ref(null)
const scale = ref(0)
const calendarDuration = ref(null)

const distractionFactors = [
  {
    id: 'distraction-1',
    label: 'Attention Span'
  },
  {
    id: 'distraction-2',
    label: 'Busy'
  },
  {
    id: 'distraction-3',
    label: 'Daydreaming'
  },
  {
    id: 'distraction-4',
    label: 'Family Responsibilities'
  },
  {
    id: 'distraction-5',
    label: 'Friends'
  },
  {
    id: 'distraction-6',
    label: 'Social Media'
  },
  {
    id: 'distraction-7',
    label: 'Time Lapse'
  },
  {
    id: 'distraction-8',
    label: 'Video Games'
  },
  {
    id: 'distraction-9',
    label: 'TV / Movies'
  },
]
const motivationFactors = [
  {
    id: 'motivation-1',
    label: 'Boring'
  },
  {
    id: 'motivation-2',
    label: 'NOT enjoyable'
  },
  {
    id: 'motivation-3',
    label: 'NOT worth the effort'
  },
  {
    id: 'motivation-4',
    label: 'Tiring'
  },
]
const uncertaintyFactors = [
  {
    id: 'uncertainty-1',
    label: 'Fear of Failure, Grades / Control'
  },
  {
    id: 'uncertainty-2',
    label: 'Cannot Get Started, All or Nothing Mindset'
  },
  {
    id: 'uncertainty-3',
    label: 'Perfectionist'
  },
  {
    id: 'uncertainty-4',
    label: 'Organization'
  },
  {
    id: 'uncertainty-5',
    label: 'Overwhelming'
  },
]

watch(reasoning, () => {
  reasoningFactors.value = []
})

function convertSelectionsToText() {
  let string = ''
  reasoningFactors.value.forEach(factor => {
    let selection = ''
    if (reasoning.value === 'distractions') {
      selection = distractionFactors.find((element) => element.id === factor).label
    } else if (reasoning.value === 'motivation') {
      selection = motivationFactors.find((element) => element.id === factor).label
    } else {
      selection = uncertaintyFactors.find((element) => element.id === factor).label
    }
    string = string + selection + ', '
  })
  return string
}
</script>