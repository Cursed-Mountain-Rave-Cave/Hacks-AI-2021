import http from './instance';
import { AxiosResponse } from 'axios';

export class DataService {
  private baseUrl = '';

  constructor(baseUrl = '') {
    this.baseUrl = baseUrl;
  }

  public get = async (url = '', data?: any): Promise<any> => {
    console.log(data)
    try {
      const response: AxiosResponse<any> = await http.get(`${this.baseUrl}/${url}`, {
        params: data
      });
      return response.data;
    } catch (e) {
      if (e.response) {
        console.error('e.response');
      }
    }
  };
}
