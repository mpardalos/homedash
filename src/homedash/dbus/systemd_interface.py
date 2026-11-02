from __future__ import annotations

from typing import Any

from sdbus import (
    DbusDeprecatedFlag,
    DbusInterfaceCommonAsync,
    DbusNoReplyFlag,
    DbusPropertyConstFlag,
    DbusPropertyEmitsChangeFlag,
    DbusPropertyEmitsInvalidationFlag,
    DbusPropertyExplicitFlag,
    DbusUnprivilegedFlag,
    dbus_method_async,
    dbus_property_async,
    dbus_signal_async,
)


class OrgFreedesktopSystemd1ManagerInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.systemd1.Manager",
):
    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('unit',),
    )
    async def get_unit(
        self,
        name: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="u",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        method_name="GetUnitByPID",
        result_args_names=('unit',),
    )
    async def get_unit_by_pid(
        self,
        pid: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ay",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        method_name="GetUnitByInvocationID",
        result_args_names=('unit',),
    )
    async def get_unit_by_invocation_id(
        self,
        invocation_id: bytes,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('unit',),
    )
    async def get_unit_by_control_group(
        self,
        cgroup: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="h",
        result_signature="osay",
        flags=DbusUnprivilegedFlag,
        method_name="GetUnitByPIDFD",
        result_args_names=('unit', 'unit_id', 'invocation_id'),
    )
    async def get_unit_by_pidfd(
        self,
        pidfd: int,
    ) -> tuple[str, str, bytes]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('unit',),
    )
    async def load_unit(
        self,
        name: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def start_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sst",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def start_unit_with_flags(
        self,
        name: str,
        mode: str,
        flags: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def start_unit_replace(
        self,
        old_unit: str,
        new_unit: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def stop_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def reload_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def try_restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def reload_or_restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def reload_or_try_restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sss",
        result_signature="uososa(uosos)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job_id', 'job_path', 'unit_id', 'unit_path', 'job_type', 'affected_jobs'),
    )
    async def enqueue_unit_job(
        self,
        name: str,
        job_type: str,
        job_mode: str,
    ) -> tuple[int, str, str, str, str, list[tuple[int, str, str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ssi",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def kill_unit(
        self,
        name: str,
        whom: str,
        signal: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sssi",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def kill_unit_subgroup(
        self,
        name: str,
        whom: str,
        subgroup: str,
        signal: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ssii",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def queue_signal_unit(
        self,
        name: str,
        whom: str,
        signal: int,
        value: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sas",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def clean_unit(
        self,
        name: str,
        mask: list[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def freeze_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def thaw_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def reset_failed_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sba(sv)",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def set_unit_properties(
        self,
        name: str,
        runtime: bool,
        properties: list[tuple[str, tuple[str, Any]]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sssbb",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def bind_mount_unit(
        self,
        name: str,
        source: str,
        destination: str,
        read_only: bool,
        mkdir: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sssbba(ss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def mount_image_unit(
        self,
        name: str,
        source: str,
        destination: str,
        read_only: bool,
        mkdir: bool,
        options: list[tuple[str, str]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def ref_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def unref_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ssa(sv)a(sa(sv))",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def start_transient_unit(
        self,
        name: str,
        mode: str,
        properties: list[tuple[str, tuple[str, Any]]],
        aux: list[tuple[str, list[tuple[str, tuple[str, Any]]]]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="a(sus)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('processes',),
    )
    async def get_unit_processes(
        self,
        name: str,
    ) -> list[tuple[str, int, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ssau",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def attach_processes_to_unit(
        self,
        unit_name: str,
        subcgroup: str,
        pids: list[int],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sst",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def remove_subgroup_from_unit(
        self,
        unit_name: str,
        subcgroup: str,
        flags: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def abandon_scope(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="u",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def get_job(
        self,
        id: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="u",
        result_signature="a(usssoo)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('jobs',),
    )
    async def get_job_after(
        self,
        id: int,
    ) -> list[tuple[int, str, str, str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="u",
        result_signature="a(usssoo)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('jobs',),
    )
    async def get_job_before(
        self,
        id: int,
    ) -> list[tuple[int, str, str, str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="u",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def cancel_job(
        self,
        id: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def clear_jobs(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def reset_failed(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def set_show_status(
        self,
        mode: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="a(ssssssouso)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('units',),
    )
    async def list_units(
        self,
    ) -> list[tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        result_signature="a(ssssssouso)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('units',),
    )
    async def list_units_filtered(
        self,
        states: list[str],
    ) -> list[tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asas",
        result_signature="a(ssssssouso)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('units',),
    )
    async def list_units_by_patterns(
        self,
        states: list[str],
        patterns: list[str],
    ) -> list[tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        result_signature="a(ssssssouso)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('units',),
    )
    async def list_units_by_names(
        self,
        names: list[str],
    ) -> list[tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="a(usssoo)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('jobs',),
    )
    async def list_jobs(
        self,
    ) -> list[tuple[int, str, str, str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def subscribe(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def unsubscribe(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=('output',),
    )
    async def dump(
        self,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        result_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=('output',),
    )
    async def dump_units_matching_patterns(
        self,
        patterns: list[str],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="h",
        flags=DbusUnprivilegedFlag,
        result_args_names=('fd',),
    )
    async def dump_by_file_descriptor(
        self,
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        result_signature="h",
        flags=DbusUnprivilegedFlag,
        result_args_names=('fd',),
    )
    async def dump_units_matching_patterns_by_file_descriptor(
        self,
        patterns: list[str],
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def reload(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def reexecute(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
            result_args_names=(),
    )
    async def exit(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
            result_args_names=(),
    )
    async def reboot(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_args_names=(),
    )
    async def soft_reboot(
        self,
        new_root: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
            result_args_names=(),
    )
    async def power_off(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
            result_args_names=(),
    )
    async def halt(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        method_name="KExec",
        result_args_names=(),
    )
    async def kexec(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_args_names=(),
    )
    async def switch_root(
        self,
        new_root: str,
        init: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def set_environment(
        self,
        assignments: list[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def unset_environment(
        self,
        names: list[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asas",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def unset_and_set_environment(
        self,
        names: list[str],
        assignments: list[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="ao",
        flags=DbusUnprivilegedFlag,
        result_args_names=('jobs',),
    )
    async def enqueue_marked_jobs(
        self,
    ) -> list[str]:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="a(ss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('unit_files',),
    )
    async def list_unit_files(
        self,
    ) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asas",
        result_signature="a(ss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('unit_files',),
    )
    async def list_unit_files_by_patterns(
        self,
        states: list[str],
        patterns: list[str],
    ) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=('state',),
    )
    async def get_unit_file_state(
        self,
        file: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asbb",
        result_signature="ba(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('carries_install_info', 'changes'),
    )
    async def enable_unit_files(
        self,
        files: list[str],
        runtime: bool,
        force: bool,
    ) -> tuple[bool, list[tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def disable_unit_files(
        self,
        files: list[str],
        runtime: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ast",
        result_signature="ba(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('carries_install_info', 'changes'),
    )
    async def enable_unit_files_with_flags(
        self,
        files: list[str],
        flags: int,
    ) -> tuple[bool, list[tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ast",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def disable_unit_files_with_flags(
        self,
        files: list[str],
        flags: int,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ast",
        result_signature="ba(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('carries_install_info', 'changes'),
    )
    async def disable_unit_files_with_flags_and_install_info(
        self,
        files: list[str],
        flags: int,
    ) -> tuple[bool, list[tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asbb",
        result_signature="ba(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('carries_install_info', 'changes'),
    )
    async def reenable_unit_files(
        self,
        files: list[str],
        runtime: bool,
        force: bool,
    ) -> tuple[bool, list[tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asbb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def link_unit_files(
        self,
        files: list[str],
        runtime: bool,
        force: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asbb",
        result_signature="ba(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('carries_install_info', 'changes'),
    )
    async def preset_unit_files(
        self,
        files: list[str],
        runtime: bool,
        force: bool,
    ) -> tuple[bool, list[tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="assbb",
        result_signature="ba(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('carries_install_info', 'changes'),
    )
    async def preset_unit_files_with_mode(
        self,
        files: list[str],
        mode: str,
        runtime: bool,
        force: bool,
    ) -> tuple[bool, list[tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asbb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def mask_unit_files(
        self,
        files: list[str],
        runtime: bool,
        force: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def unmask_unit_files(
        self,
        files: list[str],
        runtime: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def revert_unit_files(
        self,
        files: list[str],
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def set_default_target(
        self,
        name: str,
        force: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="s",
        flags=DbusUnprivilegedFlag,
        result_args_names=('name',),
    )
    async def get_default_target(
        self,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sbb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def preset_all_unit_files(
        self,
        mode: str,
        runtime: bool,
        force: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="asssbb",
        result_signature="a(sss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('changes',),
    )
    async def add_dependency_unit_files(
        self,
        files: list[str],
        target: str,
        type: str,
        runtime: bool,
        force: bool,
    ) -> list[tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sb",
        result_signature="as",
        flags=DbusUnprivilegedFlag,
        result_args_names=('links',),
    )
    async def get_unit_file_links(
        self,
        name: str,
        runtime: bool,
    ) -> list[str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="y",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def set_exit_code(
        self,
        number: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="u",
        flags=DbusUnprivilegedFlag,
        result_args_names=('uid',),
    )
    async def lookup_dynamic_user_by_name(
        self,
        name: str,
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="u",
        result_signature="s",
        flags=DbusUnprivilegedFlag,
        method_name="LookupDynamicUserByUID",
        result_args_names=('name',),
    )
    async def lookup_dynamic_user_by_uid(
        self,
        uid: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="a(us)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('users',),
    )
    async def get_dynamic_users(
        self,
    ) -> list[tuple[int, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="a(suuutuusu)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('entries',),
    )
    async def dump_unit_file_descriptor_store(
        self,
        name: str,
    ) -> list[tuple[str, int, int, int, int, int, int, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def version(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def features(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def virtualization(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def confidential_virtualization(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def architecture(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def tainted(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def firmware_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def firmware_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def loader_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def loader_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def kernel_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def kernel_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDTimestamp",
    )
    def init_rdtimestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDTimestampMonotonic",
    )
    def init_rdtimestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def userspace_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def userspace_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def shutdown_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def shutdown_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def security_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def security_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def security_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def security_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def generators_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def generators_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def generators_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def generators_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def units_load_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def units_load_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def units_load_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def units_load_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def units_load_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def units_load_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDSecurityStartTimestamp",
    )
    def init_rdsecurity_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDSecurityStartTimestampMonotonic",
    )
    def init_rdsecurity_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDSecurityFinishTimestamp",
    )
    def init_rdsecurity_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDSecurityFinishTimestampMonotonic",
    )
    def init_rdsecurity_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDGeneratorsStartTimestamp",
    )
    def init_rdgenerators_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDGeneratorsStartTimestampMonotonic",
    )
    def init_rdgenerators_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDGeneratorsFinishTimestamp",
    )
    def init_rdgenerators_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDGeneratorsFinishTimestampMonotonic",
    )
    def init_rdgenerators_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDUnitsLoadStartTimestamp",
    )
    def init_rdunits_load_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDUnitsLoadStartTimestampMonotonic",
    )
    def init_rdunits_load_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDUnitsLoadFinishTimestamp",
    )
    def init_rdunits_load_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="InitRDUnitsLoadFinishTimestampMonotonic",
    )
    def init_rdunits_load_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def log_level(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def log_target(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        property_name="NNames",
    )
    def nnames(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="NFailedUnits",
    )
    def nfailed_units(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        property_name="NJobs",
    )
    def njobs(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        property_name="NInstalledJobs",
    )
    def ninstalled_jobs(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        property_name="NFailedJobs",
    )
    def nfailed_jobs(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="at",
    )
    def transactions_with_ordering_cycle(self) -> list[int]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="d",
    )
    def progress(self) -> float:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def environment(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def confirm_spawn(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def show_status(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def unit_path(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def default_standard_output(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def default_standard_error(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def watchdog_device(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def watchdog_last_ping_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def watchdog_last_ping_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="RuntimeWatchdogUSec",
    )
    def runtime_watchdog_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="RuntimeWatchdogPreUSec",
    )
    def runtime_watchdog_pre_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def runtime_watchdog_pre_governor(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="RebootWatchdogUSec",
    )
    def reboot_watchdog_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="KExecWatchdogUSec",
    )
    def kexec_watchdog_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def service_watchdogs(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def control_group(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def system_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="y",
    )
    def exit_code(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultTimerAccuracyUSec",
    )
    def default_timer_accuracy_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultTimeoutStartUSec",
    )
    def default_timeout_start_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultTimeoutStopUSec",
    )
    def default_timeout_stop_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="DefaultTimeoutAbortUSec",
    )
    def default_timeout_abort_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultDeviceTimeoutUSec",
    )
    def default_device_timeout_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultRestartUSec",
    )
    def default_restart_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultStartLimitIntervalUSec",
    )
    def default_start_limit_interval_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def default_start_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="EventLoopRateLimitIntervalUSec",
    )
    def event_loop_rate_limit_interval_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def event_loop_rate_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="DefaultIOAccounting",
    )
    def default_ioaccounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="DefaultIPAccounting",
    )
    def default_ipaccounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def default_memory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def default_tasks_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitCPU",
    )
    def default_limit_cpu(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitCPUSoft",
    )
    def default_limit_cpusoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitFSIZE",
    )
    def default_limit_fsize(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitFSIZESoft",
    )
    def default_limit_fsizesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitDATA",
    )
    def default_limit_data(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitDATASoft",
    )
    def default_limit_datasoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitSTACK",
    )
    def default_limit_stack(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitSTACKSoft",
    )
    def default_limit_stacksoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitCORE",
    )
    def default_limit_core(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitCORESoft",
    )
    def default_limit_coresoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitRSS",
    )
    def default_limit_rss(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitRSSSoft",
    )
    def default_limit_rsssoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitNOFILE",
    )
    def default_limit_nofile(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitNOFILESoft",
    )
    def default_limit_nofilesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitAS",
    )
    def default_limit_as(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitASSoft",
    )
    def default_limit_assoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitNPROC",
    )
    def default_limit_nproc(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitNPROCSoft",
    )
    def default_limit_nprocsoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitMEMLOCK",
    )
    def default_limit_memlock(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitMEMLOCKSoft",
    )
    def default_limit_memlocksoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitLOCKS",
    )
    def default_limit_locks(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitLOCKSSoft",
    )
    def default_limit_lockssoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitSIGPENDING",
    )
    def default_limit_sigpending(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitSIGPENDINGSoft",
    )
    def default_limit_sigpendingsoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitMSGQUEUE",
    )
    def default_limit_msgqueue(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitMSGQUEUESoft",
    )
    def default_limit_msgqueuesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitNICE",
    )
    def default_limit_nice(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitNICESoft",
    )
    def default_limit_nicesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitRTPRIO",
    )
    def default_limit_rtprio(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitRTPRIOSoft",
    )
    def default_limit_rtpriosoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitRTTIME",
    )
    def default_limit_rttime(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="DefaultLimitRTTIMESoft",
    )
    def default_limit_rttimesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def default_tasks_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="DefaultMemoryPressureThresholdUSec",
    )
    def default_memory_pressure_threshold_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def default_memory_pressure_watch(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="DefaultCPUPressureThresholdUSec",
    )
    def default_cpupressure_threshold_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="DefaultCPUPressureWatch",
    )
    def default_cpupressure_watch(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="DefaultIOPressureThresholdUSec",
    )
    def default_iopressure_threshold_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="DefaultIOPressureWatch",
    )
    def default_iopressure_watch(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="TimerSlackNSec",
    )
    def timer_slack_nsec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="DefaultOOMPolicy",
    )
    def default_oompolicy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="DefaultOOMScoreAdjust",
    )
    def default_oomscore_adjust(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="DefaultRestrictSUIDSGID",
    )
    def default_restrict_suidsgid(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def ctrl_alt_del_burst_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def soft_reboots_count(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def reload_count(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="DefaultMemoryZSwapWriteback",
    )
    def default_memory_zswap_writeback(self) -> bool:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="so",
        signal_args_names=('id', 'unit'),
    )
    def unit_new(self) -> tuple[str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="so",
        signal_args_names=('id', 'unit'),
    )
    def unit_removed(self) -> tuple[str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="uos",
        signal_args_names=('id', 'job', 'unit'),
    )
    def job_new(self) -> tuple[int, str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="uoss",
        signal_args_names=('id', 'job', 'unit', 'result'),
    )
    def job_removed(self) -> tuple[int, str, str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="tttttt",
        signal_args_names=('firmware', 'loader', 'kernel', 'initrd', 'userspace', 'total'),
    )
    def startup_finished(self) -> tuple[int, int, int, int, int, int]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_args_names=(),
    )
    def unit_files_changed(self) -> None:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature="b",
        signal_args_names=('active',),
    )
    def reloading(self) -> bool:
        raise NotImplementedError

