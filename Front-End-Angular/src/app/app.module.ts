import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';

import { SharedService } from './shared.service';

import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NavbarComponent } from './main/navbar/navbar.component';
import { RegisterComponent } from './main/register/register.component';
import { LoginComponent } from './main/login/login.component';
import { CommonModule } from '@angular/common';
import { AddMotoComponent } from './main/add-moto/add-moto.component'
import { GetMotoComponent } from './main/get-moto/get-moto.component'
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { MoreinfoComponent } from './main/moreinfo/moreinfo.component';
import { ProlifeComponent } from './main/prolife/prolife.component';
import { TokenInterceptorService } from './token-interceptor.service';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';


@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    NavbarComponent,
    RegisterComponent,
    LoginComponent,
    AddMotoComponent,
    GetMotoComponent,
    MoreinfoComponent,
    ProlifeComponent,
  ],
  imports: [
    FontAwesomeModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    CommonModule,
    NgbModule,
  ],
  providers: [SharedService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptorService,
      multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
