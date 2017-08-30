import { Component, OnInit, OnDestroy } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { Subscription } from "rxjs/Rx";
import { TopsearchService } from "../services/topsearch.service";

@Component({
	selector: "marketplace",
	templateUrl: "./marketplace.component.html",
	styleUrls: ['./marketplace.component.css'],
	providers: [TopsearchService]
})

export class MarketComponent implements OnInit, OnDestroy{
	public isgrid: Boolean=true;
	private subscription: Subscription;
	public adnames: any[];
    public total:number=1;
    public cur:number=1;
    private key:string = '';
    public pages:any[] = [];

	constructor(private route: ActivatedRoute,
		private _topsearchService: TopsearchService) {
     
    }

    ngOnInit(){
    	this.subscription = this.route.queryParams.subscribe(
            (queryParam: any) => {
             	let key = '';
             	if (queryParam['key']){
             		key = queryParam['key'];
             	}
             	this.getData(key, 1);
            }
        );
    }

    getData(key:string, cur:number){
        this._topsearchService.searchMarketplace(key, cur).subscribe(data=>{
            this.adnames = data['data'];
            this.key = data['key'];
            this.cur = data['current'];
            this.total = data['total'];
            this.pages = [];
            for (let i=1; i<=this.total; i++){
                this.pages.push(i);
            }
            console.log(data);
         }, errors=>{
             console.log(errors);
         });
    }

    next(){
        if (this.cur >= this.total){
            console.log("last");
            return;
        }
        this.cur++;
        this.getData(this.key, this.cur);
    }

    prev(){
        if (this.cur <= 1){
            console.log("first");
            return;
        }
        this.cur--;
        this.getData(this.key, this.cur);
    }

    selectpage(page:number){
        this.getData(this.key, page);
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
    }

	viewList(){
		this.isgrid = false;
	}

	viewGrid(){
		this.isgrid = true;
	}
}