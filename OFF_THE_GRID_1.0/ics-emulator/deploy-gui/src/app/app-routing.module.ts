import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ScenariosComponent } from './scenarios/scenarios.component';
import { CreatescenarioComponent } from './createscenario/createscenario.component';
import { DeviceconfigComponent } from './deviceconfig/deviceconfig.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'scenarios',
    component: ScenariosComponent
  },
  {
    path: 'createscenario',
    component: CreatescenarioComponent
  },
  {
    path: 'deviceconfig',
    component: DeviceconfigComponent
  },  
  {
    path: 'deviceconfig/:id',
    component: DeviceconfigComponent
  },
  //{
  //  path: "deviceconfig/:id",
  //  redirectTo: "/deviceconfig",
  //  pathMatch: "full"
  //},
  {
    path: 'auth',
    loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule)
  },
  { path: '**', pathMatch: 'full', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
