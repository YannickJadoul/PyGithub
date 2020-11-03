# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Yannick Jadoul <yannick.jadoul@belgacom.net>                  #
# Copyright 2020 Jacek Pliszka <JacekPliszka@github>                           #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import github.GithubObject


class Artifact(github.GithubObject.CompletableGithubObject):
    """
    This class represents Artifacts. The reference can be found here https://developer.github.com/v3/actions/artifacts/
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def node_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def size_in_bytes(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._size_in_bytes)
        return self._size_in_bytes.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def archive_download_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._archive_download_url)
        return self._archive_download_url.value

    @property
    def expired(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._expired)
        return self._expired.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def expires_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._expires_at)
        return self._expires_at.value

    def download(self, archive_format="zip"):
        """
        :calls: `/repos/:owner/:repo/actions/artifacts/:artifact_id/:archive_format <https://developer.github.com/v3/actions/artifacts/#download-an-artifact>`_
        :rtype: namedtuple with filename and content members
        """
        headers, data = self._requester.requestMultipartBinaryAndCheck(
            "GET", self.url + "/" + archive_format
        )
        if headers.get("status") == "302 Found" and "location" in headers:
            headers, data = self._requester.requestMultipartBinaryAndCheck(
                "GET", headers["location"]
            )

        return data

    def delete(self):
        """
        :calls: `DELETE /repos/:owner/:repo/actions/artifacts/:artifact_id <https://developer.github.com/v3/actions/artifacts/#delete-an-artifact>`_
        :rtype: bool
        """
        status, headers, data = self._requester.requestJson(
            "DELETE", self.url
        )
        return status == 204

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._node_id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._size_in_bytes = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._archive_download_url = github.GithubObject.NotSet
        self._expired = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._expires_at = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "size_in_bytes" in attributes:  # pragma no branch
            self._size_in_bytes = self._makeIntAttribute(attributes["size_in_bytes"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "archive_download_url" in attributes:  # pragma no branch
            self._archive_download_url = self._makeStringAttribute(
                attributes["archive_download_url"]
            )
        if "expired" in attributes:  # pragma no branch
            self._expired = self._makeBoolAttribute(attributes["expired"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "expires_at" in attributes:  # pragma no branch
            self._expires_at = self._makeDatetimeAttribute(attributes["expires_at"])
