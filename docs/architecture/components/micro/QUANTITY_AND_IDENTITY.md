# Aantal, identiteit en payload — per functie vastgelegd

**Doel:** het getoonde aantal, betaalde extra's en de API-items blijven bij exact dezelfde artikelen horen. Hoofdcontracten: [keuzes/inbouw](../PRODUCT_CHOICES.md), [Sunshower-acties](SUNSHOWER_ACTIONS.md). De genoemde prijzen/ID's in de fixture zijn fictief; actuele winkelprijzen zijn niet naar het rapport gekopieerd.

## Eenheden eerst

| Waarde | Huidig contract |
| --- | --- |
| data-price / bodyPrice / price_cents | Integer centen in de frontend; display deelt door 100 |
| quantity | Positief geheel aantal, getoetst met inputconstraints en veilige integercontrole waar gebruikt |
| Variantidentiteit | Exacte variant-ID; een kleur-/titelgelijkenis is niet genoeg |
| Product/SKU-mapping | Liquid en JS hebben elk een eigen verificatielaag |
| Samengestelde items | API-items per variant, niet één vrij omschreven setregel |

Een decimaal Shopify-bedrag als string uit Admin is niet zonder omzetting dezelfde waarde als centen in data-attributen. Die conversie hoort bij de bronmapping; geen parseFloat/keer-honderd op willekeurige velden toevoegen. Zie [productdata-export](../../PRODUCT_DATA.md) voor geld-/ID-preservatie in JSONL/SQLite.

## Hotbath: validIdentity

assets/bc-product-inbouw.js:65–70 vereist data-valid == true, numerieke parent/body-ID's die verschillen, beide SKU's, het actieve form-ID gelijk aan de parentvariant en een positieve gehele quantityPerTrim. Die data-valid komt uit Liquid: exact merk, beide SKU-/variantmatches, positieve bodyprijs, niet al inbegrepen en de huidige mapping quantity == 1.

IB-01 bevestigt dat de bedoelde parent/formcombinatie geldig is, een gewijzigd actief form-ID afwijkt en dezelfde parent/bodyvariant wordt afgewezen. De test gebruikt de echte methode op een klein gecontroleerd object; de Liquid-identiteitsvalidatie is daarbij een verklaarde bovenliggende voorwaarde, geen nieuw uitgevoerde volledige Liquid-render.

## Hotbath: quantity en onzekerheid

quantity:171–179 leest het gekoppelde formuliercontrol, eist een niet-lege geldige safe integer en berekent bodyQuantity = quantity × quantityPerTrim. Een onveilige/ongeldige uitkomst geeft null.

| Geval uit IB-02 | Uitkomst |
| --- | --- |
| Aantal 2, verhouding 1 | quantity 2 en bodyQuantity 2 |
| Leeg, 0 of 2,5 bij step 1 | null, koopflow moet blokkeren |

handleSubmit consumeert de actie en stopt vroeg bij busy, uncertain, losgekoppelde component, pageLeaving of bcNavigating. IB-03 bevestigt specifiek dat een bestaande uncertain-staat de submit tegenhoudt vóór enige fetch. Dit verschilt van een gewone HTTP-fout waarna een andere handler meteen weer enabled kan worden.

Bij expliciet inbouw aan bouwt de bron twee items, controleert geretourneerde variant/SKU/hoeveelheid en navigeert pas daarna. Een timeout of onbekend antwoord is geen bewijs dat de server niets heeft toegevoegd. De bestaande uncertain-blokkade en cartcontrolelink zijn daarom een te behouden bescherming bij latere stijlharmonisatie.

## Sunshower: basisproduct en extra's tellen anders

parentQuantity gebruikt een positief veilig geheel aantal, anders displayfallback 1. Voor de echte setactie volgt eerst quantity.checkValidity; de displayfallback is dus geen toestemming om een ongeldig ingevoerd aantal te kopen.

updateTotal:332 rekent basisprijs × parentQuantity plus de som van gekozen extra's. De setpayload:358 gebruikt hetzelfde hoofdproductaantal, maar voor **iedere gekozen extra quantity 1**. SS-02 bevestigt bij twee hoofdproducten en één gekozen extra een payload van 2 + 1. Dat is het huidige codecontract, niet automatisch de gewenste commerciële setverhouding.

Voorbeeld met uitsluitend fictieve fixturebedragen: basis 10.000 cent, extra 500 cent en twee hoofdproducten geeft 20.500 cent; de extra wordt eenmaal toegevoegd. De huidige vertaling zegt “Inclusief btw · product en geselecteerde extra’s” en specificeert daar geen vermenigvuldigingsregel. Of bij twee Sunshowers ook twee installatie-accessoires nodig zijn, is een product-/UX-besluit dat niet uit de checkbox mag worden verzonnen.

Tijdens een lopend request staat de items-array al vast. De risicoanalyse van nog beschikbare kleur-/koopcontrols staat bij SS-F01; een ander getoond aantal herschrijft het verstuurde request niet.

## Grenzen van deze controle

Geen real-cart-, voorraad-, belasting-, verzending-, staffel-, tegelverpakking-, currency-/afrondings- of selling-planvrijgave. De hoeveelheidfunctie is geïsoleerd getoetst, niet iedere productfamilie. Een volgende uitbreiding moet eerst de betekenis van de eenheid en relatie bepalen en daarna de payload/teruggegeven identiteit volgen. Geen variant-ID of inbegrepen onderdeel afleiden uit alleen een titel.
