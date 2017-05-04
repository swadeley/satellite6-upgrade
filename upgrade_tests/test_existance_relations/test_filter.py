"""Upgrade TestSuite for validating Satellite role filters existence and
associations post upgrade

:Requirement: Upgraded Satellite

:CaseAutomation: Automated

:CaseLevel: Acceptance

:CaseComponent: CLI

:TestType: NonFunctional

:CaseImportance: High

:Upstream: No
"""
import pytest
from upgrade_tests.helpers.existence import compare_postupgrade, pytest_ids


# Required Data
component = 'filter'
fil_rtype = compare_postupgrade(component, 'resource type')
fil_search = compare_postupgrade(component, 'resource type')
fil_unlimited = compare_postupgrade(component, 'unlimited?')
fil_role = compare_postupgrade(component, 'role')
fil_perm = compare_postupgrade(component, 'permissions')


@pytest.mark.parametrize("pre,post", fil_rtype, ids=pytest_ids(fil_rtype))
def test_positive_filters_by_resource_type(pre, post):
    """Test all filters of all roles are existing after upgrade by resource
    types

    :id: 362f4b0c-49bb-424d-92e4-446ec59b8c5c

    :expectedresults: All filters of all roles should be retained post upgrade
        by resource types
    """
    assert pre == post


@pytest.mark.parametrize("pre,post", fil_search, ids=pytest_ids(fil_search))
def test_positive_filters_by_search(pre, post):
    """Test all filters search criteria is existing after upgrade

    :id: da2dd076-f0e6-45ee-8a5d-99f2e083aabc

    :expectedresults: All filters search criteria should be retained post
        upgrade
    """
    assert pre == post


@pytest.mark.parametrize(
    "pre,post", fil_unlimited, ids=pytest_ids(fil_unlimited))
def test_positive_filters_by_unlimited_check(pre, post):
    """Test all filters unlimited criteria is existing after upgrade

    :id: abf65640-dc9b-415e-846d-0df43391228f

    :expectedresults: All filters unlimited criteria should be retained post
        upgrade
    """
    assert pre == post


@pytest.mark.parametrize("pre,post", fil_role, ids=pytest_ids(fil_role))
def test_positive_filters_by_role(pre, post):
    """Test all filters association with role is existing after upgrade

    :id: dffdc0ac-a4b5-4b70-8e4d-fb37765f75ed

    :expectedresults: All filters association with role should be retained post
        upgrade
    """
    assert pre == post


@pytest.mark.parametrize("pre,post", fil_perm, ids=pytest_ids(fil_perm))
def test_positive_filters_by_permissions(pre, post):
    """Test all filters all permissions are existing after upgrade

    :id: dd4fab7e-bd8f-4645-8aab-42a14ffe3a0e

    :expectedresults: All filters all permissions should be retained post
        upgrade
    """
    assert pre == post
