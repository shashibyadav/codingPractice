import copy
import json


class File:
    def __init__(self, filename, size=0, user="admin"):
        self._size = size
        self._user = user
        self._fileName = filename

    def to_json(self):
        return json.dumps(
            {"_fileName": self._fileName, "_size": self._size, "_user": self._user}
        )

    @staticmethod
    def from_json(json_string):
        file_dict = json.loads(json_string)
        return File(file_dict["_fileName"], file_dict["_size"], file_dict["_user"])

    def get_size(self):
        return self._size

    def get_user(self):
        return self._user

    def set_user(self, user):
        self._user = user

    def get_filename(self):
        return self._fileName

    def __deepcopy__(self, memodict={}):
        return File(
            copy.deepcopy(self._fileName, memodict),
            copy.deepcopy(self._size, memodict),
            copy.deepcopy(self._user, memodict),
        )


class FileSystem:
    def __init__(self):
        self.file_system_dict = dict()

    def __deepcopy__(self, memodict={}):
        obj = FileSystem()
        obj.file_system_dict = copy.deepcopy(self.file_system_dict, memodict)
        return obj

    def check_file_exists(self, name):
        if name in self.file_system_dict:
            return True
        else:
            return False

    def add_file(self, name, size, user):
        if self.check_file_exists(name):
            return False
        self.file_system_dict[name] = File(name, int(size), user)
        return True

    def get_file_size(self, name):
        if not self.check_file_exists(name):
            return ""
        return str(self.file_system_dict[name].get_size())

    def del_file(self, name):
        if not self.check_file_exists(name):
            return ""
        result = str(self.file_system_dict[name].get_size())
        del self.file_system_dict[name]
        return result

    def get_n_largest_file(self, prefix, k):
        temp_heap = []
        for item in self.file_system_dict.items():
            if item[0].startswith(prefix):
                temp_heap.append(item)
        if len(temp_heap) == 0:
            return ""
        k = int(k)

        def custom_comparision(item):
            return (-int(item[1].get_size()), item[0])

        temp_heap = sorted(temp_heap, key=custom_comparision)

        temp_string = []
        for i in range(k):
            if i > len(temp_heap) - 1:
                break
            p = temp_heap[i]
            temp_string.append(str(p[0]) + "(" + str(p[1].get_size()) + ")")
        return ",".join(temp_string)


class Backup:
    def __init__(self, user):
        self._user = copy.deepcopy(user)
        self._filesystem = dict()

    def set_filesystem(self, filesystem):
        self._filesystem = filesystem

    def get_filesystem(self):
        return self._filesystem

    def get_user(self):
        return self._user

    def backup(self, file_system):
        for key in self._user.get_files():
            self.add_file_system_obj(
                key, copy.deepcopy(file_system.file_system_dict[key])
            )

    def add_file_system_obj(self, key, value):
        self._filesystem[key] = value

    def to_json(self):
        filesystem_json = {}
        for key, value in self._filesystem.items():
            filesystem_json[key] = value.to_json()
        return json.dumps(
            {"_user": self._user.to_json(), "_filesystem": filesystem_json}
        )

    @staticmethod
    def from_json(json_string):
        backup_dict = json.loads(json_string)
        user = User.from_json(backup_dict["_user"])
        filesystem = {}
        for key, value in backup_dict["_filesystem"].items():
            filesystem[key] = File.from_json(value)
        temp = Backup(user)
        temp.set_filesystem(filesystem)
        return temp


