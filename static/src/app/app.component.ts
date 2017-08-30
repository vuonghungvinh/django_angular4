import { Component } from '@angular/core';
import { CommonService } from "./services/common.service";
import { AuthenticationService } from "./services/authentication.service";
import { Router } from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [CommonService]
})
export class AppComponent {
	public defaulttype:string = "marketplace";
	constructor(
		public commonService: CommonService,
		public authencativeService: AuthenticationService,
		private router: Router){}

	onActivate(e, outlet){
	    document.body.scrollTop = 0;
	}

	searchForm(f:any){
		if (f['type'] == 'marketplace'){
			this.router.navigate(['/search/marketplace'], {queryParams: {key: f['key']}});
		}
		if (f['type'] == 'store'){
			this.router.navigate(['/search/store'], {queryParams: {key: f['key']}});
		}
		if (f['type'] == 'user'){
			this.router.navigate(['/search/user'], {queryParams: {key: f['key']}});
		}
	}

	logout(){
		this.authencativeService.logout();
		this.router.navigate(['/login']);
	}
}
