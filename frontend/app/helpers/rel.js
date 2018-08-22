import { helper } from '@ember/component/helper';

export function rel(params) {
  var [font_size] = params;
  var iFont = parseInt(font_size);
  if (iFont <= 10) {
    return (iFont * 2.7).toString();
  }
  return (iFont * 2.15).toString();
}

export default helper(rel);
