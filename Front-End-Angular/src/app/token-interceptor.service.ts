import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { SharedService } from './shared.service';
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {

  constructor(public service: SharedService) { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> { 
    request = request.clone({
      setHeaders: {
        Authorization: `Token ${this.service.getToken()}`
      }
    });
    return next.handle(request);
  }
}
