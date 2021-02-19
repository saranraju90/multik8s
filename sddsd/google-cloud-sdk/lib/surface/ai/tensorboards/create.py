# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""AI Platform endpoints create command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import encoding
from googlecloudsdk.api_lib.ai import operations
from googlecloudsdk.api_lib.ai.tensorboards import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.ai import constants
from googlecloudsdk.command_lib.ai import endpoint_util
from googlecloudsdk.command_lib.ai import flags
from googlecloudsdk.command_lib.ai import operations_util
from googlecloudsdk.command_lib.ai import tensorboards_util
from googlecloudsdk.command_lib.ai import validation
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import log


def _Run(args, version):
  """Create a new AI Platform Tensorboard."""
  validation.ValidateDisplayName(args.display_name)

  region_ref = args.CONCEPTS.region.Parse()
  args.region = region_ref.AsDict()['locationsId']
  with endpoint_util.AiplatformEndpointOverrides(version, region=args.region):
    tensorboards_client = client.TensorboardsClient()
    operation_client = operations.OperationsClient()
    op = tensorboards_client.Create(region_ref, args)
    response_msg = operations_util.WaitForOpMaybe(
        operation_client, op,
        tensorboards_util.ParseTensorboardOperation(op.name))
    if response_msg is not None:
      response = encoding.MessageToPyValue(response_msg)
      if 'name' in response:
        log.status.Print(
            ('Created AI Platform Tensorboard: {}.').format(response['name']))
    return response_msg


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Create(base.CreateCommand):
  """Create a new AI Platform Tensorboard."""

  @staticmethod
  def Args(parser):
    flags.AddRegionResourceArg(parser, 'to create a Tensorboard')
    flags.GetDisplayNameArg('tensorboard').AddToParser(parser)
    flags.GetDescriptionArg('tensorboard').AddToParser(parser)
    labels_util.AddCreateLabelsFlags(parser)

  def Run(self, args):
    return _Run(args, constants.ALPHA_VERSION)
