<script>
		import Draggable from './Draggable.svelte';
</script>

<Draggable>
	<div class="note">
        <div class="header">
            <input type="bello" class="headerInput">
        </div>
        <div class="body">
            <textarea class="bodyInput" on:mousedown|stopPropagation
  on:touchstart|stopPropagation></textarea>
        </div>
    </div>
</Draggable>

<style>
    .note {
        min-width: 200px;
        
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