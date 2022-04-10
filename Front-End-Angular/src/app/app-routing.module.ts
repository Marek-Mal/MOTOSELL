import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main/main.component';
import { RegisterComponent } from './main/register/register.component'
import { ProlifeComponent } from './main/prolife/prolife.component'
import { LoginComponent } from './main/login/login.component'
import { GetMotoComponent } from './main/get-moto/get-moto.component'

const routes: Routes = [
  { path: '', component:MainComponent },
  { path: 'Profil', component:ProlifeComponent },
  { path: 'Zarejejstruj', component:RegisterComponent },
  { path: 'Zaloguj', component:LoginComponent },
  { path: 'Ogłoszenia', component:GetMotoComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
