/*
We use two background gradients, for two states. Each background visibility is ruled by the background-size.

- default state: 1px silver bottom background is visible.
- focus state: 2px color bottom background is visible

The size of the background is animated with "transition". The y-size remains always the same. The x-size is changed.

- default state
  - silver background is 100% wide
  - color background is 0% wide.
- focus state
  - silver background is 0% wide
	- color background is 100% wide



Animation is solely on the background-size, making it grow from 0 to 100% on focus and shrink back to 0% on blur.

The grow/shrink goes from the center to the borders.
To make it go from/to a side, replace the "50% 100%" with "0 100%" or "100% 100%" (for left or right respectively) on the background-position.

This works on <input> and on <textarea> alike.
*/