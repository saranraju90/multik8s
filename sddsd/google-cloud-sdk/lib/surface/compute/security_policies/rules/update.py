# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
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
"""Command for updating security policies rules."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute.security_policies import client
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.compute.security_policies import flags as security_policy_flags
from googlecloudsdk.command_lib.compute.security_policies.rules import flags
from googlecloudsdk.core import properties


class UpdateHelper(object):
  r"""Update a Compute Engine security policy rule.

  *{command}* is used to update security policy rules.

  For example to update the description and IP ranges of a rule at priority
  1000, run:

        $ {command} 1000 \
            --security-policy my-policy \
            --description "block 1.2.3.4/32" \
            --src-ip-ranges 1.2.3.4/32
  """

  @classmethod
  def Args(cls, parser, support_redirect):
    """Generates the flagset for an Update command."""
    flags.AddPriority(parser, 'update')
    cls.SECURITY_POLICY_ARG = (
        security_policy_flags.SecurityPolicyArgumentForRules())
    cls.SECURITY_POLICY_ARG.AddArgument(parser)
    flags.AddMatcher(parser, required=False)
    flags.AddAction(
        parser, required=False, support_redirect=support_redirect)
    flags.AddDescription(parser)
    flags.AddPreview(parser, default=None)
    if support_redirect:
      flags.AddRedirectTarget(parser)

  @classmethod
  def Run(cls, release_track, args, support_redirect):
    """Validates arguments and patches a security policy rule."""
    if not any([
        args.description, args.src_ip_ranges, args.expression, args.action,
        args.preview is not None
    ]):
      raise exceptions.MinimumArgumentException([
          '--description', '--src-ip-ranges', '--expression', '--action',
          '--preview'
      ], 'At least one property must be modified.')

    holder = base_classes.ComputeApiHolder(release_track)
    ref = holder.resources.Parse(
        args.name,
        collection='compute.securityPolicyRules',
        params={
            'project': properties.VALUES.core.project.GetOrFail,
            'securityPolicy': args.security_policy
        })
    security_policy_rule = client.SecurityPolicyRule(
        ref, compute_client=holder.client)

    redirect_target = None
    if support_redirect:
      redirect_target = args.redirect_target

    return security_policy_rule.Patch(
        src_ip_ranges=args.src_ip_ranges,
        expression=args.expression,
        action=args.action,
        description=args.description,
        preview=args.preview,
        redirect_target=redirect_target)


@base.ReleaseTracks(base.ReleaseTrack.GA)
class UpdateGA(base.UpdateCommand):
  r"""Update a Compute Engine security policy rule.

  *{command}* is used to update security policy rules.

  For example to update the description and IP ranges of a rule at priority
  1000, run:

        $ {command} 1000 \
            --security-policy my-policy \
            --description "block 1.2.3.4/32" \
            --src-ip-ranges 1.2.3.4/32
  """

  SECURITY_POLICY_ARG = None

  _support_redirect = False

  @classmethod
  def Args(cls, parser):
    UpdateHelper.Args(parser, support_redirect=False)

  def Run(self, args):
    return UpdateHelper.Run(self.ReleaseTrack(), args,
                            self._support_redirect)


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class UpdateBeta(base.UpdateCommand):
  r"""Update a Compute Engine security policy rule.

  *{command}* is used to update security policy rules.

  For example to update the description and IP ranges of a rule at priority
  1000, run:

        $ {command} 1000 \
            --security-policy my-policy \
            --description "block 1.2.3.4/32" \
            --src-ip-ranges 1.2.3.4/32
  """

  SECURITY_POLICY_ARG = None

  _support_redirect = False

  @classmethod
  def Args(cls, parser):
    UpdateHelper.Args(parser, support_redirect=False)

  def Run(self, args):
    return UpdateHelper.Run(self.ReleaseTrack(), args,
                            self._support_redirect)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class UpdateAlpha(base.UpdateCommand):
  r"""Update a Compute Engine security policy rule.

  *{command}* is used to update security policy rules.

  For example to update the description and IP ranges of a rule at priority
  1000, run:

        $ {command} 1000 \
            --security-policy my-policy \
            --description "block 1.2.3.4/32" \
            --src-ip-ranges 1.2.3.4/32
  """

  SECURITY_POLICY_ARG = None

  _support_redirect = True

  @classmethod
  def Args(cls, parser):
    UpdateHelper.Args(
        parser, support_redirect=cls._support_redirect)

  def Run(self, args):
    return UpdateHelper.Run(self.ReleaseTrack(), args,
                            self._support_redirect)
