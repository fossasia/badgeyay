import { helper } from '@ember/component/helper';

export function increment(index) {
  return parseInt(index) + 1;
}

export default helper(increment);
