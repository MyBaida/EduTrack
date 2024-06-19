import { TestBed } from '@angular/core/testing';

import { PerformaceService } from './performace.service';

describe('PerformaceService', () => {
  let service: PerformaceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PerformaceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
