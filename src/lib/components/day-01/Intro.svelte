<article class="day-desc">
	<h2>--- Day 1: Inverse Captcha ---</h2>
	<p>
		You're standing in a room with "digitization quarantine" written in LEDs
		along one wall. The only door is locked, but it includes a small interface.
		"Restricted Area - Strictly No Digitized Users Allowed."
	</p>
	<p>
		It goes on to explain that you may only leave by solving a <a href="https://en.wikipedia.org/wiki/CAPTCHA">captcha</a> to prove
		you're <em>not</em> a human. Apparently, you only get one millisecond to solve the
		captcha: too fast for a normal human, but it feels like hours to you.
	</p>
	<p>
		The captcha requires you to review a sequence of digits (your puzzle input)
		and find the <em>sum</em> of all digits that match the <em>next</em> digit in the list. The
		list is circular, so the digit after the last digit is the <em>first</em> digit in
		the list.
	</p>
	<p>For example:</p>
	<ul>
		<li><code>1122</code> produces a sum of <code>3</code> (<code>1</code> + <code>2</code>) because the first digit (<code>1</code>) matches the second digit and the third digit (<code>2</code>) matches the fourth digit.</li>
		<li><code>1111</code> produces <code>4</code> because each digit (all <code>1</code>) matches the next.</li>
		<li><code>1234</code> produces <code>0</code> because no digit matches the next.</li>
		<li><code>91212129</code> produces <code>9</code> because the only digit that matches the next one is the last digit, <code>9</code>.</li>
	</ul>
	<p><em>What is the solution</em> to your captcha?</p>
</article>
