
from memory_storage import add_memory, delete_memory, get_memories

def main():
    print("Current memories:")
    memories = get_memories()
    print(memories)

    print("\nAdding new memory: 'I use Shram and Magnet as productivity tools'")
    add_memory("I use Shram and Magnet as productivity tools")

    print("\nUpdated memories:")
    memories = get_memories()
    print(memories)

    print("\nDeleting memory containing 'Magnet'")
    delete_memory("Magnet")

    print("\nFinal memories:")
    memories = get_memories()
    print(memories)

if __name__ == "__main__":
    main()
