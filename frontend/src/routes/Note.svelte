<script>
		import Draggable from './Draggable.svelte';
        let { title, body } = $props();
</script>

<Draggable>
	<div class="note">
        <div class="header">
            <input bind:value={title} class="headerInput">
        </div>
        <div class="body">
            <textarea class="bodyInput" bind:value={body} on:mousedown|stopPropagation on:touchstart|stopPropagation></textarea>
        </div>
    </div>
</Draggable>

<style>
    .note {
        min-width: 200px;
        border: 2px solid black;
        
    }
    .headerInput {
        height: 90%;
        min-width: 70%;
        background: transparent;
        border: 0px solid;
        margin-left: 5px;
    }
    .headerInput:focus {
        outline: none;
        border: 0px solid;
    }

    .header {
        height: 30px;
        background-color: yellow;
        border-bottom: 1px solid black;
    }
    .body {
        background-color: yellowgreen;
        min-height: 170px;
    }

    .bodyInput {
        background-color: transparent;
        border: 0px solid;
        min-width: 195px;
        min-height: 170px;
        margin-left: 5px;
    }

    .bodyInput:focus {
        border: 0px solid;
        outline: none;
    }
</style>