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
"""Wraps a Cloud Run job message with convenience methods."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import enum
from googlecloudsdk.api_lib.run import container_resource
from googlecloudsdk.api_lib.run import k8s_object

AUTHOR_ANNOTATION = k8s_object.RUN_GROUP + '/creator'

STARTED_CONDITION = 'Started'
COMPLETED_CONDITION = 'Completed'


class RestartPolicy(enum.Enum):
  NEVER = 'Never'
  ON_FAILURE = 'OnFailure'


class Job(k8s_object.KubernetesObject):
  """Wraps a Cloud Run job message, making fields more convenient."""

  API_CATEGORY = 'run.googleapis.com'
  KIND = 'Job'
  READY_CONDITION = COMPLETED_CONDITION
  TERMINAL_CONDITIONS = frozenset({STARTED_CONDITION, READY_CONDITION})

  @classmethod
  def New(cls, client, namespace):
    """Produces a new Job object.

    Args:
      client: The Cloud Run API client.
      namespace: str, The serving namespace.

    Returns:
      A new Job object to be deployed.
    """
    ret = super(Job, cls).New(client, namespace)
    ret.spec.template.spec.containers = [client.MESSAGES_MODULE.Container()]
    return ret

  class InstanceTemplateSpec(container_resource.ContainerResource):
    """Wrapper class for Job subfield InstanceTemplateSpec."""

    KIND = 'InstanceTemplateSpec'

    @classmethod
    def SpecAndAnnotationsOnly(cls, job):
      """Special wrapper for spec only that also covers metadata annotations.

      For a message type without its own metadata, like InstanceTemplateSpec,
      metadata fields should either raise AttributeErrors or refer to the
      metadata of a different message depending on use case. This method handles
      the annotations of metadata by referencing the parent job's annotations.
      All other metadata fields will fall through to k8s_object which will
      lead to AttributeErrors.

      Args:
        job: The parent job for this InstanceTemplateSpec

      Returns:
        A new k8s_object to wrap the InstanceTemplateSpec with only the spec
        fields and the metadata annotations.
      """
      spec_wrapper = super(Job.InstanceTemplateSpec,
                           cls).SpecOnly(job.spec.template.spec,
                                         job.MessagesModule())
      # pylint: disable=protected-access
      spec_wrapper._annotations = job.annotations
      return spec_wrapper

    @property
    def annotations(self):
      """Override to return the parent job's annotations."""
      try:
        return self._annotations
      except AttributeError:
        raise ValueError(
            'Job templates do not have their own annotations. Initialize the '
            'wrapper with SpecAndAnnotationsOnly to be able to use annotations.'
        )

    @property
    def restart_policy(self):
      """Returns the enum version of the restart policy."""
      return RestartPolicy(self.spec.restartPolicy)

    @restart_policy.setter
    def restart_policy(self, enum_value):
      self.spec.restartPolicy = enum_value.value

    @property
    def service_account(self):
      """The service account to use as the container identity."""
      return self.spec.serviceAccountName

    @service_account.setter
    def service_account(self, value):
      self.spec.serviceAccountName = value

  @property
  def template(self):
    return Job.InstanceTemplateSpec.SpecAndAnnotationsOnly(self)

  @property
  def author(self):
    return self.annotations.get(AUTHOR_ANNOTATION)

  @property
  def image(self):
    return self.template.image

  @image.setter
  def image(self, value):
    self.template.image = value

  @property
  def parallelism(self):
    return self.spec.parallelism

  @parallelism.setter
  def parallelism(self, value):
    self.spec.parallelism = value

  @property
  def completions(self):
    return self.spec.completions

  @completions.setter
  def completions(self, value):
    self.spec.completions = value

  @property
  def backoff_limit(self):
    return self.spec.backoffLimit

  @backoff_limit.setter
  def backoff_limit(self, value):
    self.spec.backoffLimit = value
