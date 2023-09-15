import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment.prod';
import { ModelResultsService } from './model-results.service';
import { ModelResult, ModelState, PredictionResult } from '../interfaces/model-result';

@Injectable({
  providedIn: 'root'
})
export class ModelService {
  url: string

  constructor(private httpClient: HttpClient, private state: ModelResultsService) {
    this.url = environment.api_url
  }

  train(form: FormData) {
    return this.httpClient.post<ModelResult>(`${this.url}/train/`, form)
  }

  test(form: FormData) {
    return this.httpClient.post<ModelResult>(`${this.url}/test/`, form)
  }

  getModelState() {
    return this.httpClient.get<ModelState>(`${this.url}/state/`)
  }

  predict(transaction: any) {
    const form = new FormData()
    form.append('transaction', transaction)
    return this.httpClient.post<PredictionResult>(`${this.url}/predict/`, form)
  } 

}
