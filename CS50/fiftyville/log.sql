-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Ok let's start by looking at crime description using date and street of our actual crime
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Description: Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery.
-- Littering took place at 16:36. No known witnesses.

-- Let's now listen to the witnesses using interviews table
SELECT name, transcript FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- Ruth
-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot,
-- you might want to look for cars that left the parking lot in that time frame.

-- Eugene
-- I don't know the thief's name, but it was someone I recognized.
-- Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- Raymond
-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- Ok let's see bakery_security_logs table for cars leaving the log within 10 minutes after 10:15am
SELECT activity, license_plate FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <=25;

-- +----------+---------------+
-- | activity | license_plate |
-- +----------+---------------+
-- | exit     | 5P2BI95       |
-- | exit     | 94KL13X       |
-- | exit     | 6P58WS2       |
-- | exit     | 4328GD8       |
-- | exit     | G412CB7       |
-- | exit     | L93JTIZ       |
-- | exit     | 322W7JE       |
-- | exit     | 0NTHK55       |
-- +----------+---------------+

-- Ok now, let's read data from ATM on Leggett Street
SELECT account_number, amount FROM atm_transactions
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- +----------------+--------+
-- | account_number | amount |
-- +----------------+--------+
-- | 28500762       | 48     |
-- | 28296815       | 20     |
-- | 76054385       | 60     |
-- | 49610011       | 50     |
-- | 16153065       | 80     |
-- | 25506511       | 20     |
-- | 81061156       | 30     |
-- | 26013199       | 35     |
-- +----------------+--------+

-- Now let's find a phone call with duration less than a minute.
SELECT caller, receiver FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- +----------------+----------------+
-- |     caller     |    receiver    |
-- +----------------+----------------+
-- | (130) 555-0289 | (996) 555-8899 |
-- | (499) 555-9472 | (892) 555-8872 |
-- | (367) 555-5533 | (375) 555-8161 |
-- | (499) 555-9472 | (717) 555-1342 |
-- | (286) 555-6063 | (676) 555-6554 |
-- | (770) 555-1861 | (725) 555-3243 |
-- | (031) 555-6622 | (910) 555-3251 |
-- | (826) 555-1652 | (066) 555-9701 |
-- | (338) 555-6650 | (704) 555-2131 |
-- +----------------+----------------+

-- Let's now see what is the earliest flight time from Fiftyville tomorow and where does it go.
SELECT city, full_name, abbreviation, hour, minute FROM airports, flights
WHERE origin_airport_id IN (
    SELECT id FROM airports WHERE city = 'Fiftyville'
)
AND year = 2021 AND month = 7 AND day = 29
AND destination_airport_id = airports.id ORDER BY hour ASC;

-- +---------------+-------------------------------------+--------------+------+--------+
-- |     city      |              full_name              | abbreviation | hour | minute |
-- +---------------+-------------------------------------+--------------+------+--------+
-- | New York City | LaGuardia Airport                   | LGA          | 8    | 20     |
-- | Chicago       | O'Hare International Airport        | ORD          | 9    | 30     |
-- | San Francisco | San Francisco International Airport | SFO          | 12   | 15     |
-- | Tokyo         | Tokyo International Airport         | HND          | 15   | 20     |
-- | Boston        | Logan International Airport         | BOS          | 16   | 0      |
-- +---------------+-------------------------------------+--------------+------+--------+

-- Now I want to get a list of pasport numbers of all the passengers flying to New York City.
SELECT passport_number FROM passengers
WHERE flight_id IN (
    SELECT id FROM flights
    WHERE origin_airport_id IN (
        SELECT id FROM airports WHERE city = 'Fiftyville'
    )
    AND destination_airport_id IN (
        SELECT id FROM airports WHERE abbreviation = 'LGA'
    )
    AND year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20
);

-- +-----------------+
-- | passport_number |
-- +-----------------+
-- | 7214083635      |
-- | 1695452385      |
-- | 5773159633      |
-- | 1540955065      |
-- | 8294398571      |
-- | 1988161715      |
-- | 9878712108      |
-- | 8496433585      |
-- +-----------------+

-- So now with all the collected data I should find to which passenger does this data match.
-- So far I have: License_plates, phone_numbers, account_numbers and passport_numbers.
SELECT name FROM people, bank_accounts
WHERE bank_accounts.person_id = people.id
AND phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
)
AND passport_number IN (
    SELECT passport_number FROM passengers
    WHERE flight_id IN (
        SELECT id FROM flights
        WHERE origin_airport_id IN (
            SELECT id FROM airports WHERE city = 'Fiftyville'
        )
        AND destination_airport_id IN (
            SELECT id FROM airports WHERE abbreviation = 'LGA'
        )
        AND year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20
    )
)
AND license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <=25
)
AND account_number IN (
    SELECT account_number FROM atm_transactions
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
);

-- So the thief is Bruce.
-- He escaped to New York City

-- Now let's see who is his accomplice using phone_numbers table
SELECT name FROM people
WHERE phone_number IN (
    SELECT receiver FROM phone_calls
    WHERE caller IN (
        SELECT phone_number FROM people WHERE name = 'Bruce'
    )
    AND year = 2021 AND month = 7 AND day = 28 AND duration < 60
);

-- So his accomplice was Robin