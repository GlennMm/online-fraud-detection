import { TestBed } from '@angular/core/testing';

import { ModelResultsService } from './model-results.service';

describe('ModelResultsService', () => {
  let service: ModelResultsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ModelResultsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
