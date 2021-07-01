"""A video player class."""

from src.video import Video
from .video_library import VideoLibrary



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")



    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title
        print("Here's a list of all available videos:")

        for video in all_videos:  # Loop through txt file, reading each video line by line
            tagString = str(video.tags)  # Convert to string to allow stripping of brackets
            # tagStrip.strip("()") # Old code - this didn't make a difference with this line placement
            print(video.title, "((", video.video_id, "))", "[[", tagString.strip("()"), "]]")

        # print("show_all_videos needs implementation")
        
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)

        if not video:
            print("cannot play video: Video does not exist")
            return
        if self._current_video != None:
            print(f"stopping video: {self._current_video}")
            print(f"Playing video: {video.video_id}")
            self._current_video = video.title
            return

        print(f"playing video:{video.title}")
        self._current_video = video.title

        
    def stop_video(self):
        """Stops the current video."""
        #stops current video from playing
        #print("stop_video needs implementation")

        video = self._video_library.get_video()
        if  video:
            print(f'stopping video:{video.title}')
            self._current_video = video

        else:
            print("Cannot play video: Video doesnt exist")    

        

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
