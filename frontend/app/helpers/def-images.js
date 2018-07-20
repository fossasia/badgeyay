import { helper } from '@ember/component/helper';

export function defImages(params) {
  var [imageName] = params;
  imageName = imageName.split('_');
  for (var i = imageName.length - 1; i >= 0; i--) {
    imageName[i] = imageName[i].charAt(0).toUpperCase() + imageName[i].slice(1);
  }
  return imageName.join(' ');
}

export default helper(defImages);
