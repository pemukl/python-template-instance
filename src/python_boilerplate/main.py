import os

from python_boilerplate.util import config, logger


def histring():
    return f"Your Python Boilerplate journey starts here :) (on {config.env.name})"


def main():
    # TODO your journey starts here
    logger.info(histring())
    logger.error(f"I have a secret env variable for you: {os.getenv('SECRET_KEY')}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
