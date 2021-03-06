# -*- coding: utf-8 -*- #
# Copyright 2018 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command group for Cloud Monitoring channel descriptors."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class ChannelDescriptors(base.Group):
  """Read Cloud Monitoring notification channel descriptors."""

  detailed_help = {
      'DESCRIPTION':
          """\
          Manage Monitoring notification channel descriptors.

          More information can be found here:
          https://cloud.google.com/monitoring/api/v3/
          https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors
          https://cloud.google.com/monitoring/alerts/using-channels-api
      """
  }
