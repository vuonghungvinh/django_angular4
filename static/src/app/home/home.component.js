"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var home_service_1 = require("../services/home.service");
var HomeComponent = (function () {
    function HomeComponent(_homeservice) {
        this._homeservice = _homeservice;
        this.isopen = false;
    }
    HomeComponent.prototype.ngOnInit = function () {
        var _this = this;
        this._homeservice.AdNames().subscribe(function (data) {
            _this.adnames = data;
            for (var i = 0; i < _this.adnames.length; i++) {
                var count = 1;
                _this.adnames[i].copy = [];
                for (var j = i + 1; j < _this.adnames.length && count < 6; j++) {
                    _this.adnames[i].copy.push(_this.adnames[j]);
                    count++;
                }
                for (var j = 0; j < _this.adnames.length && count < 6; j++) {
                    _this.adnames[i].copy.push(_this.adnames[j]);
                    count++;
                }
            }
        });
        this._homeservice.BCategories().subscribe(function (data) {
            _this.bcategories = data;
            for (var i = 0; i < _this.bcategories.length; i++) {
                var sum = 0;
                for (var j = 0; j < _this.bcategories[i].bsubcategories.length; j++) {
                    sum += _this.bcategories[i].bsubcategories[j].bsubcategorytypies.length;
                }
                _this.bcategories[i].sum = sum;
            }
        });
    };
    HomeComponent.prototype.ngAfterViewInit = function () {
        setTimeout(function () {
            jQuery('#serviceslider').carousel({
                vertical: true
            });
        }, 1500);
    };
    HomeComponent.prototype.openNav1 = function () {
        this.isopen = true;
        jQuery('.categry_outr .categry_link').parent().toggleClass('open');
        jQuery('.categry_outr .categry_dtl').slideToggle();
    };
    HomeComponent.prototype.closeNav1 = function () {
        this.isopen = false;
    };
    return HomeComponent;
}());
HomeComponent = __decorate([
    core_1.Component({
        selector: 'home-component',
        templateUrl: './home.component.html',
        providers: [home_service_1.HomeService],
        styleUrls: ['./home.component.css']
    }),
    __metadata("design:paramtypes", [home_service_1.HomeService])
], HomeComponent);
exports.HomeComponent = HomeComponent;
//# sourceMappingURL=home.component.js.map