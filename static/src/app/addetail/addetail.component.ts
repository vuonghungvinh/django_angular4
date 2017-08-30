import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'addetail-component',
  templateUrl: './addetail.component.html',
})
export class AdDetailComponent implements OnInit, OnDestroy{
	private subcription: any;
	public slug: any;

	constructor(private _activatedRouter: ActivatedRoute){}

	ngOnInit(){
		this.subcription = this._activatedRouter.params.subscribe(params=>{
			this.slug = params['slug'];
			console.log(params);
		});
	}

	ngOnDestroy(){
		this.subcription.unsubscribe();
	}
}
