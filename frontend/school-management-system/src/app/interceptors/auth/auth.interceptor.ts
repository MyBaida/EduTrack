import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

@Injectable()
export class authInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, handler: HttpHandler): Observable<HttpEvent<any>> {
    const newRequest = req.clone({
      setHeaders: {
        Authorization: `Bearer ${localStorage.getItem('token') || ''}`,
      }
    })
    return handler.handle(newRequest);
  }
}