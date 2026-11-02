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


class OrgFreedesktopSystemd1UnitInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.systemd1.Unit",
):
    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def start(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def stop(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def reload(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def try_restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def reload_or_restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="s",
        result_signature="o",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job',),
    )
    async def reload_or_try_restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ss",
        result_signature="uososa(uosos)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('job_id', 'job_path', 'unit_id', 'unit_path', 'job_type', 'affected_jobs'),
    )
    async def enqueue_job(
        self,
        job_type: str,
        job_mode: str,
    ) -> tuple[int, str, str, str, str, list[tuple[int, str, str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="si",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def kill(
        self,
        whom: str,
        signal: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="si",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def kill_subgroup(
        self,
        subgroup: str,
        signal: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sii",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def queue_signal(
        self,
        whom: str,
        signal: int,
        value: int,
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
        input_signature="ba(sv)",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def set_properties(
        self,
        runtime: bool,
        properties: list[tuple[str, tuple[str, Any]]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def ref(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def unref(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="as",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def clean(
        self,
        mask: list[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def freeze(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def thaw(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def id(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def names(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def following(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def requires(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def requisite(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def wants(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def binds_to(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def part_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def upholds(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def required_by(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def requisite_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def wanted_by(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def bound_by(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def upheld_by(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def consists_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def conflicts(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def conflicted_by(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def before(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def after(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def on_success(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def on_success_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def on_failure(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def on_failure_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def triggers(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def triggered_by(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def propagates_reload_to(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def reload_propagated_from(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def propagates_stop_to(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def stop_propagated_from(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def joins_namespace_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def slice_of(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def requires_mounts_for(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def wants_mounts_for(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def documentation(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def description(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="AccessSELinuxContext",
    )
    def access_selinux_context(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def load_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def active_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def freezer_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def sub_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def fragment_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def source_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def drop_in_paths(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def unit_file_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def unit_file_preset(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def state_change_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def state_change_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def inactive_exit_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def inactive_exit_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def active_enter_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def active_enter_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def active_exit_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def active_exit_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def inactive_enter_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def inactive_enter_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def can_start(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def can_stop(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def can_reload(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def can_isolate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def can_clean(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def can_freeze(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def can_live_mount(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(uo)",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def job(self) -> tuple[int, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def stop_when_unneeded(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def refuse_manual_start(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def refuse_manual_stop(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def allow_isolate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def default_dependencies(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def survive_final_kill_signal(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def on_success_job_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def on_failure_job_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def ignore_on_isolate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def need_daemon_reload(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def markers(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="JobTimeoutUSec",
    )
    def job_timeout_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="JobRunningTimeoutUSec",
    )
    def job_running_timeout_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def job_timeout_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def job_timeout_reboot_argument(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def condition_result(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def assert_result(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def condition_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def condition_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def assert_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def assert_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sbbsi)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def conditions(self) -> list[tuple[str, bool, bool, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sbbsi)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def asserts(self) -> list[tuple[str, bool, bool, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(ss)",
        flags=DbusPropertyConstFlag,
    )
    def load_error(self) -> tuple[str, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def transient(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def perpetual(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="StartLimitIntervalUSec",
    )
    def start_limit_interval_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def start_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def start_limit_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def failure_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def failure_action_exit_status(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def success_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def success_action_exit_status(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def reboot_argument(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="InvocationID",
    )
    def invocation_id(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def collect_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def refs(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def activation_details(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def debug_invocation(self) -> bool:
        raise NotImplementedError


class OrgFreedesktopSystemd1ServiceInterface(
    DbusInterfaceCommonAsync,
    interface_name="org.freedesktop.systemd1.Service",
):
    @dbus_method_async(
        input_signature="ssbb",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def bind_mount(
        self,
        source: str,
        destination: str,
        read_only: bool,
        mkdir: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="ssbba(ss)",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def mount_image(
        self,
        source: str,
        destination: str,
        read_only: bool,
        mkdir: bool,
        options: list[tuple[str, str]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="a(suuutuusu)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('entries',),
    )
    async def dump_file_descriptor_store(
        self,
    ) -> list[tuple[str, int, int, int, int, int, int, str, int]]:
        raise NotImplementedError

    @dbus_method_async(
        result_signature="a(sus)",
        flags=DbusUnprivilegedFlag,
        result_args_names=('processes',),
    )
    async def get_processes(
        self,
    ) -> list[tuple[str, int, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="sau",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def attach_processes(
        self,
        subcgroup: str,
        pids: list[int],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature="st",
        flags=DbusUnprivilegedFlag,
        result_args_names=(),
    )
    async def remove_subgroup(
        self,
        subcgroup: str,
        flags: int,
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def exit_type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def restart(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def restart_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="PIDFile",
    )
    def pidfile(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def notify_access(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="RestartUSec",
    )
    def restart_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def restart_steps(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="RestartMaxDelayUSec",
    )
    def restart_max_delay_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="RestartUSecNext",
    )
    def restart_usec_next(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="TimeoutStartUSec",
    )
    def timeout_start_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="TimeoutStopUSec",
    )
    def timeout_stop_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="TimeoutAbortUSec",
    )
    def timeout_abort_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def timeout_start_failure_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def timeout_stop_failure_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="RuntimeMaxUSec",
    )
    def runtime_max_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="RuntimeRandomizedExtraUSec",
    )
    def runtime_randomized_extra_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="WatchdogUSec",
    )
    def watchdog_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def watchdog_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def watchdog_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def root_directory_start_only(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def remain_after_exit(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="GuessMainPID",
    )
    def guess_main_pid(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(aiai)",
        flags=DbusPropertyConstFlag,
    )
    def restart_prevent_exit_status(self) -> tuple[list[int], list[int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(aiai)",
        flags=DbusPropertyConstFlag,
    )
    def restart_force_exit_status(self) -> tuple[list[int], list[int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(aiai)",
        flags=DbusPropertyConstFlag,
    )
    def success_exit_status(self) -> tuple[list[int], list[int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="MainPID",
    )
    def main_pid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="ControlPID",
    )
    def control_pid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def bus_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def file_descriptor_store_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        property_name="NFileDescriptorStore",
    )
    def nfile_descriptor_store(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def file_descriptor_store_preserve(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def status_text(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def status_errno(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def status_bus_error(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def status_varlink_error(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def reload_result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def clean_result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def live_mount_result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="USBFunctionDescriptors",
    )
    def usbfunction_descriptors(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="USBFunctionStrings",
    )
    def usbfunction_strings(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="UID",
    )
    def uid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="GID",
    )
    def gid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="NRestarts",
    )
    def nrestarts(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="OOMPolicy",
    )
    def oompolicy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sst)",
        flags=DbusPropertyConstFlag,
    )
    def open_file(self) -> list[tuple[str, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def extra_file_descriptor_names(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def reload_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def refresh_on_reload(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_exit_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_exit_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_handoff_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_handoff_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyEmitsChangeFlag,
        property_name="ExecMainPID",
    )
    def exec_main_pid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_code(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyEmitsChangeFlag,
    )
    def exec_main_status(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_condition(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_condition_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_pre(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_pre_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_post(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_post_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_reload(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_reload_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_reload_post(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_reload_post_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasbttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop_post(self) -> list[tuple[str, list[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sasasttttuii)",
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop_post_ex(self) -> list[tuple[str, list[str], list[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def slice(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def control_group(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def control_group_id(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_current(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_peak(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_swap_current(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_swap_peak(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="MemoryZSwapCurrent",
    )
    def memory_zswap_current(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_available(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def effective_memory_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def effective_memory_high(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="CPUUsageNSec",
    )
    def cpuusage_nsec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        property_name="EffectiveCPUs",
    )
    def effective_cpus(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def effective_memory_nodes(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def tasks_current(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def effective_tasks_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IPIngressBytes",
    )
    def ipingress_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IPIngressPackets",
    )
    def ipingress_packets(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IPEgressBytes",
    )
    def ipegress_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IPEgressPackets",
    )
    def ipegress_packets(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IOReadBytes",
    )
    def ioread_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IOReadOperations",
    )
    def ioread_operations(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IOWriteBytes",
    )
    def iowrite_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IOWriteOperations",
    )
    def iowrite_operations(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="OOMKills",
    )
    def oomkills(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="ManagedOOMKills",
    )
    def managed_oomkills(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def delegate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def delegate_controllers(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def delegate_subgroup(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="CPUWeight",
    )
    def cpuweight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="StartupCPUWeight",
    )
    def startup_cpuweight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="CPUQuotaPerSecUSec",
    )
    def cpuquota_per_sec_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="CPUQuotaPeriodUSec",
    )
    def cpuquota_period_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        property_name="AllowedCPUs",
    )
    def allowed_cpus(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        property_name="StartupAllowedCPUs",
    )
    def startup_allowed_cpus(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def allowed_memory_nodes(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
    )
    def startup_allowed_memory_nodes(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="CPUSetPartition",
    )
    def cpuset_partition(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        property_name="IOAccounting",
    )
    def ioaccounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IOWeight",
    )
    def ioweight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="StartupIOWeight",
    )
    def startup_ioweight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(st)",
        property_name="IODeviceWeight",
    )
    def iodevice_weight(self) -> list[tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(st)",
        property_name="IOReadBandwidthMax",
    )
    def ioread_bandwidth_max(self) -> list[tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(st)",
        property_name="IOWriteBandwidthMax",
    )
    def iowrite_bandwidth_max(self) -> list[tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(st)",
        property_name="IOReadIOPSMax",
    )
    def ioread_iopsmax(self) -> list[tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(st)",
        property_name="IOWriteIOPSMax",
    )
    def iowrite_iopsmax(self) -> list[tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(st)",
        property_name="IODeviceLatencyTargetUSec",
    )
    def iodevice_latency_target_usec(self) -> list[tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def memory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_min(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_low(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def startup_memory_low(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_high(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def startup_memory_high(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def startup_memory_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def memory_swap_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def startup_memory_swap_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="MemoryZSwapMax",
    )
    def memory_zswap_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="StartupMemoryZSwapMax",
    )
    def startup_memory_zswap_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        property_name="MemoryZSwapWriteback",
    )
    def memory_zswap_writeback(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def device_policy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
    )
    def device_allow(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def tasks_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
    )
    def tasks_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        property_name="IPAccounting",
    )
    def ipaccounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(iayu)",
        property_name="IPAddressAllow",
    )
    def ipaddress_allow(self) -> list[tuple[int, bytes, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(iayu)",
        property_name="IPAddressDeny",
    )
    def ipaddress_deny(self) -> list[tuple[int, bytes, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        property_name="IPIngressFilterPath",
    )
    def ipingress_filter_path(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        property_name="IPEgressFilterPath",
    )
    def ipegress_filter_path(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
    )
    def disable_controllers(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="ManagedOOMSwap",
    )
    def managed_oomswap(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="ManagedOOMMemoryPressure",
    )
    def managed_oommemory_pressure(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        property_name="ManagedOOMMemoryPressureLimit",
    )
    def managed_oommemory_pressure_limit(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="ManagedOOMMemoryPressureDurationUSec",
    )
    def managed_oommemory_pressure_duration_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="ManagedOOMPreference",
    )
    def managed_oompreference(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        property_name="OOMRules",
    )
    def oomrules(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        property_name="BPFProgram",
    )
    def bpfprogram(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(iiqq)",
    )
    def socket_bind_allow(self) -> list[tuple[int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(iiqq)",
    )
    def socket_bind_deny(self) -> list[tuple[int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bas)",
    )
    def restrict_network_interfaces(self) -> tuple[bool, list[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def bind_network_interface(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
    )
    def memory_pressure_watch(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="MemoryPressureThresholdUSec",
    )
    def memory_pressure_threshold_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="CPUPressureWatch",
    )
    def cpupressure_watch(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="CPUPressureThresholdUSec",
    )
    def cpupressure_threshold_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        property_name="IOPressureWatch",
    )
    def iopressure_watch(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        property_name="IOPressureThresholdUSec",
    )
    def iopressure_threshold_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(iiss)",
        property_name="NFTSet",
    )
    def nftset(self) -> list[tuple[int, int, str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
    )
    def coredump_receive(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def environment(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sb)",
        flags=DbusPropertyConstFlag,
    )
    def environment_files(self) -> list[tuple[str, bool]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def pass_environment(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def unset_environment(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
        property_name="UMask",
    )
    def umask(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitCPU",
    )
    def limit_cpu(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitCPUSoft",
    )
    def limit_cpusoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitFSIZE",
    )
    def limit_fsize(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitFSIZESoft",
    )
    def limit_fsizesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitDATA",
    )
    def limit_data(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitDATASoft",
    )
    def limit_datasoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitSTACK",
    )
    def limit_stack(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitSTACKSoft",
    )
    def limit_stacksoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitCORE",
    )
    def limit_core(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitCORESoft",
    )
    def limit_coresoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitRSS",
    )
    def limit_rss(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitRSSSoft",
    )
    def limit_rsssoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitNOFILE",
    )
    def limit_nofile(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitNOFILESoft",
    )
    def limit_nofilesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitAS",
    )
    def limit_as(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitASSoft",
    )
    def limit_assoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitNPROC",
    )
    def limit_nproc(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitNPROCSoft",
    )
    def limit_nprocsoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitMEMLOCK",
    )
    def limit_memlock(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitMEMLOCKSoft",
    )
    def limit_memlocksoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitLOCKS",
    )
    def limit_locks(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitLOCKSSoft",
    )
    def limit_lockssoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitSIGPENDING",
    )
    def limit_sigpending(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitSIGPENDINGSoft",
    )
    def limit_sigpendingsoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitMSGQUEUE",
    )
    def limit_msgqueue(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitMSGQUEUESoft",
    )
    def limit_msgqueuesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitNICE",
    )
    def limit_nice(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitNICESoft",
    )
    def limit_nicesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitRTPRIO",
    )
    def limit_rtprio(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitRTPRIOSoft",
    )
    def limit_rtpriosoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitRTTIME",
    )
    def limit_rttime(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LimitRTTIMESoft",
    )
    def limit_rttimesoft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def working_directory(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def root_directory(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def root_image(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        flags=DbusPropertyConstFlag,
    )
    def root_image_options(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        flags=DbusPropertyConstFlag,
    )
    def root_hash(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def root_hash_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        flags=DbusPropertyConstFlag,
    )
    def root_hash_signature(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def root_hash_signature_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def root_verity(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def root_ephemeral(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="RootMStack",
    )
    def root_mstack(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def extension_directories(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sba(ss))",
        flags=DbusPropertyConstFlag,
    )
    def extension_images(self) -> list[tuple[str, bool, list[tuple[str, str]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ssba(ss))",
        flags=DbusPropertyConstFlag,
    )
    def mount_images(self) -> list[tuple[str, str, bool, list[tuple[str, str]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="OOMScoreAdjust",
    )
    def oomscore_adjust(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def coredump_filter(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def nice(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="IOSchedulingClass",
    )
    def ioscheduling_class(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="IOSchedulingPriority",
    )
    def ioscheduling_priority(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="CPUSchedulingPolicy",
    )
    def cpuscheduling_policy(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="CPUSchedulingPriority",
    )
    def cpuscheduling_priority(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        flags=DbusPropertyConstFlag,
        property_name="CPUAffinity",
    )
    def cpuaffinity(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="CPUAffinityFromNUMA",
    )
    def cpuaffinity_from_numa(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
        property_name="NUMAPolicy",
    )
    def numapolicy(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        flags=DbusPropertyConstFlag,
        property_name="NUMAMask",
    )
    def numamask(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="TimerSlackNSec",
    )
    def timer_slack_nsec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="CPUSchedulingResetOnFork",
    )
    def cpuscheduling_reset_on_fork(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def non_blocking(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def standard_input(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def standard_input_file_descriptor_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="ay",
        flags=DbusPropertyConstFlag,
    )
    def standard_input_data(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def standard_output(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def standard_output_file_descriptor_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def standard_error(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def standard_error_file_descriptor_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="TTYPath",
    )
    def ttypath(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="TTYReset",
    )
    def ttyreset(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="TTYVHangup",
    )
    def ttyvhangup(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="TTYVTDisallocate",
    )
    def ttyvtdisallocate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="q",
        flags=DbusPropertyConstFlag,
        property_name="TTYRows",
    )
    def ttyrows(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="q",
        flags=DbusPropertyConstFlag,
        property_name="TTYColumns",
    )
    def ttycolumns(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def syslog_priority(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def syslog_identifier(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def syslog_level_prefix(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def syslog_level(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def syslog_facility(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def log_level_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="LogRateLimitIntervalUSec",
    )
    def log_rate_limit_interval_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def log_rate_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="aay",
        flags=DbusPropertyConstFlag,
    )
    def log_extra_fields(self) -> list[bytes]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(bs)",
        flags=DbusPropertyConstFlag,
    )
    def log_filter_patterns(self) -> list[tuple[bool, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def log_namespace(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def secure_bits(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def capability_bounding_set(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def ambient_capabilities(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def user(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def group(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def dynamic_user(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def set_login_environment(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="RemoveIPC",
    )
    def remove_ipc(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(say)",
        flags=DbusPropertyConstFlag,
    )
    def set_credential(self) -> list[tuple[str, bytes]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(say)",
        flags=DbusPropertyConstFlag,
    )
    def set_credential_encrypted(self) -> list[tuple[str, bytes]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        flags=DbusPropertyConstFlag,
    )
    def load_credential(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        flags=DbusPropertyConstFlag,
    )
    def load_credential_encrypted(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def import_credential(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        flags=DbusPropertyConstFlag,
    )
    def import_credential_ex(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def supplementary_groups(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="PAMName",
    )
    def pamname(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def read_write_paths(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def read_only_paths(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def inaccessible_paths(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def exec_paths(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def no_exec_paths(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def exec_search_path(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def mount_flags(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def private_tmp(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def private_tmp_ex(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def private_devices(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def protect_clock(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def protect_kernel_tunables(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def protect_kernel_modules(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def protect_kernel_logs(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def protect_control_groups(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def protect_control_groups_ex(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def private_network(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def private_users(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def private_users_ex(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def private_mounts(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="PrivateIPC",
    )
    def private_ipc(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="PrivatePIDs",
    )
    def private_pids(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def protect_home(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def protect_system(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def same_process_group(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def utmp_identifier(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def utmp_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bs)",
        flags=DbusPropertyConstFlag,
        property_name="SELinuxContext",
    )
    def selinux_context(self) -> tuple[bool, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bs)",
        flags=DbusPropertyConstFlag,
    )
    def app_armor_profile(self) -> tuple[bool, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bs)",
        flags=DbusPropertyConstFlag,
    )
    def smack_process_label(self) -> tuple[bool, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="IgnoreSIGPIPE",
    )
    def ignore_sigpipe(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def no_new_privileges(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bas)",
        flags=DbusPropertyConstFlag,
    )
    def system_call_filter(self) -> tuple[bool, list[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def system_call_architectures(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def system_call_error_number(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bas)",
        flags=DbusPropertyConstFlag,
    )
    def system_call_log(self) -> tuple[bool, list[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def personality(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def lock_personality(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bas)",
        flags=DbusPropertyConstFlag,
    )
    def restrict_address_families(self) -> tuple[bool, list[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sst)",
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory_symlink(self) -> list[tuple[str, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory_preserve(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sst)",
        flags=DbusPropertyConstFlag,
    )
    def state_directory_symlink(self) -> list[tuple[str, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def state_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def state_directory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(tus)",
        flags=DbusPropertyConstFlag,
    )
    def state_directory_quota(self) -> tuple[int, int, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def state_directory(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sst)",
        flags=DbusPropertyConstFlag,
    )
    def cache_directory_symlink(self) -> list[tuple[str, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def cache_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def cache_directory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(tus)",
        flags=DbusPropertyConstFlag,
    )
    def cache_directory_quota(self) -> tuple[int, int, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def cache_directory(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(sst)",
        flags=DbusPropertyConstFlag,
    )
    def logs_directory_symlink(self) -> list[tuple[str, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def logs_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def logs_directory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(tus)",
        flags=DbusPropertyConstFlag,
    )
    def logs_directory_quota(self) -> tuple[int, int, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def logs_directory(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="u",
        flags=DbusPropertyConstFlag,
    )
    def configuration_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="as",
        flags=DbusPropertyConstFlag,
    )
    def configuration_directory(self) -> list[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
        property_name="TimeoutCleanUSec",
    )
    def timeout_clean_usec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def memory_deny_write_execute(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def restrict_realtime(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="RestrictSUIDSGID",
    )
    def restrict_suidsgid(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def restrict_namespaces(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="t",
        flags=DbusPropertyConstFlag,
    )
    def delegate_namespaces(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(bas)",
        flags=DbusPropertyConstFlag,
    )
    def restrict_file_systems(self) -> tuple[bool, list[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ssbt)",
        flags=DbusPropertyConstFlag,
    )
    def bind_paths(self) -> list[tuple[str, str, bool, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ssbt)",
        flags=DbusPropertyConstFlag,
    )
    def bind_read_only_paths(self) -> list[tuple[str, str, bool, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="a(ss)",
        flags=DbusPropertyConstFlag,
    )
    def temporary_file_system(self) -> list[tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="MountAPIVFS",
    )
    def mount_apivfs(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def bind_log_sockets(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def keyring_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def protect_proc(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def proc_subset(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
    )
    def protect_hostname(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(ss)",
        flags=DbusPropertyConstFlag,
    )
    def protect_hostname_ex(self) -> tuple[str, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="PrivateBPF",
    )
    def private_bpf(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="BPFDelegateCommands",
    )
    def bpfdelegate_commands(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="BPFDelegateMaps",
    )
    def bpfdelegate_maps(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="BPFDelegatePrograms",
    )
    def bpfdelegate_programs(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="BPFDelegateAttachments",
    )
    def bpfdelegate_attachments(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="MemoryKSM",
    )
    def memory_ksm(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="MemoryTHP",
    )
    def memory_thp(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def user_namespace_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def network_namespace_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
        property_name="IPCNamespacePath",
    )
    def ipcnamespace_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def root_image_policy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def mount_image_policy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def extension_image_policy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(tt)",
    )
    def state_directory_quota_usage(self) -> tuple[int, int]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(tt)",
    )
    def cache_directory_quota_usage(self) -> tuple[int, int]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="(tt)",
    )
    def logs_directory_quota_usage(self) -> tuple[int, int]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="s",
        flags=DbusPropertyConstFlag,
    )
    def kill_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def kill_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def restart_kill_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def final_kill_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="SendSIGKILL",
    )
    def send_sigkill(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="b",
        flags=DbusPropertyConstFlag,
        property_name="SendSIGHUP",
    )
    def send_sighup(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature="i",
        flags=DbusPropertyConstFlag,
    )
    def watchdog_signal(self) -> int:
        raise NotImplementedError

