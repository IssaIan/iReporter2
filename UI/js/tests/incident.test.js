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

describe('All incidents', () => {
    it('user can view all incidents', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/useracc.html');
        page.on('dialog', dialog => {
            expect(dialog.mesage()).toBe('Records returned successfully')
            dialog.accept();});

    })
})

describe('Create incident', ()=> {
    it('user can create an incident', async () =>{
        await page.goto('https://issaian.github.io/iReporter2/UI/useracc.html');
        page.on('dialog', dialog => {
            dialog.accept();});
        await page.click('button[id=createincident]');

        await page.waitForSelector('.flag-form');

        await page.click('input[id=description]');
        await page.type('input[id=description]', incident.description);

        await page.click('input[id=location]');

        await page.click('button[id=post]');

    }, 9000000);
    
});

afterEach( async () => {
    await browser.close();
  });