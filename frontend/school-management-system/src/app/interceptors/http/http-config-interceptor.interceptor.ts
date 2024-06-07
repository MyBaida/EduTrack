
import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { finalize } from 'rxjs/operators';

@Injectable()
export class HttpConfigInterceptor implements HttpInterceptor {
  public loadingSubject = new Subject<boolean>();

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    this.loadingSubject.next(true);
    return next.handle(req).pipe(
      finalize(() => this.loadingSubject.next(false))
    );
  }
}