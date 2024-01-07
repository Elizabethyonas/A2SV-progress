
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        
        for path in paths:
            elements = path.split()
            directory = elements[0]
            
            for file_info in elements[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]  
                file_path = directory + '/' + file_name
                content_to_paths[content].append(file_path)
        
        duplicate_files = []
        
        for paths in content_to_paths.values():
            if len(paths) > 1:
                duplicate_files.append(paths)
        
        return duplicate_files


        