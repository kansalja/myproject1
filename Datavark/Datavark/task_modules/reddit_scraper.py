import logging, praw
from datetime import datetime
from django.conf import settings as s
import pandas as pd

logger = logging.getLogger("django")


class RedditScraper:
    """
    Class to acquire the data from Reddit
    """

    def __new__(cls, args=None, kwargs={}):
        obj = super().__new__(cls)
        return obj._get_data()

    def _get_data(self):
        _root_url = s.DA_SETTINGS["data_sources"]["reddit"]["source_root_url"]
        _praw_config = s.DA_SETTINGS["data_sources"]["reddit"]["praw_config"]
        reddit = praw.Reddit(
            client_id=_praw_config["praw_client_id"],
            client_secret=_praw_config["praw_client_secret"],
            username=_praw_config["praw_username"],
            password=_praw_config["praw_password"],
            user_agent=_praw_config["praw_user_agent"],
        )
        _data = []
        _weekly_report_page_ids = []
        _all_submissions = reddit.subreddit("ufos")

        """
        Legacy: The below commented code was used to retrieve weekly sighting reports 
        by targetting their formatting on r/UFOs as it was prior to the change 
        by the subreddit administrators in January 2023.
        """

        # for i in _all_submissions.search(
        #     '"Weekly UFO Sightings:" AND - ', syntax="lucene", time_filter="week"
        # ):
        #     _weekly_report_page_ids.append(i.id)
        # for report_page_id in _weekly_report_page_ids:
        #     submission = reddit.submission(report_page_id)
        #     submission.comments.replace_more(limit=0)
        #     comments = submission.comments.list()
        #     for comment in comments:
        #         if comment.is_root:
        #             _data.append(
        #                 {
        #                     "report_link": f"{_root_url}{comment.permalink}",
        #                     "text": comment.body,
        #                     "posted": datetime.fromtimestamp(
        #                         comment.created_utc
        #                     ).strftime("%Y-%m-%dT%H:%M:%S"),
        #                 }
        #             )

        """
        Sighting reports are now formatted as new submissions (posts) 
        with the "Witness/Sighting" 'flair', as of January 2023. This is 
        targetted in the code, below.
        
        !Note: Increase the time_filter if needing to extract more than one 
        previous week's reports in one go.

        Official documentation for all search parameters are available here: 
        https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html
        """

        # get data tagged with "Witness/Sighting" flair
        for i in _all_submissions.search(
            'flair:"Witness/Sighting"', syntax="lucene", time_filter="week"
        ):
            _weekly_report_page_ids.append(i.id)

        # get data tagged with "Report" flair
        for i in _all_submissions.search(
            'flair:"Report"', syntax="lucene", time_filter="week"
        ):
            _weekly_report_page_ids.append(i.id)

        for report_page_id in _weekly_report_page_ids:
            submission = reddit.submission(report_page_id)
            if submission.selftext:
                _data.append(
                    {
                        "report_link": f"{_root_url}{submission.permalink}",
                        "text": f'"{submission.selftext}"',
                        "posted": datetime.fromtimestamp(
                            submission.created_utc
                        ).strftime("%Y-%m-%dT%H:%M:%S"),
                    }
                )
        _df = pd.DataFrame(_data)
        if not _df.empty:
            _df.to_csv(
                s.DA_SETTINGS["data_sources"]["reddit"]["data_path"], index=False
            )
            return True
        logger.warning("No new REDDIT data acquired - the download was empty.")
        return False
