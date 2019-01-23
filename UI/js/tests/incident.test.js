const puppeteer = require('puppeteer');
const faker = require('faker');



let browser
let page


const incident = {
    description:faker.lorem.paragraph(),
    media:faker.image.nature()
  };

beforeEach(async () => {
    // launch browser

    browser = await puppeteer.launch()
    // creates a new page in the opened browser
    page = await browser.newPage()
})

describe('Create incident', ()=> {
    it('user can create an incident', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/useracc.html');
        
        page.on('dialog', dialog => {
            dialog.accept();})
        await page.click('button[id=createincident]');

        await page.waitForSelector('.flag-form');

        await page.click('select[id=record_type]');
        await page.select('option[id=red-flag]');

        await page.click('input[id=description]');
        await page.type('input[id=description]', incident.description);

        await page.click('input[id=location]');

        await page.click('input[id=media]');
        await page.file('input[id=media]', incident.media);

        await page.click('input[type=submit]');

    }, 9000000);
    
});

afterEach( async () => {
    await browser.close();
  });