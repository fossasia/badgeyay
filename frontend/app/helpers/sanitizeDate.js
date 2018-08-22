import { helper } from '@ember/component/helper';

export function sanitizeDate(date) {
  return new Date(date).toLocaleString();
}

export default helper(sanitizeDate);
