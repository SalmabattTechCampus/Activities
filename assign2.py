double Fee = 10000;
double Year = 1;
double TotalFee;
double Rate = 5;
double TotalCost = 15000 + 15500 + 16000 + 16500;

System.out.println("Year   "  + " Total Fee  ");
System.out.println();

while (Year <= 14) {
    TotalFee = Fee + ((Fee * ((Year * Rate) - Rate)) / 100);
    System.out.println(Year + "  " + "       "+ TotalFee);` 
    Year++;
}

System.out.println("Total cost tuition of 4 years starting 10 years from now is " + TotalCost);