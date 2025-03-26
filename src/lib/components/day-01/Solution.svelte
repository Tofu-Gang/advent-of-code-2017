<script lang="ts">
  import input from "./input";

  const RADIUS = 5;
  let index: number = $state(0);
  let sum: number = $state(0);

  function getInputNumberLeft(offset: number): number | undefined {
    return Number(input[index - RADIUS + offset]);
  }

  function getInputNumberRight(offset: number): number | undefined {
    return Number(input[index + 1 + RADIUS - offset]);
  }
</script>

<p class="ascii-art">
██████╗ ██╗ ██████╗ ██╗████████╗██╗███████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║██╔════╝ ██║╚══██╔══╝██║╚══███╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║  ██║██║██║  ███╗██║   ██║   ██║  ███╔╝ ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██║  ██║██║██║   ██║██║   ██║   ██║ ███╔╝  ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║╚██████╔╝██║   ██║   ██║███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝


 ██████╗ ██╗   ██╗ █████╗ ██████╗  █████╗ ███╗   ██╗████████╗██╗███╗   ██╗███████╗
██╔═══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝
██║   ██║██║   ██║███████║██████╔╝███████║██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗
██║▄▄ ██║██║   ██║██╔══██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝
╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║  ██║██║ ╚████║   ██║   ██║██║ ╚████║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝
    ▀▀
</p>

<p>
  {#each Array.from(Array(RADIUS).keys()).slice(1) as i (i)}
    <span style="color: rgba(var(--font-color), {i * 0.2})">{`${getInputNumberLeft(i) ? getInputNumberLeft(i) : ""} `}</span>
  {/each}
  <span style="color: {input[index] === input[index + 1] ? 'green' : 'red'}">{`${input[index] ? input[index] : ""} `}</span>
  <span style="color: {input[index] === input[index + 1] ? 'green' : 'red'}">{`${input[index + 1] ? input[index + 1] : input[0]} `}</span>
  {#each Array.from(Array(RADIUS).keys()).slice(1).reverse() as i (i)}
    <span style="color: rgba(var(--font-color), {i * 0.2})">{`${getInputNumberRight(i) ? getInputNumberRight(i) : ""} `}</span>
  {/each}
</p>

<button onclick={() => {
  if(index < input.length) {
    sum += (input[index] === input[index + 1] ? Number(input[index]) : 0);
    index++;
  } else if(index === input.length) {
    sum += (input[index] === input[0] ? Number(input[index]) : 0);
  }
}}>
  Sum: {sum}
</button>

<p>Comparisons left: {input.length - index}</p>

<style>
	.ascii-art {
    color: #ffff66;
    font-style: normal;
    text-shadow: 0 0 80px #ffff66;
		font-size: 10pt;
		font-family: ui-monospace, monospace;
		white-space: pre;
	}
</style>
