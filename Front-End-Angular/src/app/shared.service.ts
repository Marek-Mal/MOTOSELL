import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = "http://192.168.88.195:8000"
  readonly PhotosUrl = "http://192.168.88.195:8000/my_media"
  
  
  constructor(private http:HttpClient) {
  }

  GetMotoList():Observable<any>{
    return this.http.get<any>(this.APIUrl + '/getposts/');
  }

  PostMotoList(val:any): Observable<any>{
    return this.http.post<any>(this.APIUrl + '/postmoto/', val)
  }

  PutMotoList(val:any): Observable<any>{
    return this.http.put<any>(this.APIUrl + '/updateposts/' + val.get('Moto_id'), val)
  }

  DeleteMotoList(val:any): Observable<any>{
    return this.http.delete(this.APIUrl + '/deleteposts/' + val)
  }

  UserMethodRegister(val:any): Observable<any> {
    return this.http.post(this.APIUrl + '/users/', val)
  }

  GetUser(): Observable<any> {
    return this.http.get(this.APIUrl + '/currentuser/')
  }

  OffersSorted(): Observable<any> {
    return this.http.get(this.APIUrl + '/sortposts/')
  }

  UserMethodLogin(val:any): Observable<any> {
    return this.http.post(this.APIUrl + '/login-rest/', val)
  }

  UserUpdate(val:any): Observable<any> {
    return this.http.put(this.APIUrl + '/updateuser/' + val.user_id, val)
  }

  UserDelete(val:any): Observable<any> {
    return this.http.delete(this.APIUrl + '/deleteuser/' + val.user_id, val)
  }

  public getToken(): any {
    return localStorage.getItem('token');
  }

}
