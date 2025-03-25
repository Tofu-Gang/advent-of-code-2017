<script>
	import Intro from '$lib/components/Intro.svelte';
</script>

<Intro />

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

		:global(s) {
				text-decoration-color: #fff;
				text-decoration: line-through;
    }
</style>
