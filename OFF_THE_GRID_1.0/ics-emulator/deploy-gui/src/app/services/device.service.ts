import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Http, Response, Headers, URLSearchParams, RequestOptions } from '@angular/http';
import { map } from 'rxjs/operators';

//import { Observable } from 'rxjs';
//import 'rxjs/add/operator/map';
//import 'rxjs/add/operator/catch';
//import { catchError } from 'rxjs/operators'; 


@Injectable({
  providedIn: 'root'
})
export class DeviceService {
  constructor(
    //private _http: HttpClient, 
    private _http:Http,
  ) {}

  baseUrl = `http://localhost:3000`;

  getDevicesList() {
    return this._http.get(`${this.baseUrl}/get-devices`);
  }

  getDevicesListByproject(id) {
    return this._http.get(`${this.baseUrl}/get-device-by-id/${id}`);
  }

  getFlowJsonFile(projectid) {
    console.log("in service projectid is" + projectid);
    return this._http.get(`${this.baseUrl}/get-flows/${projectid}`);
  }

  createDevice(device) {
        let bodyString = JSON.stringify(device); // Stringify payload
        let headers      = new Headers({ 'Content-Type': 'application/json' }); // ... Set content type to JSON
        let options       = new RequestOptions({ headers: headers }); // Create a request option

        this._http.post(`${this.baseUrl}/add-device`, device, options) // ...using post request
                         .pipe(map(res => res.json())) // ...and calling .json() on the response to return data
                         .subscribe();
   
  }

  }
