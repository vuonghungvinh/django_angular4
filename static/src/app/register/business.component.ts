import { Component, OnInit, ViewContainerRef } from "@angular/core";
import { HomeService } from "../services/home.service";
import { RegisterService } from "../services/register.service";
import { ToastsManager } from "ng2-toastr/ng2-toastr";
import { AlertService } from "../services/alert.service";
import { Router } from "@angular/router";

@Component({
	selector: "business-component",
	templateUrl: "business.component.html",
	styleUrls: ['../login/login.component.css'],
	providers: [HomeService, RegisterService]
})

export class BusinessComponent implements OnInit{
	public countries = [
		{code: "BH", value: "Bahrain"},
		{code: "EG", value: "Egypt"},
		{code: "KW", value: "Kuwait"},
		{code: "LB", value: "Lebanon"},
		{code: "OM", value: "Oman"},
		{code: "QA", value: "Qatar"},
		{code: "SA", value: "Saudi Arabia"},
		{code: "AE", value: "United Arab Emirates"}
	];
	public validate_password: boolean = true;
	public meesage_password: string = 'here';
	public bcategories: any[];
	public cities: any[];
	constructor(
		private _homeservice: HomeService,
		private registerService: RegisterService,
		private vRef: ViewContainerRef,
		private toast: ToastsManager,
		private alert: AlertService,
		private _router: Router){
			this.toast.setRootViewContainerRef(vRef);
	}

	ngOnInit(){
		this._homeservice.BCategories().subscribe(data=>{
			this.bcategories = data;	
		});
	}

	changeCountry(country:any){
		this._homeservice.getCities(country).subscribe(data=>{
			this.cities = data;
		});
	}

	registerForm(f:any){
		let self = this;
		this.registerService.registerBusiness(f).subscribe(data=>{
			this.alert.success("Register Business success.", true);
			this._router.navigate(['login']);
		}, error=>{
			let errors =  error.json();
			let error_msg = '';
			for (let err in errors){
				for (let i=0; i<errors[err].length; i++){
					if (error_msg == ''){
						error_msg = errors[err][i];
					} else {
						error_msg += "</br>"+ errors[err][i];
					}
				}
			}
			self.toast.error(error_msg, "Error", {enableHTML: true});
		});
	}

	changepassword(f:any, password:any){
		this.validate_password = true;
		this.meesage_password = '';
		if (f.username == password){
			this.validate_password = false;
			this.meesage_password = 'Password must be different from Username! Try again.';
			return ;
		}
		if (password.length < 8){
			this.validate_password = false;
			this.meesage_password = '';
			return ;
		}
		let re = /[0-9]/;
		if(!re.test(password)) {
			this.validate_password = false;
			this.meesage_password = 'Password must contain at least one number (0-9)!';
			return;
		}
		re = /[a-z]/;
		if(!re.test(password)) {
			this.validate_password = false;
			this.meesage_password = 'Password must contain at least one lowercase letter (a-z)!';
			return ;
		}
		re = /[A-Z]/;
		if(!re.test(password)) {
			this.validate_password = false;
			this.meesage_password = 'Password must contain at least one uppercase letter (A-Z)!';
			return;
		}
	}
}