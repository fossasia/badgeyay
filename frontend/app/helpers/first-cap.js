import { helper } from '@ember/component/helper';

export function firstCap(str) {
  return str[0].charAt(0).toUpperCase() + str[0].slice(1);
}

export default helper(firstCap);
