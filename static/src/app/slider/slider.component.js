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
var SliderComponent = (function () {
    function SliderComponent() {
    }
    SliderComponent.prototype.ngOnInit = function () {
    };
    SliderComponent.prototype.ngAfterViewInit = function () {
        var _this = this;
        this.things.changes.subscribe(function (t) {
            _this.renderComplete();
        });
    };
    SliderComponent.prototype.renderComplete = function () {
    };
    return SliderComponent;
}());
__decorate([
    core_1.Input('adnames'),
    __metadata("design:type", Array)
], SliderComponent.prototype, "adnames", void 0);
__decorate([
    core_1.Input('text1'),
    __metadata("design:type", String)
], SliderComponent.prototype, "text1", void 0);
__decorate([
    core_1.Input('text2'),
    __metadata("design:type", String)
], SliderComponent.prototype, "text2", void 0);
__decorate([
    core_1.ViewChildren('allTheseThings'),
    __metadata("design:type", core_1.QueryList)
], SliderComponent.prototype, "things", void 0);
SliderComponent = __decorate([
    core_1.Component({
        selector: "slider-component",
        templateUrl: "./slider.component.html"
    })
], SliderComponent);
exports.SliderComponent = SliderComponent;
//# sourceMappingURL=slider.component.js.map