<script>
	import Intro from '$lib/components/Intro.svelte';
	import Day01Intro from "$lib/components/day-01/Intro.svelte"
	import Day01Solution from "$lib/components/day-01/Solution.svelte"
</script>

<Intro />
<Day01Intro />
<Day01Solution />

<style>
    :global(body) {
				background-color: #0f0f23;;
				color: #cccccc;
				font-family: "Source Code Pro", monospace;
				font-weight: 300;
				font-size: 14pt;
    }

		:global(h2) {
        display: block;
        font-size: 1em;
        margin-block-start: 0.83em;
        margin-block-end: 0.83em;
        margin-inline-start: 0;
        margin-inline-end: 0;
        font-weight: normal;
        unicode-bidi: isolate;
		}

		:global(article) {
				width: 45em;
				margin-bottom: 2em;
		}

    :global(article h2) {
				color: #ffffff;
				margin-top: 1em;
				margin-bottom: 1em;
				white-space: nowrap;
    }

		:global(article:first-of-type) {
    		margin-top: 0;
    }

		:global(article em) {
				color: #ffffff;
				font-style: normal;
				text-shadow: 0 0 5px #ffffff;
		}

		:global(article em.star) {
				color: #ffff66;
				font-style: normal;
				text-shadow: 0 0 5px #ffff66;
    }

		:global(article a) {
				white-space: nowrap;
		}

		:global(article ul) {
        list-style-type: none;
        padding: 0;
		}

		:global(article li) {
        padding-left: 2.5em;
        position: relative;
		}

    :global(article li:before) {
        content: "\00a0\00a0-\00a0";
        position: absolute;
        left: 0;
        top: 0;
    }

		:global(a) {
				text-decoration: none;
				color: #009900;
				outline: 0;
		}

		:global(s) {
				text-decoration-color: #fff;
				text-decoration: line-through;
    }

		:global(ul) {
        display: block;
        list-style-type: disc;
        margin-block-start: 1em;
        margin-block-end: 1em;
        margin-inline-start: 0;
        margin-inline-end: 0;
        padding-inline-start: 40px;
        unicode-bidi: isolate;
		}

		:global(li) {
        display: list-item;
        text-align: -webkit-match-parent;
        unicode-bidi: isolate;
		}

    :global(code) {
        position: relative;
        display: inline-block;
        margin: 0;
        padding: 0;
    }

    :global(code:before) {
        z-index: -1;
        content: "";
        position: absolute;
        display: block;
        left: -2px;
        right: -2px;
        top: 3px;
        bottom: 0;
        border: 1px solid #333340;
        background: #10101a;
    }
</style>
