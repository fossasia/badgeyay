import { helper } from '@ember/component/helper';

export function extractRole(user) {
  user = user[0];
  if (user.isAdmin) {
    return 'Admin';
  } else if (user.isSales) {
    return 'Sales';
  } else {
    return 'User';
  }
}

export default helper(extractRole);
