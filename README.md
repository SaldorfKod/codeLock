Made by Tim Nilsson and Calle Larsen

Arduino Nano esp32 project with micropython simulating a door-lock system using buttons, led diods and a servo

Images:

On startup red led is on, simulating the door being locked:
![door_locked](https://github.com/SaldorfKod/codeLock/assets/87430118/24f4d09f-9ecd-4269-ada1-ee35bc860374)

After entering the correct code the green led lights up and servo rotates, simulating the door being opened:
![door_opened](https://github.com/SaldorfKod/codeLock/assets/87430118/ee85c23d-5f16-420a-a7b0-5b9310c64baf)

After five seconds, servo rotates back and door goes back into locked mode:
![door_locked](https://github.com/SaldorfKod/codeLock/assets/87430118/24f4d09f-9ecd-4269-ada1-ee35bc860374)

When pressing the fifth(rightmost) button, you have the possibility to change combination, simulated by the yellow led lighting up:
![alter_code_before](https://github.com/SaldorfKod/codeLock/assets/87430118/de290901-bba9-476b-b0cc-0106d5b065d4)

First you need to enter current code, after doing so the green light turns on:
![alter_code_after](https://github.com/SaldorfKod/codeLock/assets/87430118/7b421f9f-c785-4204-8781-61ea31c2bed7)

Then you enter your new code, and efter doing so the code changes and door goes back into locked mode:
![door_locked](https://github.com/SaldorfKod/codeLock/assets/87430118/24f4d09f-9ecd-4269-ada1-ee35bc860374)
