import { helper } from '@ember/component/helper';

export function ifEqual(params) {
  let [arg1, arg2] = params;
  return arg1 === arg2;
}

export default helper(ifEqual);
