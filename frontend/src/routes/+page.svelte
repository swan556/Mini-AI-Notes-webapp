<script lang="ts">
	import Note from './Note.svelte';

	let notes: { title: string; body: string }[] = [];
	let i = 0;

	

	function addNote() {
		notes = [
			...notes,
			{
				title: `nested title for note ${i}`,
				body: `this is a nested body for note ${i}`
			}
		];
		i++;
	}
</script>

<button on:click={addNote}>+</button>

{#each notes as note}
	<Note title={note.title} body={note.body} />
{/each}
