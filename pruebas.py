
# Main Game Loop
while run_game:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # GUI window will remain open until [X] button is clicked or GUI is closed.
            run_game = False

    # Create background
    win.fill(black)
    draw_texts()


    # Player passes
    if (keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]) and main_loop == 0 and session:


pygame.quit()

