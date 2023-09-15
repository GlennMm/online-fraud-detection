import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { of } from 'rxjs';
import { ModelResult } from '../interfaces/model-result';

@Injectable({
  providedIn: 'root'
})
export class ModelResultsService {

  training_result: ModelResult
  test_result: ModelResult
  model_state = of(false)

  constructor() { }

  public state(): Observable<boolean> {
    return this.model_state
  }

  public set_state(v: boolean) {
    this.model_state = of(v)
  }

}
