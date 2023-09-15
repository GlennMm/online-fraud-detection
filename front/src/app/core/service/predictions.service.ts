import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
    providedIn: 'root'
})
export class PredictionsService {
    
    base_url = 'http://localhost:8000/api'
    
    constructor(private http: HttpClient) {}
    
    predictOne(form: FormData){
        return this.http.post(`${this.base_url}/predict/`, form)
    }

    predict_batch(form: FormData) {
      return this.http.post(`${this.base_url}/predict/batch`, form)
    }

}