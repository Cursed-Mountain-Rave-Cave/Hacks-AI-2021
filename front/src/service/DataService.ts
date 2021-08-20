import http from './instance';
import { AxiosResponse } from 'axios';

export class DataService {
  private baseUrl = '';

  constructor(baseUrl = '/v1') {
    this.baseUrl = baseUrl;
  }

  protected get = async (url = '', data?: any): Promise<any> => {
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
