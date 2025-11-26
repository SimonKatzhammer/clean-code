package ubConferenceCenter;

import java.util.ArrayList;
import java.util.List;

/* 
public enum CatalogItem {
    SMALL_ROOM(100, .05), 
    LARGE_ROOM(150, .05),                
    PROJECTOR(50, .05), 
    COFFEE(10, 0), 
    COOKIES(15, 0)

    private int unitPrice;
    private double taxRate;

    public enum CatalogItem () {
        this.unitPrice = unitPrice;
        this.taxRate = taxRate;
    }
}
 */




public class Statement {

  public enum CatalogItem {SMALL_ROOM, LARGE_ROOM,
                           PROJECTOR, COFFEE, COOKIES}

  public record RentalItem(CatalogItem type,
                           int days,
                           int unitPrice,
                           int price,
                           int tax) {
  }

  public record Totals(int subtotal, int tax) {
  }

  private String customerName;
  private int subtotal = 0;
  private int tax = 0;
  private List<RentalItem> items = new ArrayList<>();

  public Statement(String customerName) {
    this.customerName = customerName;
  }

  //extract method refactoring 

  public void rentCostsPerDay(CatalogItem item, int days) {
    int unitPrice = switch (item) {
      case SMALL_ROOM -> 100;
      case LARGE_ROOM -> 150;
      case PROJECTOR -> 50;
      case COFFEE -> 10;
      case COOKIES -> 15;
    };

    public void rentCostsPerDay(CatalogItem item, int days) {
        costs = calculateBaseCosts(item.unitPrice * days);
        costs *= eligibleForDiscount(item, days);
        tax = calculateTaxCosts(item, days)


    // my new extracted methods code:
    double eligibleForDiscount(CatalogItem item, int days) {
        if item.is(SMALL_ROOM, LARGE_ROOM) & days >= 5 {
            return 0.90
        }
        else return 1.0

    int calculateBaseCosts(CatalogItem item, int days){
        return item.unitPrice * days;
    }

    double calculateTaxCosts(item, days){
        return item.taxRate * days;
    }

    // -> a bit more orderly than that:

    }= switch (item) {
      case SMALL_ROOM, LARGE_ROOM -> days == 5;
      case PROJECTOR, COFFEE, COOKIES-> false;
    };


    int price = unitPrice * days;



    if (eligibleForDiscount) price = (int) Math.round(price * .9);


    subtotal += price;
    int thisTax = switch (item) {
      case SMALL_ROOM, LARGE_ROOM, PROJECTOR ->
           (int) Math.round(price * .05);
      case COFFEE,COOKIES -> 0;
    };
    tax += thisTax;
    items.add(new RentalItem(item, days, unitPrice, price, thisTax));
  }


  public RentalItem[] getItems() {
    List<RentalItem> items = new ArrayList<>(this.items);
    boolean largeRoomFiveDays = items.stream().anyMatch(
      item -> item.type() == CatalogItem.LARGE_ROOM && item.days() == 5);
    boolean coffeeFiveDays = items.stream().anyMatch(
      item -> item.type() == CatalogItem.COFFEE && item.days() == 5);
    if (largeRoomFiveDays && coffeeFiveDays)
      items.add(new RentalItem(CatalogItem.COOKIES, 5, 0, 0, 0));
    return items.toArray(new RentalItem[0]);
  }


  public String getCustomerName() {
    return customerName;
  }


  public Totals getTotalCosts() {
    return new Totals(subtotal, tax);
  }
}