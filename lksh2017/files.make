# -*- Makefile -*-
# $Id$

# Copyright (C) 2007-2009 Alexander Chernov <cher@ejudge.ru> */

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

USERLIST_CLNT_MODULES = \
 ${EJUDGEROOT}/userlist_clnt/admin_process.c\
 ${EJUDGEROOT}/userlist_clnt/change_registration.c\
 ${EJUDGEROOT}/userlist_clnt/close.c\
 ${EJUDGEROOT}/userlist_clnt/cnts_passwd_op.c\
 ${EJUDGEROOT}/userlist_clnt/control.c\
 ${EJUDGEROOT}/userlist_clnt/copy_user_info.c\
 ${EJUDGEROOT}/userlist_clnt/create_member.c\
 ${EJUDGEROOT}/userlist_clnt/create_user.c\
 ${EJUDGEROOT}/userlist_clnt/delete_cookie.c\
 ${EJUDGEROOT}/userlist_clnt/delete_field.c\
 ${EJUDGEROOT}/userlist_clnt/delete_info.c\
 ${EJUDGEROOT}/userlist_clnt/do_pass_fd.c\
 ${EJUDGEROOT}/userlist_clnt/edit_field.c\
 ${EJUDGEROOT}/userlist_clnt/get_cookie.c\
 ${EJUDGEROOT}/userlist_clnt/get_database.c\
 ${EJUDGEROOT}/userlist_clnt/get_fd.c\
 ${EJUDGEROOT}/userlist_clnt/get_info.c\
 ${EJUDGEROOT}/userlist_clnt/import_csv_users.c\
 ${EJUDGEROOT}/userlist_clnt/list_all_users.c\
 ${EJUDGEROOT}/userlist_clnt/login.c\
 ${EJUDGEROOT}/userlist_clnt/logout.c\
 ${EJUDGEROOT}/userlist_clnt/lookup_cookie.c\
 ${EJUDGEROOT}/userlist_clnt/lookup_user.c\
 ${EJUDGEROOT}/userlist_clnt/lookup_user_id.c\
 ${EJUDGEROOT}/userlist_clnt/move_member.c\
 ${EJUDGEROOT}/userlist_clnt/open.c\
 ${EJUDGEROOT}/userlist_clnt/pass_fd.c\
 ${EJUDGEROOT}/userlist_clnt/priv_cookie.c\
 ${EJUDGEROOT}/userlist_clnt/priv_login.c\
 ${EJUDGEROOT}/userlist_clnt/read_and_notify.c\
 ${EJUDGEROOT}/userlist_clnt/recv_packet.c\
 ${EJUDGEROOT}/userlist_clnt/register_contest.c\
 ${EJUDGEROOT}/userlist_clnt/register_new_2.c\
 ${EJUDGEROOT}/userlist_clnt/send_packet.c\
 ${EJUDGEROOT}/userlist_clnt/set_cookie.c\
 ${EJUDGEROOT}/userlist_clnt/set_passwd.c\
 ${EJUDGEROOT}/userlist_clnt/team_cookie.c\
 ${EJUDGEROOT}/userlist_proto.c\
 ${EJUDGEROOT}/xml_utils/parse_ip.c\
 ${EJUDGEROOT}/unix/sock_op_enable_creds.c\
 ${EJUDGEROOT}/unix/sock_op_put_creds.c\
 ${EJUDGEROOT}/unix/sock_op_put_fds.c

