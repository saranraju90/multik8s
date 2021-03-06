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
"""Delete node template command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute import flags as compute_flags
from googlecloudsdk.command_lib.compute.sole_tenancy.node_templates import flags
from googlecloudsdk.core.console import console_io


class Delete(base.DeleteCommand):
  """Delete a Compute Engine node template."""

  detailed_help = {
      'brief': 'Delete a Compute Engine node template.',
      'EXAMPLES': """
         To delete a node template, run:

           $ {command} my-node-template
       """
  }

  @staticmethod
  def Args(parser):
    flags.MakeNodeTemplateArg().AddArgument(parser)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    client = holder.client

    node_template_ref = flags.MakeNodeTemplateArg().ResolveAsResource(
        args, holder.resources,
        scope_lister=compute_flags.GetDefaultScopeLister(holder.client))

    console_io.PromptContinue(
        'You are about to delete node template: [{}]'.format(
            node_template_ref.Name()),
        throw_if_unattended=True, cancel_on_no=True)

    messages = holder.client.messages
    request = messages.ComputeNodeTemplatesDeleteRequest(
        nodeTemplate=node_template_ref.Name(),
        project=node_template_ref.project,
        region=node_template_ref.region)

    service = holder.client.apitools_client.nodeTemplates
    return client.MakeRequests([(service, 'Delete', request)])
