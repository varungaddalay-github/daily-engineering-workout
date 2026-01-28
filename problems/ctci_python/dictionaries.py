from collections import Counter, defaultdict


"""
Problem 30.1 - Account Sharing Detection
Detect if any username appears with multiple IP addresses.

Input: Array of (IP, username) tuples
Output: Any IP with a shared username, or empty string if none
Examples:

[("203.0.113.10", "mike"), ("292.0.2.5", "mike")] → "203.0.113.10" (mike appears twice)
[("111.0.0.0", "mike"), ("111.0.0.1", "mike2")] → "" (no sharing)


Constraints: Up to 10^5 connections, unique IPs, usernames 1-30 chars
"""

def connection_sharing(connections):
    seen = set()

    for ip, usr in connections:
        if usr in seen:
            return ip
        else:
            seen.add(usr)
    return ""


"""
Problem 30.2 - Most Shared Account
Find the username that appears most frequently across connections.

Input: Array of (IP, username) tuples
Output: Most frequent username (ties: return any)
Examples:

[("203.0.113.10", "mike"), ("202.0.2.5", "mike"), ("208.51.100.25", "bob")] → "mike" (appears 2x)


Constraints: Up to 10^5 connections, unique IPs

- calculate the counts
- find the max value
"""

def most_shared_account(connections):    
    freq_map = {}
    max_val = 0
    max_username = ""

    for _, usr in connections:
        freq_map[usr] = freq_map.get(usr, 0) + 1
        if freq_map[usr] > max_val:
            max_val = freq_map[usr]
            max_username = usr
    return max_username
    
connections = [("203.0.113.10", "mike"), ("202.0.2.5", "mike"), ("208.51.100.25", "bob")]
print(most_shared_account(connections))



"""
Problem 30.3 - Most Frequent Octet
Find the most common first octet (first number) in IPv4 addresses.

Input: Array of IP address strings
Output: Most frequent first octet as string
Examples:

["203.0.113.10", "203.0.113.5", "208.51.100.5"] → "203" (appears 2x)


Constraints: Up to 10^5 IPs, IPv4 format, octets 0-255

ips = ["203.0.113.10", "208.51.100.5", "202.0.2.5", "203.0.113.5"]

"""





"""
Problem 30.4 - Multi-Account Cheating
Detect if any two users have the exact same set of IP addresses.

Input: Array of (username, [IP list]) tuples
Output: Boolean - do any two users share the same IP set?
Examples:

[("bob", ["111.0.0.10", "222.0.0.5"]), ("bob2", ["222.0.0.5", "111.0.0.10"])] → True


Constraints: Up to 10^5 users, 1-10 IPs per user

"""




"""
Problem 30.5 - Domain Resolver
Implement a class managing IP→domain→subdomain mappings.

API:

register_domain(ip, domain): Associate domain with IP
register_subdomain(domain, subdomain): Add subdomain to domain
has_subdomain(ip, domain, subdomain): Check if subdomain exists


Constraints: Up to 10^5 calls per method, domains/subdomains ≤100 chars

"""


"""
Problem 30.6 - Find All Squares
Find all index pairs [i, j] where arr[i]^2 == arr[j].

Input: Array of unique integers
Output: List of [i, j] pairs (any order)
Examples:

[4, 10, 3, 100, 5, 2, 10000] → [[5, 0], [1, 3], [3, 6]] (2²=4, 10²=100, 100²=10000)


Constraints: Up to 10^6 elements, values 1 to 10^9

"""


"""
Problem 30.7 - Word Expansion Class
Check if a string can be formed by adding exactly one letter to another and reordering.

API: Checker(s) with method expands_into(s2)
Examples:

Checker("tea").expands_into("team") → True
Checker("tea").expands_into("seam") → False


Constraints: Strings up to 10^5 chars, lowercase only

"""


"""
Problem 30.8 - Cheater Detection
Find student pairs with identical wrong answers sitting next to each other.

Input: Correct answers, student array [id, desk, answers], desks per row m
Output: List of suspect student ID pairs
Examples: Students at adjacent desks in same row with same mistakes
Constraints: Up to 10^5 questions, up to 10^5 students

"""


"""
Problem 30.9 - Product of Alphabetical Sums
Check if three strings exist whose alphabetical sum product equals target.

Input: Array of 1-3 letter strings, target integer
Output: Boolean - does such a triplet exist?
Examples:

["abc", "nop"], target = 1620 → True (6 × 6 × 45 = 1620 with "abc", "abc", "nop")


Constraints: Up to 10^5 words, target ≤ 10^6

"""


"""
Problem 30.10 - Action Log Anomalies
Find tickets with anomalies (wrong open/close order, different agents, etc).

Input: Log of [agent, action, ticket_number] tuples (chronological)
Output: List of ticket numbers with anomalies
Anomalies: Closed before opened, multiple opens, different agents, agent did other work between open/close
Constraints: Up to 10^5 log entries, ticket numbers < 10^6

"""


"""
Problem 30.11 - Largest Set Intersection
Find which set to exclude to maximize intersection of remaining sets.

Input: Array of integer sets
Output: Index to exclude (smallest index in case of tie)
Examples:

[[1,2,3], [3,2,1], [1,4,5], [1,2]] → 2 (excluding index 2 gives intersection {1,2})


Constraints: Up to 10^5 sets, up to 10^5 total elements across all sets

"""
