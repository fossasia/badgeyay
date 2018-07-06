import { helper } from '@ember/component/helper';

export function sanitizeDate(date) {
  return new Date(date).toDateString();
}

export default helper(sanitizeDate);
