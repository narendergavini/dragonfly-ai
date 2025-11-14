<template>
  <div class="mb-3">
    <p class="text-xl font-semibold mb-3">Call Application, Goals and Time Constraints</p>
    <p>Why don't you start off by telling me a little bit about why you are calling today.</p>
    <p>Feel free to share any details you think might be relevant to our conversation. For instance:</p><br>
    <p>Is there a particular assignment or exam you're working on?</p>
    <p class="font-semibold">Caller Application (Caller Response)</p>
    <br>
    <p>What would you like to accomplish immediately after this call. That is, what do you hope our session will prepare you to do?</p>
    <p>Or, do you have future goals that you are pursuing that require better study skills?</p>
    <p>IF SPECIFIC APPLICATION: How will doing your best on <span class="font-bold">[APPLICATION]</span> benefit your future?</p><br>
    <p>Caller Goals for this Session</p>
    <textarea rows="3" placeholder="Agent Notes: Caller Goals" class="w-3/4 my-3"></textarea>
    <p>How do you think better study skills specifically will help you achieve your goals?</p>
    <p class="italic">Amend Caller Goals to reflect answer.</p>
    <br>
    <p class="italic">Confirm and clarify above selections and call goals before continuing.</p>
  </div>
  <hr>
  <div class="mb-3">
    <p class="text-xl font-semibold mb-3">How are you feeling?</p>
    <p>You said that your <span class="font-bold">[APPLICATION]</span> is due in less than 24 hours, is that right?</p><br>
    <p>Could I ask how you're feeling?</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="procrastination-type" value="stressed" v-model="feeling" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Stressed/Anxious</label>
        </div>
        <div class="flex items-center">
          <input name="procrastination-type" value="relaxed" v-model="feeling" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Not Stressed/Not Anxious</label>
        </div>
      </div>
    </fieldset>
  </div>
  <hr>
  <div class="my-3" v-if="feeling === 'stressed'">
    <p class="text-xl font-semibold mb-3">Performance Reset</p>
    <p>That feeling is totally understandable.</p><br>
    <p>It’s actually evolutionary. It’s part of the “fight or flight” mechanism our nervous system evolved to keep us safe from danger. That response mechanism is useful when the response stimuli is something that puts us in physical danger, but when it comes to more cognitive tasks, when we need to be acting and thinking from a place of calm, it’s not very helpful.</p>
    <p>What we want to do right now is a simple breathing exercise to reroute your nervous system’s response away from that fight or flight response and back toward your baseline, so that you can think and act from a place of calm. That’s where you perform at your best on cognitive tasks like <span class="font-bold">[APPLICATION]</span>.</p><br>
    <p>Here's what we'll do.</p>
    <p>When you’re ready, you’ll take a deep breath in and then I’ll say “Aaaand exhale” and you’ll breath out while I count to ten. We’ll do this 5 times.</p>
    <p>Are you ready?</p><br>
    <p>Deep breath. Good.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10.</p><br>
    <p>Deep breath. Feel free to close your eyes while you’re doing this.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10.</p><br>
    <p>Deep breath. And notice your shoulders. Try to keep them relaxed.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10.</p><br>
    <p>Deep breath. Just remember that this is all part of the process of getting back to your baseline.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10.</p><br>
    <p>Deep breath. Last time.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10. </p><br>
    <p>This is a great exercise you can do whenever you’re feeling overwhelmed. Get yourself back to that baseline and ready to do your best.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="feeling === 'stressed'">
    <p class="text-xl font-semibold mb-3">Mind Reset</p>
    <p>The breathing exercise we just did can help calm us when we realize that our emotions are running high, but it’d be even better if we could intervene in that “fight or flight” mechanism before our emotions started running so high.</p><br>
    <p>I’m going to use an analogy here to help you remember what I’m about to tell you.</p>
    <p>Imagine you’re driving to school and you approach a stop sign.</p>
    <p>What does that stop sign mean? And what do you do when you see it?</p>
    <p class="font-semibold">[Allow Called to Respond]</p><br>
    <p>Exactly, just as the stop sign tells us when to be aware of our surroundings, so too, our emotions help us be more attentive to our next steps.</p>
    <p>In the analogy, the stop sign merely provides context to what you should pay attention to at that moment. It says “Stop and look.”</p>
    <p>Once you see that the way is clear, you can take your foot off the brake and keep going.</p>
    <p>In this way, your emotional response to <span class="font-bold">[APPLICATION]</span> is a signal to your brain that you need to stop, find a safe, logical way to move forward, and then get on your way.</p><br>
    <p>I am here to show you a safe way to move forward so you can do your best on <span class="font-bold">[APPLICATION]</span>.</p>
    <p>Sound good?</p>
    <p class="font-semibold">[Allow Called to Respond]</p><br>
    <p>Excellent. But in the future, if you sense emotions growing, remember that those emotions are just telling you to stop, take a breath, assess the situation for a successful path forward, and then get on your way.</p><br>
    <p>Right now what it means though is that you should focus on the tasks we are about to discuss.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Identify Goals</p>
    <p>Whenever we have a limited amount of time to prepare for something, the first thing we should immediately assess is what, out of all of the things we need to do, is the most important. What is the best, most impactful thing we can spend our time on.</p><br>
    <p>Let’s talk about <span class="font-bold">[APPLICATION]</span>. What do you think are the 3 or 4 most important things you can spend the time you have on?</p>
    <textarea rows="3" placeholder="Agent Notes: Press enter key between each task/activity" class="w-3/4 my-3"></textarea>
    <p>Great!</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Strategize</p>
    <p>Now, how many hours do you have to prepare for <span class="font-bold">[APPLICATION]</span>? Keep in mind that you need to sleep and eat and take other breaks.</p>
    <input type="number" v-model="hours" class="block mt-3 w-24 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Hours" />
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Put into Practice 1</p>
    <p>Alright.</p>
    <p>Let’s take those three or four important things you identified earlier.</p>
    <textarea rows="3" placeholder="Agent Notes" class="w-3/4 my-3"></textarea>
    <p>You have <span>{{ hours }}</span> hours in which to work on these things.</p>
    <p>I want you to get something to write with.</p>
    <p>Draw a table with 3 columns and <span>{{ Number(hours + 1) }}</span> rows.</p>
    <p>Label the first column: <span class="font-semibold">Hour</span></p>
    <p>And the second column: <span class="font-semibold">Task</span></p>
    <p>In the Hour column, number the rows 1 through <span>{{ hours }}</span>.</p>
    <p>Next, in the <span class="font-semibold">Task</span> column, I want you to write down which of the tasks you need to focus on for each hour-long session. It’s totally okay to put the same task for multiple hour-long sessions.</p>
    <p>[<span class="font-semibold">PS NOTE</span> Walk Caller through filling out the following table.]</p>
    <table class="mt-3 border">
      <thead>
        <tr>
          <td class="font-semibold p-2 border">Hour</td>
          <td class="font-semibold p-2 border">Task</td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="font-semibold p-2 border">Example</td>
          <td class="font-semibold p-2 border">Quadratics</td>
        </tr>
        <tr v-for="index in 6">
          <td class="font-semibold p-2 border">{{ index }}</td>
          <td class="p-2 border">
            <input type="text" placeholder="PS Note Field" class="w-96 text-sm">
          </td>
        </tr>
        <tr>
          <td class="font-semibold p-2 border">[etc.]</td>
          <td class="p-2 border">
            <input type="text" placeholder="PS Note Field" class="w-96 text-sm">
          </td>
        </tr>
      </tbody>
    </table>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Put into Practice 2</p>
    <p>Even though you’re working against a deadline, it’s still important to give yourself small breaks so that you can recharge and refocus, so we’re going to make a rule for these sessions.</p>
    <p>That rule is: you can only work for 45 minutes every hour.</p>
    <p>The other fifteen minutes you’ll use as a mini break or reward session.</p>
    <p>Label the third column of your table <span class="font-semibold">Break</span>. Now, let’s identify a reward or an activity that you can do as a reward and to help stay motivated.</p>
    <p>[<span class="font-semibold">PS NOTE</span> Add Caller-identified reward to the note field in the Break column.]</p>
    <table class="mt-3 border">
      <thead>
      <tr>
        <td class="font-semibold p-2 border">Hour</td>
        <td class="font-semibold p-2 border">Task (:45)</td>
        <td class="font-semibold p-2 border">Break (:15)</td>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="font-semibold p-2 border">Example</td>
        <td class="font-semibold p-2 border">Quadratics</td>
        <td class="font-semibold p-2 border">Cookie, walk</td>
      </tr>
      <tr v-for="index in 6">
        <td class="font-semibold p-2 border">{{ index }}</td>
        <td class="p-2 border">
          <input type="text" placeholder="PS Note Field" class="w-96 text-sm">
        </td>
        <td class="p-2 border">
          <input type="text" placeholder="PS Note Field" class="w-96 text-sm">
        </td>
      </tr>
      <tr>
        <td class="font-semibold p-2 border">[etc.]</td>
        <td class="p-2 border">
          <input type="text" placeholder="PS Note Field" class="w-96 text-sm">
        </td>
        <td class="p-2 border">
          <input type="text" placeholder="PS Note Field" class="w-96 text-sm">
        </td>
      </tr>
      </tbody>
    </table>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Refinement Methods</p>
    <p>[<span class="font-semibold">PS NOTE</span> Skip screen if Caller application does not require studying]</p>
    <p>As you study those topics that are most important, I want you to do two things.</p><br>
    <p>First, I want you to elaborate, out loud, as if you were teaching the topic. If you’re studying the structure of a cell, for instance, then I want you to talk through the cell’s structure as if you’re teaching it to somebody else. You can do this with the picture of the cell in front of you, or you can try to do it without a visual aide.</p>
    <p>Next, I want you to think of ways the information you’re studying might be applied in the real world.</p><br>
    <p>These two techniques can really help information be more memorable.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">How are you feeling? (2)</p>
    <p>Alright, that does it for us today. </p>
    <p>How are you feeling?</p>
    <fieldset class="mt-4">
      <div class="space-y-4 sm:items-center sm:space-y-0">
        <div class="flex items-center">
          <input name="procrastination-type" value="stressed" v-model="feeling" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Stressed / Anxious</label>
        </div>
        <div class="flex items-center">
          <input name="procrastination-type" value="relaxed" v-model="feeling" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          <label class="ml-3 block text-sm font-medium leading-6 text-gray-900">Not Stressed / Not Anxious</label>
        </div>
      </div>
    </fieldset>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="feeling === 'stressed'">
    <p>That feeling is totally understandable.</p>
    <p>It’s actually evolutionary. It’s part of the “fight or flight” mechanism our nervous system evolved to keep us safe from danger. That response mechanism is useful when the response stimuli is something that puts us in physical danger, but when it comes to more cognitive tasks, when we need to be acting and thinking from a place of calm, it’s not very helpful.</p>
    <p>What we want to do right now is a simple breathing exercise to reroute your nervous system’s response away from that fight or flight response and back toward your baseline, so that you can think and act from a place of calm. That’s where you perform at your best on cognitive tasks like <span class="font-semibold">[APPLICATION]</span>.</p>
    <p>Here’s what we’ll do.</p>
    <p>When you’re ready, you’ll take a deep breath in and then I’ll say “Aaaand exhale” and you’ll breath out while I count to ten. We’ll do this 5 times. </p>
    <p>Are you ready?</p><br>
    <p>Deep breath. Good.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10.</p><br>
    <p>Deep breath. Feel free to close your eyes while you’re doing this. </p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10.</p><br>
    <p>Deep breath. And notice your shoulders. Try to keep them relaxed.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10. </p><br>
    <p>Deep breath. Just remember that this is all part of the process of getting back to your baseline.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10. </p><br>
    <p>Deep breath. Last time.</p>
    <p>Aaaand exhale: 1-2-3-4-5-6-7-8-9-10. </p><br>
    <p>This is a great exercise you can do whenever you’re feeling overwhelmed. Get yourself back to that baseline and ready to do your best.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3" v-if="feeling === 'stressed'">
    <p class="text-xl font-semibold mb-3">Mind Reset</p>
    <p>The breathing exercise we just did can help calm us when we realize that our emotions are running high, but it’d be even better if we could intervene in that “fight or flight” mechanism before our emotions started running so high.</p>
    <p>I’m going to use an analogy here to help you remember what I’m about to tell you.</p>
    <p>Imagine you’re driving to school and you approach a stop sign.</p>
    <p>What does that stop sign mean? And what do you do when you see it?</p>
    <p class="text-red-500">[Allow Caller to respond]</p><br>
    <p>Exactly, just as the stop sign tells us when to be aware of our surroundings, so too, our emotions help us be more attentive to our next steps.</p>
    <p>In the analogy, the stop sign merely provides context to what you should pay attention to at that moment. It says “Stop and look.” </p>
    <p>Once you see that the way is clear, you can take your foot off the brake and keep going.</p><br>
    <p>In this way, your emotional response to <span class="font-semibold">[APPLICATION]</span> is a signal to your brain that you need to stop, find a safe, logical way to move forward, and then get on your way.</p>
    <p>I am here to show you a safe way to move forward so you can do your best on <span class="font-semibold">[APPLICATION]</span>.</p>
    <p>Sound good?</p>
    <p class="text-red-500">[Allow Caller to respond]</p><br>
    <p>Excellent. But in the future, if you sense emotions growing, remember that those emotions are just telling you to stop, take a breath, assess the situation for a successful path forward, and then get on your way.</p>
    <p>Right now what it means though is that you should focus on the tasks we are about to discuss.</p>
    <hr class="mt-3">
  </div>
  <div class="my-3">
    <p class="text-xl font-semibold mb-3">Summary</p>
    <p>What we did here today <span class="font-semibold">[FIRST NAME]</span> is match some evidence-based strategies to the needs of your specific <span class="font-semibold">[APPLICATION]</span>.</p>
    <p>Together, we put together a plan to help you direct your efforts toward the most important tasks you need to accomplish.</p>
    <p>[<span class="font-semibold">PS NOTE</span> Review plan below]</p>
    <img src="/images/crunch-time-table-1.png" class="w-1/2" alt="table-1">
    <p>Do you have any questions or concerns for me at this point?</p><br>
    <p>Well, <span class="font-semibold">[FIRST NAME]</span>, I would like to commend you on taking the initiative to call us. Best of luck on your <span class="font-semibold">[APPLICATION]</span>. I’m excited about your performance and wish you well in your class. </p>
    <p>Goodbye.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const feeling = ref(null)
const hours = ref(0)
</script>