class User:
    def __init__(self, userId, capacity):
        self._files = set()
        self._user_id = userId
        if userId == "admin":
            self._capacity = float("inf")
        else:
            self._capacity = int(capacity)

    def to_json(self):
        return json.dumps(
            {
                "_user_id": self._user_id,
                "_capacity": self._capacity,
                "_files": list(self._files),  # Convert set to list
            }
        )

    @staticmethod
    def from_json(json_string):
        user_dict = json.loads(json_string)
        user = User(user_dict["_user_id"], user_dict["_capacity"])
        user._files = set(user_dict["_files"])
        return user

    def __deepcopy__(self, memodict={}):
        obj = User(copy.deepcopy(self._user_id), copy.deepcopy(self._capacity))
        obj._files = copy.deepcopy(self._files)
        return obj

    def check_add_possible(self, size):
        remaining_capacity = self._capacity - int(size)
        if remaining_capacity < 0:
            return False
        else:
            return True

    def add_file(self, name, size):
        remaining_capacity = self._capacity - int(size)
        if remaining_capacity < 0:
            return ""
        self._capacity = remaining_capacity
        self._files.add(name)
        return self._capacity

    def del_file(self, name, file_size):
        self._capacity += int(file_size)
        self._files.remove(name)

    def get_user_id(self):
        return self._user_id

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_files(self):
        return self._files


class Users:
    def __init__(self):
        self._users = dict()
        self._users["admin"] = User("admin", float("inf"))

    def __deepcopy__(self, memodict={}):
        obj = Users()
        obj._users = copy.deepcopy(self._users)
        return obj

    def get_user(self, user_id):
        return self._users[user_id]

    def set_user(self, user_id, value):
        self._users[user_id] = value

    def add_user(self, user_id, capacity):
        if user_id in self._users:
            return False
        else:
            self._users[user_id] = User(user_id, capacity)
            return True

    def check_add_possible(self, user_id, size):
        return self._users[user_id].check_add_possible(size)

    def add_file_by(self, user_id, name, size):
        if user_id in self._users:
            success = self._users[user_id].add_file(name, size)
            if success != "":
                return str(self._users[user_id].get_capacity())
            else:
                return ""
        else:
            return ""

    def merge_users(self, user_1, user_2, file_system):
        if user_1 not in self._users or user_2 not in self._users:
            return ""
        if user_1 == user_2:
            return str(self._users[user_1].get_capacity())

        temp_mem = copy.deepcopy(self._users[user_1])
        user_1_files = temp_mem.get_files()
        isError = False
        for key in self._users[user_2].get_files():
            if key in user_1_files:
                isError = True
                break
            user_1_files.add(key)
            file_system.file_system_dict[key].set_user(user_1)

        if isError:
            return ""
        else:
            self._users[user_1] = temp_mem
            self._users[user_1].set_capacity(
                self._users[user_1].get_capacity() + self._users[user_2].get_capacity()
            )
            del self._users[user_2]
            return str(self._users[user_1].get_capacity())


# queries = [
#     ["ADD_FILE", "/dir1/dir2/file.text", "10"],
#     ["ADD_FILE", "/dir1/dir2/file.txt", "5"],
#     ["GET_FILE_SIZE", "/dir1/dir2/file.txt"],
#     ["DELETE_FILE", "/non-existing.file"],
#     ["DELETE_FILE", "/dir1/dir2/file.txt"],
#     ["GET_FILE_SIZE", "/non-existing.file"],
#     ["GET_N_LARGEST", "/", "5"],
# ]

# queries = [
#     ["ADD_FILE", "/dir/file1.text", "5"],
#     ["ADD_FILE", "/dir/file2", "20"],
#     ["ADD_FILE", "/dir/deeper/file3.mov", "9"],
#     ["GET_N_LARGEST", "/dir", "2"],
#     ["GET_N_LARGEST", "/dir/file", "3"],
#     ["GET_N_LARGEST", "/another_dir", "file.txt"],
#     ["ADD_FILE", "/big_file.mp4", "20"],
#     ["GET_N_LARGEST", "/", "2"],
# ]

# queries = [
#     ["ADD_USER", "user1", "200"],
#     ["ADD_USER", "user1", "100"],
#     ["ADD_FILE_BY", "user1", "/dir/file.med", "50"],
#     ["ADD_FILE_BY", "user1", "/file.big", "140"],
#     ["ADD_FILE_BY", "user1", "/dir/file.small", "20"],
#     ["ADD_FILE", "/dir/admin_file", "300"],
#     ["ADD_USER", "user2", "110"],
#     ["ADD_FILE_BY", "user2", "/dir/file.med", "45"],
#     ["ADD_FILE_BY", "user2", "/new_file", "50"],
#     ["MERGE_USER", "user1", "user2"],
# ]

