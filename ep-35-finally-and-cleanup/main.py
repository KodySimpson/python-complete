"""
Episode 35: finally and Cleanup

In this episode you'll learn:
- What `finally` does and when it runs
- Using `finally` to release resources (files, locks, state)
- try/finally vs `with` (context managers)
"""

# ------------------------------------------------------------
# 1) Why finally?
# ------------------------------------------------------------
# The `finally` block always runs whether the try-block succeeds, fails,
# or even if you `return` inside try/except. Use it to release resources
# you acquired in try: close files, release locks, restore state.


# ------------------------------------------------------------
# 2) A realistic cleanup example (files)
# ------------------------------------------------------------
def demo_finally_file_cleanup():
    """Ensure a file is closed and removed even if an error occurs."""
    import os

    path = "demo_finally_output.txt"
    f = None
    print("Opening file and writing...")
    try:
        f = open(path, "w")
        f.write("Hello from demo_finally_file_cleanup()!\n")
        print("File written. Now simulating an error...")
        # Simulate an error after acquiring the resource
        raise RuntimeError("something went wrong after writing")
    except RuntimeError as e:
        print("Handled runtime error:", e)
    finally:
        # Always close the file if it was opened
        if f and not f.closed:
            f.close()
            print("File closed.")
        # Clean up the temporary file if it exists
        try:
            if os.path.exists(path):
                os.remove(path)
                print(f"Deleted temporary file: {path}")
        except Exception as cleanup_err:
            print("Warning: could not remove temporary file:", cleanup_err)
        print("Cleanup complete (finally always runs)\n")


# ------------------------------------------------------------
# 3) Restoring process state (current working directory)
# ------------------------------------------------------------
def demo_finally_restore_cwd():
    """Temporarily change directories, then restore in finally."""
    import os
    old = os.getcwd()
    print("Original cwd:", old)
    try:
        os.chdir("/")
        print("Now in:", os.getcwd())
        # Do some work here; if it fails, we still restore cwd
        # raise RuntimeError("boom")
    finally:
        os.chdir(old)
        print("Restored cwd:", os.getcwd(), "\n")


# ------------------------------------------------------------
# 4) try/finally vs with (context managers)
# ------------------------------------------------------------
def demo_with_preferred():
    """Use with-statement to handle open/close automatically."""
    try:
        with open("with_example.txt", "w") as f:
            f.write("Using with means close() happens automatically.\n")
        print("with-example written and closed.")
    finally:
        import os
        if os.path.exists("with_example.txt"):
            os.remove("with_example.txt")
            print("with-example cleaned up.\n")


# ------------------------------------------------------------
# 5) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== finally and Cleanup ===")
    demo_finally_file_cleanup()
    demo_finally_restore_cwd()
    demo_with_preferred()

    print("\n=== Try it yourself ===")
    print("1) Acquire a threading.Lock() and ensure release in finally.")
    print("2) Create a temporary directory and ensure it’s removed in finally.")
    print("3) Wrap network/socket usage: always close on error in finally.")

