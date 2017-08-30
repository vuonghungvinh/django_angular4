import { Routes, RouterModule } from "@angular/router";
import { HomeComponent } from "./home/home.component";
import { AdDetailComponent } from "./addetail/addetail.component";
import { LoginComponent } from "./login/login.component";
import { MainRegisterComponent } from "./register/mainregister.component";
import { IndividualComponent } from './register/individual.component';
import { BusinessComponent } from "./register/business.component";
import { TwitterComponent } from "./twitter/twitter.component";
import { AuthGurad } from './guards/auth.guard';
import { LoginGurad } from './guards/logined.guard';
import { MarketComponent } from "./topsearch/marketplace.component";
import { StoreComponent } from "./topsearch/store.component";
import { UserComponent } from "./topsearch/user.component";

const routing: Routes = [
	// {path: "", component: HomeComponent, canActivate: [AuthGurad]},
	{path: "", component: HomeComponent},
	{path: "ad-detail/:slug", component: AdDetailComponent},
	{path: "twitter", component: TwitterComponent},
	{path: "login", component: LoginComponent, canActivate: [LoginGurad]},
	{path: "register", component: MainRegisterComponent, canActivate: [LoginGurad]},
	{path: "register/individual", component: IndividualComponent, canActivate: [LoginGurad]},
	{path: "register/business", component: BusinessComponent, canActivate: [LoginGurad]},
	{path: "search/marketplace", component: MarketComponent},
	{path: "search/store", component: StoreComponent},
	{path: "search/user", component: UserComponent},
	{ path: '**', redirectTo: '' }
]

export const appRoutes = RouterModule.forRoot(routing)