import { Component, OnInit, AfterViewInit } from '@angular/core';
import { HomeService } from "../services/home.service";
declare var jQuery: any;

@Component({
  selector: 'home-component',
  templateUrl: './home.component.html',
  providers: [HomeService],
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, AfterViewInit{
	public bcategories: any[];
	public adnames: any[];
	public isopen: boolean=false;

	constructor(private _homeservice:HomeService){}

	ngOnInit(){
		this._homeservice.AdNames().subscribe(data=>{
			this.adnames = data;
			for (var i=0; i<this.adnames.length; i++){
				var count=1;
				this.adnames[i].copy = [];
				for (var j=i+1; j<this.adnames.length && count < 6; j++){
					this.adnames[i].copy.push(this.adnames[j]);
					count++;
				}

				for (var j=0; j<this.adnames.length && count < 6; j++){
					this.adnames[i].copy.push(this.adnames[j]);
					count++;
				}
			}
		});
		this._homeservice.BCategories().subscribe(data=>{
			this.bcategories = data;
			for (var i=0; i<this.bcategories.length; i++){
				let sum = 0;
				for (var j=0; j<this.bcategories[i].bsubcategories.length; j++){
					sum+=this.bcategories[i].bsubcategories[j].bsubcategorytypies.length;
				}
				this.bcategories[i].sum = sum;
			}
		});
	}

	ngAfterViewInit(){
		setTimeout(function(){
			jQuery('#serviceslider').carousel({
				vertical: true
			});
		}, 1500);
	}

	openNav1(){
		this.isopen = true;
		jQuery('.categry_outr .categry_link').parent().toggleClass('open');
		jQuery('.categry_outr .categry_dtl').slideToggle();
	}
	closeNav1(){
		this.isopen = false;
	}
}
