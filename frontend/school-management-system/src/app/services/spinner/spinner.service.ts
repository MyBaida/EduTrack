import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SpinnerService {

  constructor() { }

  private _loading: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);

  public loading: Observable<boolean> = this._loading.asObservable();

  startRequest() {
    this._loading.next(true);
  }

  endRequest() {
    this._loading.next(false);
}
}
