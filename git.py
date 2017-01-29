
if __name__ == '__main__':
    import os.path
    from gittools.git import Git

    base_path = os.path.dirname(os.path.realpath(__file__))
    git = Git(base_path)
    git.run()
