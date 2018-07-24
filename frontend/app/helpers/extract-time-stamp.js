import { helper } from '@ember/component/helper';

export function extractTimeStamp(date) {
  return Math.floor((new Date(date)).getTime() / 100);
}

export default helper(extractTimeStamp);
