import pygame
import sys
from screen_manager import ScreenManager

def main():
    # Initialize pygame and the display
    try:
        pygame.init()
    except Exception as e:
        print(f"Error initializing Pygame: {e}")
        sys.exit(1)

    try:
        screen_info = pygame.display.Info()
        screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
    except Exception as e:
        print(f"Error when setting display mode: {e}")
        pygame.quit()
        sys.exit(1)
    
    
    manager = ScreenManager(screen)
    
    # Main loop
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    else:
                        manager.next_color()
                elif event.type == pygame.QUIT:
                    running = False

            
            pygame.display.flip()
        except Exception as e:
            print(f"Unexpected error during execution: {e}")
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
