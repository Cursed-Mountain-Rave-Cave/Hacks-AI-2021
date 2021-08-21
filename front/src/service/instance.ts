import axios from 'axios';
import { stringify } from 'qs';

export default axios.create({
  baseURL: 'http://localhost:4100/',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  },
  proxy: false,
  // eslint-disable-next-line
  paramsSerializer: (params: any) => {
    return stringify(params, { arrayFormat: 'repeat' });
  }
});
