import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule, FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { NgZorroAntdModule, NZ_I18N, en_US } from 'ng-zorro-antd';
import { IconsProviderModule } from './icons-provider.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';
import { HttpClientModule } from '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ScenariosComponent } from './scenarios/scenarios.component';
import { CreatescenarioComponent } from './createscenario/createscenario.component';
import { DeviceconfigComponent } from './deviceconfig/deviceconfig.component';
import { HttpModule } from '@angular/http';

registerLocaleData(en);

@NgModule({
  declarations: [AppComponent, DashboardComponent, ScenariosComponent, CreatescenarioComponent, DeviceconfigComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    IconsProviderModule,
    NgZorroAntdModule,
    ReactiveFormsModule,
    NgbModule,
    FormsModule,
    HttpModule,
    ReactiveFormsModule
  ],
  providers: [{ provide: NZ_I18N, useValue: en_US }, FormBuilder],
  bootstrap: [AppComponent]
})
export class AppModule {}
