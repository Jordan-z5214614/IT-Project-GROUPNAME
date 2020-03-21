import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NoderedService {
  constructor(private _http: HttpClient) {}

  baseUrl = `http://localhost:8000`;

  getProjectsList() {
    return this._http.get(`${this.baseUrl}/listprojects`);
  }

  getProjectsMetaData() {
    return this._http.get(`${this.baseUrl}/projects-metadata`);
  }
}
