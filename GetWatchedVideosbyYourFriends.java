class Entry{
    int freq;
    String vid;
    public Entry(int freq, String vid){
        this.freq = freq;
        this.vid = vid;
    }
    
}
class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        ArrayList<String> videos = new ArrayList<>();
        for (int i:bfs(id, level,friends)){
            videos.addAll(watchedVideos.get(i));
        }
        
        
        Map<String, Integer> map = new HashMap<>();
        for (String i:videos){
            if (map.containsKey(i)){
                int val = map.get(i);
                map.replace(i, ++val);
            }else{
                map.put(i, 1);
            }
        }
        PriorityQueue<Entry> pq = new PriorityQueue<Entry>(
        new Comparator<Entry>(){
            @Override
            public int compare(Entry e1, Entry e2){
                if(e1.freq!=e2.freq){
                    return e1.freq-e2.freq;
                }
                return e1.vid.compareTo(e2.vid);
            }
        });
        for (String key:map.keySet()){
            pq.offer(new Entry(map.get(key), key));
        }
        ArrayList<String> ans = new ArrayList<>();
        while (!pq.isEmpty()){
            ans.add(pq.poll().vid);
        }
        return ans;
        
    }
    private List<Integer> bfs(int start, int level, int[][] friends){
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.offer(start);
        
        int currentLevel = 0;
        while (!queue.isEmpty()){
            if (currentLevel >= level){
                break;
            }
            ArrayList<Integer> subqueue = new ArrayList<>(queue);
            queue = new LinkedList<>();
            for (int i:subqueue){
                visited.add(i);
                for (int j:friends[i]){
                    if (!visited.contains(j) && !queue.contains(j) && !subqueue.contains(j)){
                        queue.offer(j);
                    }
                }
            }
            currentLevel++;
        }
        return new ArrayList<Integer>(queue);
    }
}