queries = [
    ["ADD_USER", "user1", "200"],
    ["ADD_USER", "user1", "100"],
    ["ADD_FILE_BY", "user1", "/dir/file.med", "50"],
    ["ADD_FILE_BY", "user1", "/file.big", "140"],
    ["ADD_FILE_BY", "user1", "/dir/file.small", "20"],
    ["ADD_FILE", "/dir/admin_file", "300"],
    ["ADD_USER", "user2", "110"],
    ["ADD_FILE_BY", "user2", "/dir/file.med", "45"],
    ["ADD_FILE_BY", "user2", "/new_file", "50"],
    ["MERGE_USER", "user1", "user2"],
    ["BACKUP", "user1"],
]


def solution(queries):
    result = []
    user_group = Users()
    admin_user = user_group.get_user("admin")
    file_system = FileSystem()
    for item in queries:
        if item[0] == "ADD_FILE":
            admin_user.add_file(item[1], item[2])
            result.append(file_system.add_file(item[1], item[2], "admin"))
        if item[0] == "GET_FILE_SIZE":
            result.append(file_system.get_file_size(item[1]))
        if item[0] == "DELETE_FILE":
            success = file_system.del_file(item[1])
            if success != "":
                admin_user.del_file(item[1], success)
            result.append(success)
        if item[0] == "GET_N_LARGEST":
            result.append(file_system.get_n_largest_file(item[1], item[2]))
        if item[0] == "ADD_USER":
            result.append(user_group.add_user(item[1], item[2]))
        if item[0] == "ADD_FILE_BY":
            if user_group.get_user(item[1]) is None:
                result.append("")
            else:
                if user_group.check_add_possible(
                    item[1], item[3]
                ) and not file_system.check_file_exists(item[2]):
                    file_system.add_file(item[2], item[3], item[1])
                    result.append(user_group.add_file_by(item[1], item[2], item[3]))
                else:
                    result.append("")
        if item[0] == "MERGE_USER":
            result.append(user_group.merge_users(item[1], item[2], file_system))
        if item[0] == "BACKUP":
            b_obj = Backup(user_group.get_user(item[1]))
            b_obj.backup(file_system)
            backup_s = b_obj.to_json()
            new_backup = Backup.from_json(backup_s)
            # user_group.
            print(new_backup.__dict__)
    return result


# def solution(queries):
# result = []
# file_system = FileSystem()
# for item in queries:
#     if item[0] == "ADD_FILE":
#         result.append(file_system.add_file(item[1], item[2]))
#     if item[0] == "GET_FILE_SIZE":
#         result.append(file_system.get_file_size(item[1]))
#     if item[0] == "DELETE_FILE":
#         result.append(file_system.del_file(item[1]))
#     if item[0] == "GET_N_LARGEST":
#         result.append(file_system.get_n_largest_file(item[1], item[2]))
# if item[0] == "ADD_USER":
#     result.append()
# if item[0] == "ADD_USER":
#     if not check_file(user_dict, item[1]):
#         user_dict[item[1]] = dict()
#         user_total_capacity[item[1]] = int(item[2])
#         capacity_remaining[item[1]] = int(item[2])
#         result.append(True)
#     else:
#         result.append(False)
# if item[0] == "ADD_FILE_BY":
#     if not check_file(user_dict, item[1]):
#         result.append("")
#         continue
#     user_files = user_dict[item[1]]
#     if not check_file(user_files, item[2]):
#         result.append("")
#         continue
#     user_files[item[2]] = int(item[3])
#     capacity_remaining[item[1]] -= int(item[3])
#     result.append(capacity_remaining[item[1]])
# if item[0] == "MERGE_USER":
#     first = item[1]
#     second = item[2]
# if

# return result


print(solution(queries))
