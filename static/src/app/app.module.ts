import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { appRoutes } from "./app.routes";
import { HttpModule } from '@angular/http';
import { ToastModule } from "ng2-toastr/ng2-toastr";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { FacebookModule } from "ngx-facebook";

import { AppComponent } from './app.component';
import { HomeComponent } from "./home/home.component";
import { AdDetailComponent } from "./addetail/addetail.component";
import { SliderComponent } from "./slider/slider.component";
import { LoginComponent } from "./login/login.component";
import { MainRegisterComponent } from "./register/mainregister.component";
import { IndividualComponent } from './register/individual.component';
import { BusinessComponent } from "./register/business.component";
import { AlertComponent } from "./alert/alert.component";
import { AlertService } from "./services/alert.service";
import { AuthenticationService } from "./services/authentication.service";
import { CommonService } from "./services/common.service";
import { TwitterComponent } from "./twitter/twitter.component";
import { SliderlocationComponent } from "./sliderlocation/sliderlocation.component";
import { AuthGurad } from "./guards/auth.guard";
import { LoginGurad } from "./guards/logined.guard";
import { MarketComponent } from "./topsearch/marketplace.component";
import { CheckurlPipe } from "./pipe/checkurl.pipe";
import { StoreComponent } from "./topsearch/store.component";
import { UserComponent } from "./topsearch/user.component";

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AdDetailComponent,
    SliderComponent,
    LoginComponent,
    MainRegisterComponent,
    IndividualComponent,
    BusinessComponent,
    AlertComponent,
    TwitterComponent,
    SliderlocationComponent,
    MarketComponent,
    CheckurlPipe,
    StoreComponent,
    UserComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ToastModule.forRoot(),
    appRoutes,
    FormsModule,
    FacebookModule.forRoot(),
    HttpModule
  ],
  providers: [
    AlertService,
    AuthenticationService,
    CommonService,
    AuthGurad,
    LoginGurad
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
