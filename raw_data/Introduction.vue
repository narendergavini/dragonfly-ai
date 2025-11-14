<template>
  <div v-if="currentStep === 1">
    <p class="mb-3 text-2xl font-semibold">Name Verification</p>
    <p>Thank you for calling DragonFly. This is {{ session.agent.firstName }}</p><br>
    <p>Before we get started, I just need to verify a few pieces of information.</p><br>
    <div>
      <p>Am I speaking with <span>
        <input type="text" v-model="session.user.firstName" class="rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
      </span>&nbsp;?
      </p>
      <fieldset class="mt-4">
        <div class="space-y-4 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
          <div v-for="option in options" :key="option.id" class="flex items-center">
            <input :id="option.id" name="client-verify" :value="option.id" v-model="verify" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
            <label :for="option.id" class="ml-3 block text-sm font-medium leading-6 text-gray-900">{{ option.title }}</label>
          </div>
        </div>
      </fieldset>
    </div>
    <div v-if="showSubStep === 'nameChange'" class="mt-3">
      <p>Oh, I'm sorry. Who am I speaking with today? (Edit First Name)</p>
      <div class="flex mt-3">
        <button type="button" @click="nextStep" class="ml-auto rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Next</button>
      </div>
    </div>
    <div v-if="showSubStep === 'namePreference'" class="mt-3">
      <p>And do you prefer to be called {{ session.user.firstName }}? (If 'NO' Edit First Name)</p>
      <div class="flex mt-3">
        <button type="button" @click="nextStep" class="ml-auto rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Next</button>
      </div>
    </div>
  </div>
  <div v-if="currentStep === 2">
    <p class="mb-3 text-2xl font-semibold">Sub-Solution Verification</p>
    <p>Hi {{ session.user.firstName }}, Like I said, my name is {{ session.agent.firstName }}. I will be your performance specialist today.</p><br>
    <div>
      <p>I see you are calling about
        <span>
          <select id="solution-suite" v-model="selectedSolution" class="rounded-md border-0 py-1.5 pl-3 pr-10 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-indigo-600 sm:text-sm sm:leading-6">
            <option v-for="solution in solutions" :value="solution._id" :selected="selectedSolution === solution._id">{{ solution.solution }}</option>
          </select>
        </span>
        . Is that right?</p>
      <fieldset class="mt-4">
        <div class="space-y-4 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
          <div v-for="option in options" :key="option.id" class="flex items-center">
            <input :id="option.id" name="client-verify" :value="option.id" v-model="verify" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
            <label :for="option.id" class="ml-3 block text-sm font-medium leading-6 text-gray-900">{{ option.title }}</label>
          </div>
        </div>
      </fieldset>
    </div>
    <div v-if="showSubStep === 'reviewSolutions'" class="mt-3">
      <p>[Review sub-solution options using the dropdown menu and select the appropriate call option]</p>
      <div class="flex mt-3">
        <button type="button" @click="nextStep" class="ml-auto rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Next</button>
      </div>
    </div>
  </div>
  <div v-if="currentStep === 3">
    <p class="mb-3 text-2xl font-semibold">Call History</p>
    <div>
      <p>Have you called DragonFly Before, or is this your first Time?</p><br>
      <fieldset>
        <div class="space-y-4 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
          <div v-for="option in callHistoryOptions" :key="option.id" class="flex items-center">
            <input :id="option.id" name="client-verify" :value="option.id" v-model="verify" type="radio" class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600" />
            <label :for="option.id" class="ml-3 block text-sm font-medium leading-6 text-gray-900">{{ option.title }}</label>
          </div>
        </div>
      </fieldset>
    </div>
    <div v-if="showSubStep === 'firstCall'" class="mt-5">
      <p>Oh that's exciting! Since you haven't called us before, I'm going to walk you through our call process very briefly and then we'll get started.</p><br>
      <p>At Dragonfly, we work with students and professionals to tackle performance challenges in real time. That means our aim today is to help you get the ball rolling on whatever it is you’re calling about. This session will last about 22 minutes, it’s going to be conversational, and when it’s over you’re going to walk away with some evidence-based techniques you can begin implementing right away.</p><br>
      <p>While I’ll be a sort of coach for our conversation, remember that you’re in charge here and that my role is to support you. </p><br>
      <p>If it ever seems like I’ve misunderstood or misinterpreted something you’ve said, please correct me. That way we can be sure that the evidence-based actions we go over during the second half of our conversation are relevant to your situation.</p><br>
      <p>Would you like to get started?</p>
      <div class="flex">
        <button type="button" @click="loadCallScript" class="ml-auto rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Next</button>
      </div>
    </div>
    <div v-if="showSubStep === 'repeatCall'" class="mt-5">
      <p>That’s great! I won’t spend much time reviewing our process then, but just a reminder that our session will last about 22 minutes, and I’ll start off by asking you a few questions just to establish where you’re at and where you’d like to be, and then we’ll jump into the skill building part of the call.</p><br>
      <p>Ready to get started?</p>
      <div class="flex">
        <button type="button" @click="loadCallScript" class="ml-auto rounded-md bg-indigo-600 px-2.5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import SolutionService from "../../services/SolutionService.js";

const currentStep = ref(1)

const props = defineProps(['session'])
const emits = defineEmits(['loadScript'])

const verify = ref(null)
const showSubStep = ref(null)
const solutions = ref(null)
const selectedSolution = ref(null)
const selectedSubSolution = ref(null)

const options = [
  { id: 'yes', title: 'YES' },
  { id: 'no', title: 'NO' }
]
const callHistoryOptions = [
  { id: 'yes', title: 'First Time Caller' },
  { id: 'no', title: 'Repeat Caller' }
]

watch(() => verify.value, () => {
  if (verify.value !== null) {
    if (verify.value === 'yes') {
      if (currentStep.value === 1) {
        showSubStep.value = 'namePreference'
      } else if (currentStep.value === 2) {
        nextStep()
      } else {
        showSubStep.value = 'firstCall'
      }
    } else {
      if (currentStep.value === 1) {
        showSubStep.value = 'nameChange'
      } else if (currentStep.value === 2) {
        showSubStep.value = 'reviewSolutions'
      } else {
        showSubStep.value = 'repeatCall'
      }
    }
  }
})

function nextStep() {
  currentStep.value = currentStep.value + 1
  verify.value = null
  showSubStep.value = null
}

function loadCallScript() {
  let scriptName = props.session.solutionSuite.subSolutions.filter(item => item._id === selectedSolution.value)[0].solution
  scriptName = scriptName.toLowerCase().replace(' ', '-')
  emits('loadScript', scriptName)
}

onMounted(async () => {
  solutions.value = props.session.solutionSuite.subSolutions
  selectedSolution.value = props.session.subSolutionID
  // let preSelectedSolution = solutions.value.filter(item => item._id === props.session.)
})

</script>